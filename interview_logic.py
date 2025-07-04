import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# logic.py

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from prompts import question_prompt, evaluation_prompt, summary_prompt

llm = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()

# Chains
question_chain = question_prompt | llm | parser
evaluation_chain = evaluation_prompt | llm | parser
summary_chain = summary_prompt | llm | parser
