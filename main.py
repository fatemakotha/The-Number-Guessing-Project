import random

print("Welcome to The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

correct_answer = random.randint(1, 101) #picks a random number from 1 - 100
print(f"The correct answer is {correct_answer}")