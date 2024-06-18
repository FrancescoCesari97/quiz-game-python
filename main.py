#  quiz game

questions = ("How many elements are in the periodic table?: ",
             "which animal lays the largest eggs?: ",
             "what is the most abundat gas in Earth atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116","B 117","C 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))

answer = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D):").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        score += 1
        print("correct!")
    else:
        print("incorrect!")
        print(f"{answer[question_num]} is the correct answer")


    question_num += 1
    print()

    print(f"your total score is {score}/{len(answer)}")

    score = int(score / len(answer) * 100)


    print(f"your total score is {score}%")