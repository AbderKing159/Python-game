import random

class HangmanGame:
  def __init__(self, words):
    self.words = words
    self.word = random.choice(self.words)
    self.incorrect_guesses = 0

    self.correct_letters = []
    self.incorrect_letters = []
  
  def play(self):
    name = input('What is your name: ')
    print(f"Welcome to the game {name} . You will have 6 chances to guess the name of the car , let's get STARTED")

    while True:
      result = []
      for letter in self.word:
        if letter in self.correct_letters:
          result.append(letter)
        else:
          result.append("_")

      print(" ".join(result))
      print("Incorrect guesses:", self.incorrect_guesses)
      print("Incorrect letters:", " ".join(self.incorrect_letters))

      if "_" not in result:
        print(f"Congratulations {name}, you won!")
        break
      if self.incorrect_guesses == 6:
        print("Sorry, you lost. The word was", self.word)
        break

      guess = input("Guess a letter: ")

      if guess in self.word:
        self.correct_letters.append(guess)
      else:
        self.incorrect_guesses += 1
        self.incorrect_letters.append(guess)

cars = ["dacia", "ford", "tesla", "fiat","toyota","lexus","audi"]
game = HangmanGame(cars)
game.play()
