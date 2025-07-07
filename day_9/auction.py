from os import system

# system('cls')

auction_bids = {}

bidders = True

while(bidders):
   name = input("Enter your name : ")
   amount = int(input("Enter your bid : "))
   auction_bids[name] = amount
   system('cls')
   q = (input("Press y to for next bidder or n to finish bidding : ")).lower()
   system('cls')
   if(q == "y"):
      continue
   bidders = False


highest_bid = 0
winner_name = ""

for key in auction_bids:
   if auction_bids[key] > highest_bid:
      highest_bid =  auction_bids[key]
      winner_name = key

print(auction_bids)

print(f"Congraulation {winner_name} you won the bid with amount {highest_bid}")
