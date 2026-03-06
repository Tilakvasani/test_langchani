from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()
model=ChatGroq(model='llama-3.3-70b-versatile')
parser =StrOutputParser()

prompt1=PromptTemplate(
    template='generate a tweet about {topic} (only 4 to 8 line)',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='generate a Linkedin about {topic} (only 4 to 8 line)',
    input_variables=['topic']
)

parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'Linkedin':RunnableSequence(prompt2,model,parser)
})

result=parallel_chain.invoke({'topic':'ai'})
print("about tweet:- \n"+result['tweet']+"\n\nabout Linkedin:- \n"+result['Linkedin'])