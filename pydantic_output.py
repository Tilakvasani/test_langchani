from typing import TypedDict,Annotated,Literal
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel,Field
load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile")

class Review(BaseModel):
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos","neg"]= Field(description='return sentiment of the review either positive or negative')

stru=model.with_structured_output(Review)
result=stru.invoke("""The sound in VS Code happens because of Audio Cues or Accessibility Signals that play a sound when errors or warnings appear.
It is a built-in feature, not an extension.""")
result=dict(result)
print(result)
print(result['summary'])
print(result['sentiment'])