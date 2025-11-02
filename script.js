const currentWordEl = document.getElementById('current-word');
const playerInputEl = document.getElementById('player-input');
const submitBtn = document.getElementById('submit-btn');
const undoBtn = document.getElementById('undo-btn');
const newBtn = document.getElementById('new-btn');
const restartBtn = document.getElementById('restart-btn');
const messageEl = document.getElementById('message');
const usedWordsEl = document.getElementById('used-words');

let wordList;
let currentWord;
let usedWords;
let previousWord;

async function init() {
    const response = await fetch('words.txt');
    const text = await response.text();
    wordList = new Set(text.split('\n').map(word => word.trim().toLowerCase()));
    startGame();
}

function startGame() {
    currentWord = generateRandomWord();
    usedWords = new Set([currentWord]);
    previousWord = null;
    updateUI();
}

function generateRandomWord() {
    const threeLetterWords = [...wordList].filter(word => word.length === 3);
    return threeLetterWords[Math.floor(Math.random() * threeLetterWords.length)];
}

function updateUI() {
    currentWordEl.textContent = currentWord;
    playerInputEl.value = '';
    messageEl.textContent = '';
    usedWordsEl.textContent = [...usedWords].join(', ');
}

function isValidWord(word) {
    return wordList.has(word);
}

function validTransformation(word1, word2) {
    if (word1 === word2) return false;

    const len1 = word1.length;
    const len2 = word2.length;

    if (Math.abs(len1 - len2) > 1) return false;

    if (len1 === len2) { // Rearranging or changing one letter
        if (word1.split('').sort().join('') === word2.split('').sort().join('')) {
            return true;
        }
        let diff = 0;
        for (let i = 0; i < len1; i++) {
            if (word1[i] !== word2[i]) {
                diff++;
            }
        }
        return diff === 1;
    }

    if (len2 === len1 + 1) { // Adding one letter
        for (let i = 0; i < len2; i++) {
            if (word2.slice(0, i) + word2.slice(i + 1) === word1) {
                return true;
            }
        }
    }

    if (len2 === len1 - 1) { // Removing one letter
        for (let i = 0; i < len1; i++) {
            if (word1.slice(0, i) + word1.slice(i + 1) === word2) {
                return true;
            }
        }
    }

    return false;
}


submitBtn.addEventListener('click', () => {
    const playerWord = playerInputEl.value.toLowerCase();

    if (!isValidWord(playerWord)) {
        messageEl.textContent = 'Invalid word.';
        return;
    }

    if (usedWords.has(playerWord)) {
        messageEl.textContent = 'You already used this word!';
        return;
    }

    if (validTransformation(currentWord, playerWord)) {
        previousWord = currentWord;
        currentWord = playerWord;
        usedWords.add(playerWord);
        updateUI();
    } else {
        messageEl.textContent = 'Invalid transformation.';
    }
});

undoBtn.addEventListener('click', () => {
    if (previousWord) {
        const wordToUndo = currentWord;
        usedWords.delete(wordToUndo);
        currentWord = previousWord;
        previousWord = null;
        updateUI();
    } else {
        messageEl.textContent = 'No previous word to undo.';
    }
});

newBtn.addEventListener('click', () => {
    startGame();
});

restartBtn.addEventListener('click', () => {
    init();
});

init();