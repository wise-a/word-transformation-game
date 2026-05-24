# Word Transformation Game

This project is a word transformation game that can be played in two ways: as a command-line application using Python or as a web-based game in your browser.

## Game Rules

The rules of the game are simple:

1.  You start with a random 3-letter word.
2.  On each turn, you must transform the current word into a new, valid word by performing one of the following actions:
    *   **Adding one letter:** For example, "cat" to "cart".
    *   **Removing one letter:** For example, "cart" to "cat".
    *   **Changing one letter:** For example, "cat" to "cot".
    *   **Rearranging the letters:** For example, "cat" to "act".
3.  The new word must be a valid English word.
4.  Words cannot be repeated within the same game.

## How to Play

### Command-Line Version

To play the command-line version of the game, you will need to have Python 3 installed on your system.

1.  Open a terminal or command prompt.
2.  Navigate to the directory where the project files are located.
3.  Run the following command:
    ```bash
    python3 wordtransformation.py
    ```
4.  Follow the on-screen instructions to play the game.

### Web Version

To play the web-based version of the game, you can simply open the `index.html` file in your web browser.

1.  Open your preferred web browser.
2.  Open the `index.html` file from the project directory.
3.  The game will load in your browser, and you can start playing immediately.

Alternatively, you can run a local web server to serve the files. If you have Python 3 installed, you can use the built-in HTTP server.

1.  Open a terminal or command prompt.
2.  Navigate to the directory where the project files are located.
3.  Run the following command:
    ```bash
    python3 -m http.server 8000
    ```
4.  Open your web browser and navigate to `http://localhost:8000`.

## Project Files

*   `wordtransformation.py`: The Python script for the command-line version of the game.
*   `words.txt`: A text file containing a list of valid English words, used as the game's dictionary.
*   `index.html`: The main HTML file for the web-based version of the game.
*   `style.css`: The CSS file for styling the web version.
*   `script.js`: The JavaScript file that contains the logic for the web version.
*   `LICENSE`: The license for the project.
*   `README.md`: This file.
