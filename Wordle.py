import random
import requests
from colorama import Fore

response = requests.get("https://random-word-api.herokuapp.com/word?length=5")
data = response.json()
secretWord = random.choice(data)

count = 0
for letters in secretWord:
    count += 1
print(count * "_")
guess = input("Guess the word: ")

while guess != secretWord:
    while len(guess) != len(secretWord):
        guess = input("Its a five-letter word, guess the word again: ")

    for i in range(len(guess)):
        if guess[i] == secretWord[i]:
            print(Fore.GREEN + guess[i], end="")
        elif guess[i] in secretWord:
            print(Fore.YELLOW + guess[i], end="")
        else:
            print(Fore.RESET + '_', end="")

    guess = input(Fore.RESET + "\nGuess the word: ")

print("Victory")