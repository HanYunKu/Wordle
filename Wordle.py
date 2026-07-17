import requests
from colorama import Fore, init

init(autoreset=True)

def main():
    response = requests.get("https://random-word-api.herokuapp.com/word?length=5")
    data = response.json()
    secretWord = data[0]   # API already gives a single word

    print("_ " * len(secretWord))

    guess = input("Guess the word: ")

    while guess != secretWord:
        while len(guess) != len(secretWord):
            guess = input("It's a five-letter word, guess again: ")

        for i in range(len(guess)):
            if guess[i] == secretWord[i]:
                print(Fore.GREEN + guess[i], end="")
            elif guess[i] in secretWord:
                print(Fore.YELLOW + guess[i], end="")
            else:
                print("_", end="")

        guess = input("\nGuess the word: ")

    print("Victory!")

main()
