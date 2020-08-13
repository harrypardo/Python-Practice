from nltk.corpus import words
import random

def get_word():
    word_list = words.words()
    while True:
        word = word_list[random.randint(1, len(word_list))]
        if len(word) >= 3:
            return word

def display_word(word, guess, letter):
    for index, w in enumerate(list(word)):
        if w == letter:
            guess = guess[:index] + letter + guess[index + 1:]
    return guess

def hangman():
    lives = 6
    done = set()
    word = get_word()
    word_set = set(list(word))
    current_word = "*" * len(word)
    print("Guess the word: ")

    while True:
        print(current_word)
        print("Guess a letter:")
        letter = input()
        if letter in done:
            print("You already guessed that letter!")
        elif letter in word_set:
            done.add(letter)
            current_word = display_word(word, current_word, letter)
            print("You guessed a letter!")
            if current_word == word:
                print("You won!")
                break
        else:
            lives -= 1
            print("Wrong letter! Lives: " + str(lives))
            if lives == 0:
                print("You lose")
                print("The word was " + word)
                break

if __name__ == '__main__':
    hangman()