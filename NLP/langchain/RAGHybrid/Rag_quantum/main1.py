import os
from dotenv import load_dotenv

# LangChain
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader


from qiskit_optimization import QuadraticProgram
from qiskit_algorithms.minimum_eigensolvers import NumPyMinimumEigensolver
from qiskit_optimization.algorithms import MinimumEigenOptimizer
load_dotenv()


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


loader = TextLoader("data/knowledge.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

splits = splitter.split_documents(docs)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(splits, embeddings)

retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

def optimize_chunks(docs, query):
    """
    Select best 3 chunks using QUBO + classical solver
    """

    n = len(docs)

    # Simple relevance scoring
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

    # Maximize relevance → minimize negative
    qp.minimize(linear={f"x{i}": -scores[i] for i in range(n)})

    # Constraint: select exactly 3 chunks
    qp.linear_constraint(
        linear={f"x{i}": 1 for i in range(n)},
        sense="==",
        rhs=3,
        name="limit_chunks"
    )

    # Solve with NumPyMinimumEigensolver
    solver = NumPyMinimumEigensolver()
    optimizer = MinimumEigenOptimizer(solver)

    result = optimizer.solve(qp)

    selected_docs = []
    for i, val in enumerate(result.x):
        if val == 1:
            selected_docs.append(docs[i])

    return selected_docs



def rag_with_optimization(query):
    # Step 1: Retrieve
    docs = retriever.invoke(query)

    print(f"\nRetrieved {len(docs)} chunks")

    # Step 2: Optimize
    selected_docs = optimize_chunks(docs, query)

    print(f"Selected {len(selected_docs)} chunks (optimized)")

    # Step 3: Build context
    context = "\n".join([d.page_content for d in selected_docs])

    # Step 4: LLM
    prompt = f"""
Answer using ONLY the context below:

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response.content



if __name__ == "__main__":
    print("RAG + Optimization System (Qiskit 2.x Ready)")

    while True:
        query = input("\nYou: ")

        if query.lower() == "exit":
            break

        answer = rag_with_optimization(query)

        print("\nAI:", answer)
        print("-" * 50)