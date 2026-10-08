import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    def __init__(self, length=5):
        self.length = length
        self.target = random.choice([w for w in WORDS if len(w) == length])
        self.history = []

    def _print_history(self):
        print("History:")
        if not self.history:
            print("  (none)")
            return
        for number, (guess, feedback) in enumerate(self.history, start=1):
            print(f"{number}. {guess}  {' '.join(feedback)}")

    def _print_summary(self, result, guesses_used):
        print("Session summary:")
        print("Target:", self.target)
        print("Result:", result)
        print("Valid guesses:", guesses_used)
        self._print_history()

    def run(self):
        print(f"Wordle — {self.length} letters, 6 guesses.")
        guesses_used = 0
        result = "lost"
        while guesses_used < 6:
            guess = input("> ").strip().lower()
            if guess == "q":
                result = "quit"
                break
            if len(guess) != self.length or not guess.isalpha():
                print("Enter a valid word of the required length.")
                continue
            guesses_used += 1
            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))
            self._print_history()
            if guess == self.target:
                print("Solved!")
                result = "won"
                break
        if result == "lost":
            print("The word was:", self.target)
        self._print_summary(result, guesses_used)
