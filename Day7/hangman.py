
import random
import os
from hangman_words import words
from hangman_logo import stages,logo
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
print(logo)

guessed_letters = set()

chosen_word = random.choice(words).lower()
display = []

lives = 6
for letter in chosen_word:
    display += "_"
print(f"{' '.join(display)} ")
end_of_game = False
while not end_of_game:
    
    
   
    guess = input("Guess the letter:").lower()
    
    if guess in guessed_letters:
        
        print(f"You the already guessed the letter {guess}")
        continue
    guessed_letters.add(guess)
    clear_screen()
    for position in range(len(chosen_word)):     
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
            
    print(f"{' '.join(display)}")
    if guess in display:
        print(f"You guessed the right letter.")
    if guess not in chosen_word:
        lives -= 1   
        print(f"{guess} is not in the word.")     
        if lives == 0:
         end_of_game = True
         print("YOU LOSE")
         print(f"The correct word was {chosen_word}")

    
    if "_" not in display:
        end_of_game = True
        print("You Won.")
    
    print(stages[lives])
