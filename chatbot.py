import random
import time

food = ["Rice", "Dessert", "NOTHING.", "Meat (raw)", "Meat (Cooked)", "Idk choose"]
print("Hi lmao Im some kind of chatbot idk")
name = input("Whats ur name?: ")
print("Hi", name, "lmao")
meal = input("Choose a number lol: ")
print("Uh.. okay? Anyways this is what ur having today: ")
time.sleep(2)
print(random.choice(food))

day = input("Okay so uh how's your day?: ")
day = day.lower()
if day == "Good":
    print("Ok lmao")
else:
    print("What")
