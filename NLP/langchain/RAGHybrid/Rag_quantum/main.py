import os
import numpy as np
from dotenv import load_dotenv

# LangChain
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Quantum
from qiskit_optimization import QuadraticProgram
from qiskit_algorithms import QAOA
from qiskit.primitives import Sampler
from qiskit_optimization.algorithms import MinimumEigenOptimizer
load_dotenv()


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


loader = TextLoader("data/knowledge.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
splits = splitter.split_documents(docs)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(splits, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 10})


def quantum_select_chunks(docs, query):
    """
    Select best subset of chunks using QUBO
    """

    n = len(docs)

    # Simple relevance score (length + keyword match)
    scores = []
    for d in docs:
        text = d.page_content.lower()
        score = 0
        for word in query.lower().split():
            if word in text:
                score += 2
        score += len(text) * 0.001
        scores.append(score)

    # Build QUBO
    qp = QuadraticProgram()

    for i in range(n):
        qp.binary_var(name=f"x{i}")

    # Objective: maximize relevance (convert to minimize)
    qp.minimize(linear={f"x{i}": -scores[i] for i in range(n)})

    # Constraint: select only 3 chunks
    qp.linear_constraint(
        linear={f"x{i}": 1 for i in range(n)},
        sense="==",
        rhs=3,
        name="limit_chunks"
    )

    # Solve
    qaoa = QAOA(sampler=Sampler())
    optimizer = MinimumEigenOptimizer(qaoa)

    result = optimizer.solve(qp)

    selected = []
    for i, val in enumerate(result.x):
        if val == 1:
            selected.append(docs[i])

    return selected



def rag_with_quantum(query):
    docs = retriever.invoke(query)
    print(f"\nRetrieved {len(docs)} chunks")
    selected_docs = quantum_select_chunks(docs, query)
    print(f"Selected {len(selected_docs)} chunks via quantum")
    context = "\n".join([d.page_content for d in selected_docs])
    prompt = f"""
Answer the question using context:

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":
    print(" RAG + Quantum Optimization System Ready")

    while True:
        q = input("\nYou: ")
        if q.lower() == "exit":
            break

        answer = rag_with_quantum(q)
        print("\nAI:", answer)