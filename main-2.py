import random 
from words import words
import string

def valid_word(words):
  word = random.choice(words)
  while '-' or ' 'in word:
    word = random.choice(words)
  return word.upper

def hangman():
  word = valid_word(words)
  #letters in the word
  word_letters = set(word)
  alph = set(string.ascii_uppercase)
  
  #letters user has guessed 
  used_letters = set()

  # number of lives
  lives = 6
  while len(word_letters) > 0 and lives > 0: 
    #used letters
    print("you have", lives, "lives left and you used these following leters", ' '.join(used_letters))

    #current word
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print("Current word is ", ' '.join(word_list) )

      #user input
    user_letter = input("Type a letter: ").upper()
    
  # if this letter is a valid character in the alphabet where it has not been used yet then add to used letters 
    if user_letter in alph - used_letters:
      used_letters.add(user_letter)
  # if the letter was guessed correctly, then remove from word letters
      if user_letter in word_letters:
        word_letters.remove(user_letter)
      else:
        lives -= 1
        print("letter is not in word")
      
    elif user_letter in used_letters:
      print("you have already used this letter, guess again")
    else:
      print("inavlid character: plase try again")
  if lives == 0:
    print('You died, sorry. The word was', word)
  else:
    print('YAY! You guessed the word', word, '!!')
if __name__ == '__main__':
    hangman()

  
  
    