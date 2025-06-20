import random

bikes_list= ["tvs jupiter", "re hunter", "re himalayan", "Yamaha Tenere"]

print(bikes_list[0])

bikes_list.append("honda nx500")

print(bikes_list)

# who pay the bill
names = ["Aarav", "Meera", "Rohan", "Kavya", "Vihaan"]
print(len(names))
print("who will pay the bill ?")
print(f"{names[random.randint(0,len(names))]}")
print(random.choice(names))