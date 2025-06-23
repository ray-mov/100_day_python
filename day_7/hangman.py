import random

words = ["apple", "banana", "orange", "grape", "melon", "kiwi", "mango", "pear", "peach", "plum"]
life = 5


chosen_word = random.choice(words)
word_len = len(chosen_word)
char_left = word_len

temp_spaces = ""

for num in range(0,word_len):
  temp_spaces+=" _ "

print(temp_spaces)

while char_left and life:
    guess = input("Please guess a letter : ").lower()
    if not guess.isalpha():
      print("Please Enter a valid character ! ")
      continue
    for num in range(0,word_len):
      if chosen_word[num] == guess:
        print("You guess correct")
        char_left-=1
        temp_spaces[num] =" "+ guess + " "
      else:
        print("Oops Wring Guess")
        life-=1
        print(f"Life left {life}")
    print(temp_spaces)
      
         
  
    
    
