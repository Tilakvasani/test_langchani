from typing import TypedDict,Annotated
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile")

class Review(TypedDict):
    summary: Annotated[str,"A brief summary of the review "]
    sentiment: Annotated[str,"return sentiment of the review negative,positive or neutral"]
    
stru=model.with_structured_output(Review)


result=stru.invoke("""The sound in VS Code happens because of Audio Cues or Accessibility Signals that play a sound when errors or warnings appear.
It is a built-in feature, not an extension.""")

print(result)
print(result['summary'])
print(result['sentiment'])