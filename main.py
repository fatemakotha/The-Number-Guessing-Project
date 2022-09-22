import random
from art import logo
print(logo)
print("Welcome to The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

correct_answer = random.randint(1, 101) #picks a random number from 1 - 100
print(type(correct_answer)) #prints: int
print(f"The correct answer is {correct_answer}")

question = input("Do you want the Easy or the Hard level?")
if question == "easy":
    lives = 10
elif question == "hard":
    lives = 5
print(f"You chose {question} so you have {lives} lives")






game_is_over = False
while not game_is_over:
    guess = int(input("Enter a number from 1 - 100: "))
    
    
    if guess == correct_answer:
        game_is_over = True
        print("YOU WIN")
        
    elif guess > correct_answer:
        print("Too High")
        lives -= 1
        print(lives)
        if lives == 0:
            game_is_over = True
            print("You lost all lives. You lose.")
        
    elif guess < correct_answer:
        print("Too low")
        lives -= 1
        print(lives)
        if lives == 0:
            game_is_over = True
            print("You lost all lives. You lose.")
        


    