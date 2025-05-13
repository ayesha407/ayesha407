import random

def get_random_word(): words = ['python', 'hangman', 'challenge', 'programming', 'algorithm'] return random.choice(words)

def display_word(word, guessed_letters): return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game(): word = get_random_word() guessed_letters = set() attempts = 6

print('Welcome to Hangman!')
print(display_word(word, guessed_letters))

while attempts > 0:
    guess = input('Guess a letter: ').lower()

    if len(guess) != 1 or not guess.isalpha():
        print('Please enter a single alphabetic character.')
        continue

    if guess in guessed_letters:
        print('You already guessed that letter. Try again.')
        continue

    guessed_letters.add(guess)

    if guess in word:
        print('Correct guess!')
    else:
        attempts -= 1
        print(f'Incorrect guess. You have {attempts} attempts left.')

    current_display = display_word(word, guessed_letters)
    print(current_display)

    if '_' not in current_display:
        print('Congratulations! You guessed the word:', word)
        break
else:
    print('Game Over! The word was:', word)

if name == 'main': play_game()
