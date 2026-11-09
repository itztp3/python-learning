import random
from datetime import datetime

# Smart Quiz Master & Performance Analyzer

questions = [
    {
        "question": "Which language is commonly used for AI?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. XML"],
        "answer": "B"
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. <!--", "D. **"],
        "answer": "B"
    },
    {
        "question": "Which function gets input from a user?",
        "options": ["A. print()", "B. type()", "C. input()", "D. len()"],
        "answer": "C"
    },
    {
        "question": "Which loop runs while a condition is true?",
        "options": ["A. for", "B. while", "C. if", "D. def"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["A. ", "B. *", "C. //", "D. %"],
        "answer": "B"
    },
    {
        "question": "Which method adds an item to a list?",
        "options": ["A. add()", "B. insert()", "C. append()", "D. push()"],
        "answer": "C"
    },
    {
        "question": "Which function returns the length of a list?",
        "options": ["A. count()", "B. size()", "C. len()", "D. total()"],
        "answer": "C"
    }
]


def save_result(name, score, total, accuracy, grade):
    with open("quiz_results.txt", "a") as file:
        file.write(
            f"{datetime.now()} | {name} | "
            f"{score}/{total} | {accuracy:.2f}% | {grade}\n"
        )


def view_results():
    print("\n========== PREVIOUS RESULTS ==========")

    try:
        with open("quiz_results.txt", "r") as file:
            results = file.read()

            if results.strip():
                print(results)
            else:
                print("No previous results found.")

    except FileNotFoundError:
        print("No results available yet.")


def start_quiz():
    name = input("\nEnter your name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    quiz_questions = random.sample(questions, len(questions))

    score = 0
    wrong_answers = []

    print("\n========== QUIZ STARTED ==========")

    for index, question in enumerate(quiz_questions, start=1):
        print(f"\nQuestion {index}: {question['question']}")

        for option in question["options"]:
            print(option)

        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("Invalid choice! Enter A, B, C or D.")

        if answer == question["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect answer!")
            wrong_answers.append({
                "question": question["question"],
                "your_answer": answer,
                "correct_answer": question["answer"]
            })

    total = len(quiz_questions)
    accuracy = (score / total) * 100

    if accuracy >= 90:
        grade = "Excellent"
    elif accuracy >= 70:
        grade = "Very Good"
    elif accuracy >= 50:
        grade = "Good"
    else:
        grade = "Needs Improvement"

    print("\n========== QUIZ REPORT ==========")
    print("Student Name   :", name)
    print("Total Questions:", total)
    print("Correct Answers:", score)
    print("Wrong Answers  :", len(wrong_answers))
    print(f"Accuracy       : {accuracy:.2f}%")
    print("Performance    :", grade)

    if wrong_answers:
        print("\n========== WRONG ANSWERS ==========")

        for item in wrong_answers:
            print("\nQuestion:", item["question"])
            print("Your Answer:", item["your_answer"])
            print("Correct Answer:", item["correct_answer"])

    save_result(name, score, total, accuracy, grade)
    print("\nResults saved successfully!")


def main():
    while True:
        print("\n================================")
        print("       SMART QUIZ MASTER")
        print("================================")
        print("1. Start Quiz")
        print("2. View Previous Results")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            start_quiz()
        elif choice == "2":
            view_results()
        elif choice == "3":
            print("Thank you for using Smart Quiz Master!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()