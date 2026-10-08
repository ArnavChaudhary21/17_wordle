from game import WordleGame
from words import WORDS

if __name__ == "__main__":
    while True:
        choice = input("Choose word length (4, 5, or 6): ").strip()
        if choice not in {"4", "5", "6"}:
            print("Please choose 4, 5, or 6.")
            continue
        length = int(choice)
        if not any(len(word) == length for word in WORDS):
            print(f"No {length}-letter words are available.")
            continue
        WordleGame(length).run()
        break
