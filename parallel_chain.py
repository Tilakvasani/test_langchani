from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

model1 =ChatGroq(model="llama-3.3-70b-versatile")
model2 =ChatGroq(model="llama-3.3-70b-versatile")

prompt1=PromptTemplate(
    template='Generate short and simple notes from the following text \n{text}',
    input_variables=['text']
)
prompt2=PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3=PromptTemplate(
    template='merge the provided notes and quiz into the following into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes','quiz ']
)

parser=StrOutputParser()
parallel_chain=RunnableParallel({
    'notes':prompt1 | model1 | parser,
    'quiz':prompt2 | model2 | parser
})
merage_chain=prompt3 | model1 | parser

chain = parallel_chain | merage_chain
text="""Photosynthesis is the process by which green plants, algae, and some bacteria 
convert sunlight, water, and carbon dioxide into glucose and oxygen. This process 
occurs mainly in the chloroplasts of plant cells, where chlorophyll absorbs sunlight. 
The glucose produced is used as energy for the plant, while oxygen is released as 
a byproduct. Photosynthesis is essential for life on Earth as it forms the base 
of the food chain and regulates atmospheric oxygen levels.
"""

result=chain.invoke({'text':text})


print(result)

chain.get_graph().print_ascii()