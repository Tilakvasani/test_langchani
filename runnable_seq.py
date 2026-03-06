from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence


load_dotenv()

model = ChatGroq(model='llama-3.3-70b-versatile')

parser=StrOutputParser()
prompt1=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='explain the following joke {text}',
    input_variables=['text']
)

prompt3=PromptTemplate(
    template='give me sentiment of the following {explain} is this good or bad (one word)',
    input_variables=['explain']
)
chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser,prompt3,model,parser)

print(chain.invoke({'topic':'AI'}))