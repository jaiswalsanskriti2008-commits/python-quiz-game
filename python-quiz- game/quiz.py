
print("================================")
print("       WELCOME TO QUIZ GAME")
print("================================")

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "2. Which language is used for AI?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "3. How many days are there in a week?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "4. Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "5. What is 10 + 5?",
        "options": ["A. 10", "B. 15", "C. 20", "D. 25"],
        "answer": "B"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct answer is:", q["answer"])

print("\n================================")
print("           QUIZ RESULT")
print("================================")

print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Wrong Answers:", len(questions) - score)
print("Your Score:", score, "/", len(questions))

if score == 5:
    print("Excellent! Perfect Score!")
elif score >= 3:
    print("Good Job! Keep Practicing!")
else:
    print("Try Again! You Can Do Better!")

print("================================")
print("       THANK YOU FOR PLAYING")
print("================================")
