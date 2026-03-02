from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(model="moonshotai/kimi-k2-instruct-0905")
result=llm.invoke("what is the capital of goa")
print(result.content)