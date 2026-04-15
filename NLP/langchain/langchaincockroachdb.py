import asyncio
from langchain_cockroachdb import AsyncCockroachDBVectorStore, CockroachDBEngine
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

async def main():
    # Initialize
    engine = CockroachDBEngine.from_connection_string(
        "cockroachdb://root@localhost:26257/defaultdb?sslmode=disable"
    )
    
    await engine.ainit_vectorstore_table(
        table_name="documents",
        vector_dimension=1536,
    )
    
    vectorstore = AsyncCockroachDBVectorStore(
        engine=engine,
        embeddings=OpenAIEmbeddings(),
        collection_name="documents",
    )
    
    # Add documents
    await vectorstore.aadd_texts([
        "CockroachDB is a distributed SQL database",
        "LangChain makes building LLM apps easy",
    ])
    
    # Search
    results = await vectorstore.asimilarity_search(
        "Tell me about databases",
        k=2
    )
    
    for doc in results:
        print(doc.page_content)
    
    await engine.aclose()

asyncio.run(main())