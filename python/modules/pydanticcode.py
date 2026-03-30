from pydantic import BaseModel, Field, field_validator, model_validator, EmailStr
from typing import List, Optional
#from pydantic_settings import BaseSettings
from langchain_core.tools import tool
from langchain.agents import create_agent

class User(BaseModel):   # class coding with structured data  
    username: Optional[str] = Field(default="kumar", max_length=50)
    email: EmailStr = Field(description="User's email address")
    password:str
    salary: Optional[str] = Field(default="50000", max_length=10)

# Field = default, max_length, min_length, pattern, gt, ge, lt, le, alias, description, title

user = User( email="kumar@test.com", password="password123")
print(user)

class searchinput(BaseModel):
    query: str
    max_results: Optional[int] = Field(default=10, gt=0, le=100, description="Maximum number of search results to return (1-100)")
    url: Optional[str] = Field(default=None, max_length=200, description="URL to search within (optional)")

class outputstructure(BaseModel):
     title: str = 
     sentiment: str = Field(..., description="Sentiment analysis of the search result")
     summary: str = Field(..., description="provide a concise summary of the search result")
     url: str = Field(..., description="URL of the search result")



@tool(args_schema=searchinput)
def search_datbase(query:str, max_results:int, url: Optional[str] = "www.oracle.com") -> List[str]:
      connecting to the database logic

    return f"Searching for '{query}' with max results {max_results} in URL: {url}"


create_agent(
    tools=[search_datbase],
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    Humanmessages = []
    response_format=outputstructure
)



class userinput(BaseModel):
    email: EmailStr = Field(description="User's email address")
    url: Optional[str] = Field(default=None, max_length=200, description="URL to search within (optional)")
    url: List[str] = ["https://docs.oracle.com", "www.google.com"]   

    @field_validator('email')   # @ decorator  cls is the class(email) itself and value is the value of the field
    def check_email_domain(cls, value):
        if not value.endswith('@gmail.com'):
            raise ValueError("Email must be from the domain '@gmail.com")
        return value

    @field_validator('url')
    def check_url(cls, value):
        if value and not value.startswith("https://docs.oracle.com"):
            raise ValueError("URL must start with 'https'")
        return value





