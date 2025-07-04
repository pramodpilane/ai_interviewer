from dotenv import load_dotenv
from interview_logic import question_chain, evaluation_chain, summary_chain

load_dotenv()

from sys import stdin

def get_multiline_input(prompt="YOUR ANSWER: (type 'END' to finish):"):
    print(prompt)
    lines = []
    while True:
        line = stdin.readline().rstrip("\n")
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def run_interview(topic: str, num_questions: int):
    evaluations = []

    print(f"\n🧠 Starting Interview on: {topic}")
    print("-" * 50)

    for i in range(num_questions):
        # Generate question
        question = question_chain.invoke({"topic": topic})
        print("\nINTERVIEWER:")
        print(f"{question}\n")

        # Get user answer
        answer = get_multiline_input()

        # Evaluate
        feedback = evaluation_chain.invoke({"question": question, "answer": answer})
        print(f"\n📝 FEEDBACK:\n {feedback}")
        evaluations.append(f"Q{i+1}: {feedback}\n")
        print("-" * 50)

    # Summarize
    print("\n📊 INTERVIEW SUMMARY:")
    summary = summary_chain.invoke({"evaluations": "\n".join(evaluations)})
    print(summary)

if __name__ == "__main__":
    print("Welcome to the AI Technical Interviewer CLI!")
    topic = input("Choose a topic (e.g., Python, ML, JavaScript): ").strip()
    num = int(input("How many questions? (3–5): "))
    run_interview(topic, num)
