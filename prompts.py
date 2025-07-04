# prompts.py

from langchain_core.prompts import ChatPromptTemplate

# Technical question prompt
question_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a technical interviewer. Ask a question on {topic}."),
    ("human", "Start the interview.")
])

# Evaluation prompt
evaluation_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert evaluator. Score the answer out of 10 and explain."),
    ("human", "Question: {question}\nAnswer: {answer}")
])

# Summary prompt
summary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You summarize interview results."),
    ("human", "Evaluate the performance:\n{evaluations}")
])
