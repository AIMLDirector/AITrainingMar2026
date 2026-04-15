from langchain_community.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv
load_dotenv()

search = GoogleSerperAPIWrapper()

response = search.run("latest AI news 2026")
print(response)