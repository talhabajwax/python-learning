questions = [
    ["What is the capital of Pakistan?", "islamabad"],
    ["What is 5 + 3?", "8"],
    ["What is 10 - 4?", "6"],
    ["What is 7 × 2?", "14"],
    ["What is 20 ÷ 4?", "5"],
    ["What color is the sky on a clear day?", "blue"],
    ["How many days are there in a week?", "7"],
    ["Which planet do we live on?", "earth"],
    ["What is the opposite of hot?", "cold"],
    ["How many months are there in a year?", "12"],
    ["Python is a programming language. (yes/no)", "yes"],
    ["Which animal is known as the king of the jungle?", "lion"],
    ["What is the first month of the year?", "january"],
    ["How many hours are there in a day?", "24"],
    ["What do bees make?", "honey"],
    ["What is the largest ocean on Earth?", "pacific"],
    ["How many legs does a spider have?", "8"],
    ["What gas do humans need to breathe?", "oxygen"],
    ["What is the freezing point of water in Celsius?", "0"],
    ["Which device is commonly used to make phone calls?", "phone"]
]

score = 0
for q in questions:
    print(q[0])
    answer = input("Your answer: ").lower()
    if answer == q[1]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
print("Your final score is:", score)