import random
import termcolor


def select_word():
  with open("badwords.txt", "r") as file:
    words = file.readlines()
  return random.choice(words).strip().lower()


def check_guess(word, guess):
  if len(guess) != len(word):
    return False
  for i in range(len(word)):
    if guess[i] == word[i]:
      print(termcolor.colored(guess[i], "green"), end="")
    elif guess[i] in word:
      print(termcolor.colored(guess[i], "yellow"), end="")
    else:
      print(termcolor.colored(guess[i], "grey"), end="")
  print()
  return guess == word


def play_wordle():
  word = select_word()
  guessed = False
  guesses = 0
  while not guessed:
    guess = input("Enter your guess: ").strip().lower()
    guessed = check_guess(word, guess)
    guesses += 1
  print(
    f"Congratulations! You guessed the word '{word}' in {guesses} guesses.")


play_wordle()
