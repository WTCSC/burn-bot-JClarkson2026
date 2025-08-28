import random

respondFirst = [["Sooo...","you wanna be burnt?"],["Okay,", "You and your busted cut are done"],["ello ", "you're done"]]
respondSecond = [["at the ripe age of", "you can even walk on your own"],["serouslly?", "and you still live with your parents?"]]
respondThird = ["the cusine of kings no doubt","I got some baby food if you'd perfer that", "literal child"]
respondFourth = ["wooooo how coool.... i dont care","i've never been! not gonna but glad you had a time"]

askName = input("What's your name? ")
askAge = input("How old are you? ")
askFood = input("What's your favorite food? ")
askPlace = input("What is your favorite place? ")

response = f""
rand = random.randint(0, len(respondFirst)-1)
response += f"{respondFirst[rand][0]} {askName} {respondFirst[rand][1]}\n"
rand = random.randint(0, len(respondSecond)-1)
response += f"{respondSecond[rand][0]} {askAge} {respondSecond[rand][1]}\n"
rand = random.randint(0, len(respondThird)-1)
response += f"{askFood}? {respondThird[rand]}\n"
rand = random.randint(0, len(respondFourth)-1)
response += f"{askPlace}? {respondFourth[rand]}"

print(response)