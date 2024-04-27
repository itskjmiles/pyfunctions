# Task 1
questions = [
    {"question": "What is the capital of France?", "answer": "Paris" or "paris"},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "Shakespeare" or "shakespeare"},
    {"question": "What is 2 + 2?", "answer": "4"}
]

# Task 2
def quiz(questions):
    score = 0
    total_questions = len(questions)

    for i, qna in enumerate(questions, start=1):
        question = qna["question"]
        correct_answer = qna["answer"]
        user_answer = input(f"Question {i}: {question} ").strip().lower()

        if user_answer == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}")

    return score, total_questions

# Task 3
def score_quiz(score, total_questions):
    percentage = (score / total_questions) * 100
    print(f"\nYou got {score} out of {total_questions} questions correct.")
    print(f"Your score: {percentage}%")

def run_quiz():
    print("Welcome to the Quiz!")
    print("Answer the following questions:")

    score, total_questions = quiz(questions)
    score_quiz(score, total_questions)

if __name__ == "__main__":
    run_quiz()
