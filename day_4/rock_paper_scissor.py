import random 

print("Welcome to Rock Paper Scissors Game")
print("""
      choose 1 : ROCK
      Choose 2 : PAPER
      Choose 3 : SCISSOR
      """)


while True:
  try:
      player = int(input("Enter Your Choice : "))
      if(player>3 or player <1):
        print("Wrong Choice. Please Re enter")
      else:
        break
      
  except ValueError:
        print("Invalid input. Please enter a number.")
        

player_com = int(random.randint(1,3))

def showChoice(num):
  if num == 1:
    print("""
                 ,--, /: :\/': :`\/: :\
                |`;  ' `,'   `.;    `: |
                |    |     |  '  |     |.
                | :  |     | pb  |     ||
                | :. |  :  |  :  |  :  | \
                 \__/: :.. : :.. | :.. |  )
                      `---',\___/,\___/ /'
                           `==._ .. . /'
                                `-::-'
          """)
  elif num == 2:
    print("""
                     _.-._
                    | | | |_
                    | | | | |
                    | | | | |
                  _ |  '-._ |
                  \`\`-.'-._;
                   \    '   |
                    \  .`  /
                     |    |
          """)
  else:
    print("""
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/

          """)


print("You Choose")
showChoice(player)
print("Comp Choose")
print(player_com)
showChoice(player_com)

def printWin():
  print("You Win")

if(player == 1 and player_com == 3 ):
  printWin()
elif(player == 2 and player_com == 1):
  printWin()
elif(player == 3 and player_com == 2):
  printWin()
elif player == player_com:
  print("Draw")
else:
  print("You Loose")
  
