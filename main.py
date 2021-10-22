import json
import random


def show_question(question, category):
    global points
    global fifty_fifte

    print()
    if question.get("category") != category:
        return
    print(question.get("category"))
    print(question["question"])
    print("a: ", question["a"])
    print("b: ", question["b"])
    print("c: ", question["c"])
    print("d: ", question["d"])
    print("e: ", question["e"])
    print("f: ", question["f"])
    print()

    answer = input("Which answer do you choose: ")

    if answer == question["correct answer"]:
        points += 1
        print("Yes, that's the correct answer You already have: ", points, " points")
    elif answer == "e":
        print("Ok you are losing nothing")
    elif answer == "f" and fifty_fifte > 0:
        fifty_fifte -= 1
        while True:
            odp = random.choice(['a', 'b', 'c', 'd'])
            if odp != question["correct answer"]:
                x = random.randint(0, 1)
                if x == 0:
                    print(question["correct answer"])
                    print(odp)
                else:
                    print(odp)
                    print(question["correct answer"])
                break
        answer = input("Which answer do you choose: ")
        if answer == question["correct answer"]:
            points += 1
            print("Yes, that's the correct answer You already have ", points, "points ")
        else:
            print("Unfortunately, wrong answer -1 point")
            points -= 1
    elif answer == "f" and fifty_fifte < 1:
        print("Unfortunately, the aid can no longer be selected. Choose answer again")
        show_question(questions[i])
    else:
        print("Unfortunately, wrong answer -1 point")
        points -= 1


ans = "yes"
ranking = {}
while ans == "yes":
    points = 0
    fifty_fifte = 1
    imie = input("Give your name: ")
    category = "film"
    while True:
        category = input("Provide question categories: ")

        if category in ["python", "film", "fizyka"]:
            break
    with open("quiz.json") as json_file:
        questions = json.load(json_file)

        for i in range(0, len(questions)):
            show_question(questions[i], category)

    print()
    print("It's game over scored number of points is: ", points)
    ranking[imie] = points
    ans = input("Do you want to play again: yes or no: ")


print("Ranking: ")
print(ranking)
