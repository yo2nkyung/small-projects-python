#quiz_program.py

import json

def load_questions(file_path):
    try:
        with open(file_path, 'r') as file:
            questions = json.load(file)
        
        return questions

    except FileNotFoundError:
        print(f"Cannot find file: {file_path}")
        return [] #빈 리스트 반환

def get_user_anwser(question):
    return input(question + " ")

def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def run_quiz(questions):
    score = 0
    for question in questions:
        user_answer = get_user_anwser(question["question"])
        is_correct = check_answer(user_answer, question["answer"])
        if is_correct == True:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question["answer"]}.")
    
    print(f"Your total score is: {score} out of {len(questions)}")
    return

file_path = 'questions.json'
questions = load_questions(file_path)

while True:
    run_quiz(questions)
    
    user_input = input("Do you still want to take quiz? (y/n): ").lower()
    if user_input != 'y':
        break
