from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

chat_history=[
    SystemMessage(content='you are a helpful AI assistant')
]
model=ChatGroq(model="moonshotai/kimi-k2-instruct-0905")

while True:
    user_input=input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: "+result.content)
print(chat_history)