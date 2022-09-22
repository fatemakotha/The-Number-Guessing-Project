import random
from art import logo
print(logo)
print("Welcome to The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

correct_answer = random.randint(1, 101) #picks a random number from 1 - 100
print(type(correct_answer)) #prints: int
print(f"The correct answer is {correct_answer}")

guess = int(input("Enter a number from 1 - 100: "))

if guess == correct_answer:
    print("You win")
elif guess > correct_answer:
    print("Too High")
elif guess < correct_answer:
    print("Too Low")