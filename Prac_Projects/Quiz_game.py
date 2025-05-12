#python quiz game

questions = ("What is my real name?:  ",
             "How old am I?: ",
             "What is my favorite sports?: ",
             "What color are my eyes?: ",
             "Am I cool?: ")

options = (("A.Chosen","B.Batman","C.Xan","D.Xanny"),
           ("A.1","B.100","C.11","D.00"),
           ("A.Football","B.Basketball","C.Swimming","D.Esports"),
           ("A.Black","B.Brown","C.Hazel","D.Green"),
           ("A.Yes","B.No","C.Obviously","D.Hell no"))

answers = ("B","C","B","B","C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("        Results       ")
print("----------------------")

print("answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(guesses) * 100)
print(f"Your score is:  {score}%")