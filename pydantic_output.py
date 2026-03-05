from typing import TypedDict,Annotated,Literal
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel,Field
load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile",temperature=1.5)

class Review(BaseModel):
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos","neg","nut"]= Field(description='return sentiment of the review either positive or negative or nutral')


for temp in [0.0, 0.5, 1.0, 1.5]:
    model = ChatGroq(model="llama-3.3-70b-versatile", temperature=temp)
    stru = model.with_structured_output(Review)
    result = stru.invoke("""
I am deeply happy, truly joyful, completely fulfilled and grateful.
My life is wonderful, my family is healthy, my career is thriving.
But I also feel sad sometimes.
    """)
    print(f"Temp {temp} → {result.sentiment}")