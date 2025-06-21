fruits = [
    "Apple",
    "Banana",
    "Mango",
    "Orange",
    "Pineapple",
    "Grapes",
    "Strawberry",
    "Watermelon",
    "Papaya",
    "Guava",
    "Blueberry",
    "Cherry",
    "Kiwi",
    "Litchi",
    "Pomegranate"
]


for fruit in fruits:
  print(fruit)
  
numbers = [163, 220, 33, 432, 500, 733, 773,399,223,424,340,444]

max_num = 0

for num in numbers:
  if max_num < num:
    max_num = num

print(f"max number is {max_num}")
 
print(sum(numbers))
print(max(numbers))