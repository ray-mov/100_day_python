import random

words = ["apple", "banana", "orange", "grape", "melon", "kiwi", "mango", "pear", "peach", "plum"]
life = 5
chosen_word = random.choice(words)
word_len = len(chosen_word)
display_word = ["_"]* word_len

print(" ".join(display_word))

guessed_letters = set()

while "_" in display_word and life:
   guess = input("Please guess a letter : ").lower()
   
   if not guess.isalpha() and len(guess) != 1:
     print("Please Enter a valid character ! ")
     continue
   
   if guess in guessed_letters:
     print('You already choose that  word ')
     continue
   
   guessed_letters.add(guess)
   
   if guess in chosen_word:
     print("You guessed correctly")
     for i in range(word_len):
       if chosen_word[i] == guess:
         display_word[i] = guess
   else:
     life -=1
     print(f"Wrong guess. Lives left: {life}")

   print(" ".join(display_word))
     
   
  

# Game over messages
if "_" not in display_word:
    print(f"\n🎉 Congrats! You guessed the word: {chosen_word}")
else:
    print(f"\n💀 Game Over! The word was: {chosen_word}")
