#using Tuple

questions = ("What is mitochondria?: ",
             "Which animal lays largest egg?: ",
             "How many elements are in the periodic table?: ",
             "How many bones are in the human body?: ",
             "What is the most abundant gas in Earth's atmosphere ")   #Tuple of questions

options = (("A. Bone","B. Organ","C. Power House of cell","D. Car"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. 116","B. 117","C. 118","D. 119"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"))

answers = ("C","D","C","A","A")

guesses = [] #we will be appending our guesses to list that's why used

score  = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess) 
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-----------------------")
print("        RESULTS        ")
print("-----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end = " ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
