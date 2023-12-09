import random
from hangman_stages import stages, logo, line
from hangman_words import word_list
chosen_word = random.choice(word_list)

#Hangman's logo
print(logo)

display = []

for letter in range(len(chosen_word)):
    display.append("_")
lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(line)
        print("You already chosen this " + guess +
              "letter, guess another letter")
    for n in range(len(chosen_word)):
        if guess == chosen_word[n]:
            display[n] = guess

    if guess not in chosen_word:
        lives -= 1
        print(line)
        print('\n' + guess + " is wrong letter, You lost a life")
    if lives == 0:
        end_of_game = True
        print("You lose")

    print(f"\n{' '.join(display)}")
    print(stages[lives])
        

    if '_' not in display:
        end_of_game = True
        print("You win")
