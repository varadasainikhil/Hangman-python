import random
import hangman_art
import hangman_words
 
word_list = hangman_words.word_list
stages = hangman_art.stages

print(hangman_art.logo)
randomWord = random.choice(word_list)
print(randomWord)

dashes = []
for letter in randomWord:
  dashes.append("-")
print(dashes)
        
score = 0
lives = 7
correctGuesses=[]
while(score < len(randomWord) and lives>0):
    guess = str(input("Enter the letter you guessed: ").lower())
    miss=len(randomWord)
    for i in range(0, len(randomWord)):
        if(guess == randomWord[i]):
            score+=1
            dashes[i] = guess
            correctGuesses.append(guess)
        else:
            miss-=1
    if(miss == 0):
        print("Wrong guess")
        print(stages[lives-1])
        lives-=1
    print(f"".join(dashes))
    if "-" not in dashes:
        print("You win")
    elif(lives == 0):
        print("You have lost all your lives")
        print(f"The correct answer is {randomWord}")