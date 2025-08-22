file_path = '/home/user/documents/theword/words.txt' 

import random
import os

def load_dictionary(file_path):
    """Load words from a file into a set."""
    try:
        with open(file_path, 'r') as f:
            return set(word.strip().lower() for word in f)
    except FileNotFoundError:
        print(f"Dictionary file not found at {file_path}. Please provide a valid path.")
        return set()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(script_dir, 'words.txt')

# This line should be moved here, after the function definition and file_path creation
word_list = load_dictionary(file_path)  

def generate_random_word(word_list):
    """Generate a random 3-letter word from the dictionary."""
    three_letter_words = [word for word in word_list if len(word) == 3]
    if three_letter_words:
        return random.choice(three_letter_words) 
    else:
        return None 

# ... rest of your code ...

# ... rest of your code ...

def is_valid_word(word, word_list):
    """Check if a word is valid."""
    return word in word_list

def display_instructions():
    """Display the game instructions."""
    print(
        """
Welcome to the Word Transformation Game!

Rules:
1. You start with a random 3-letter word.
2. On each turn, you must transform the word into another valid word by:
    - Adding one letter.
    - Removing one letter.
    - Rearranging the letters.
3. Words cannot be repeated.

Special Commands:
- "undo": Revert to the previous word.
- "new": Start with a new random word.
- "restart": Start a new game.

Let's begin!
        """
    )

def play_game():
    """Main game loop."""

    if not word_list:  # Use the global word_list
        return

    display_instructions()
    current_word = generate_random_word(word_list)  # Use the global word_list
    print(f"Starting word: {current_word}")

    used_words = {current_word}
    previous_word = None

    while True:
        print(f"\nCurrent word: {current_word}")
        player_word = input("Enter the next word or 'undo', 'new', or 'restart': ").lower()

        if player_word == "undo":
            if previous_word:
                current_word = previous_word
                print(f"Reverted to previous word: {current_word}")
            else:
                print("No previous word to undo.")
            continue

        if player_word == "new":
            current_word = generate_random_word(word_list)
            used_words = {current_word}
            previous_word = None
            print(f"New starting word: {current_word}")
            continue

        if player_word == "restart":
            play_game()  # Restart the game
            return

        if player_word in used_words:
            print("You already used this word! Try again.")
            continue

        if not is_valid_word(player_word, word_list):  # Use the global word_list
            print("Invalid word. Try again.")
            continue

        # Check if the word is a valid transformation
        if valid_transformation(current_word, player_word):
            previous_word = current_word  # Store the previous word
            used_words.add(player_word)
            current_word = player_word
        else:
            print("Invalid transformation. Try again.")

        print(f"Words used: {', '.join(used_words)}")

def valid_transformation(word1, word2):
    """Check if word2 is a valid transformation of word1."""
    if len(word2) == len(word1) + 1:  # Adding one letter
        for i in range(len(word2)):
            if word2[:i] + word2[i+1:] == word1:
                return True
        if word2[:-1] == word1 or word2[1:] == word1:  # Adding a letter at the beginning or end
            return True

    if len(word2) == len(word1) - 1:  # Removing one letter
        for i in range(len(word1)):
            if word1[:i] + word1[i+1:] == word2:
                return True

    if sorted(word1) == sorted(word2):  # Rearranging letters
        return True

    if len(word1) == len(word2): 
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                return True 

    return False

if __name__ == "__main__":
    play_game()
