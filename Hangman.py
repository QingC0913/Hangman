from random import *
word = ["waffle", "pancake", "spaghetti", "meatball", "pizza", "pasta", "cheese", "bread", "cake", "donut", "noodle", "pastry", "popcorn"]
randomIndex = randint(0, len(word)-1)
chosen = word[randomIndex]
dash = []
wrong = []
turns = 6
flag = False

answer=input("Would you like to play? Yes or No ")
if answer == ("no"):
    print("This is the end, then.")

if answer == ("yes"):
    print("Let's start the game! The category is food.")
    print("This word has", len(chosen), "letters")
    for letter in range(len(chosen)):
        dash.append("_")

    while turns > 0:
        flag = False
        guess = input("Guess a letter! ")
        for i in range(len(chosen)):
            if (chosen[i] == guess):
                dash[i] = guess
                flag = True
        if (flag == False):
            wrong.append(guess)
            turns -=1

        print ("Guessing board:", dash)
        print ("Wrong guesses:", wrong)
        if (flag == True):
            answer = input("Can you guess the whole word?")
            if (answer == "yes"):
                wordGuess = input ("What is your guess?")
                if (wordGuess == chosen):
                    print("You win! The word is", chosen+"!")
                    break
    if (turns == 0):
        print ("Sorry, you lose.")
