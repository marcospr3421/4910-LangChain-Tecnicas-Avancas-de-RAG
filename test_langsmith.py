from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's request only based on the given context."),
    ("user", "Question: {question}\nContext: {context}")
])
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
output_parser = StrOutputParser()

chain = prompt | model | output_parser

question = "Can you summarize this morning's meetings?"
context = "During this morning's meeting, we solved all world conflict."
chain.invoke({"question": question, "context": context})