from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model=ChatGroq(model="moonshotai/kimi-k2-instruct-0905",temperature=1.3,max_tokens=20)

result=model.invoke("write a 5 line about virat")
print(result.content)   