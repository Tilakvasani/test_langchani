from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
model=ChatGroq(model="moonshotai/kimi-k2-instruct-0905")

messages=[
    SystemMessage(content='you are a helpful assistant'),
    HumanMessage(content='Tell me about Langchain')
]
result=model.invoke(messages).content

messages.append(AIMessage(content=result))

print(messages)