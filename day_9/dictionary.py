my_disc = {
  "t": 0,
  "r" :0
}



print(my_disc)
print(my_disc["t"])

my_disc["u"] = 0
my_disc["t"] = 1

print(my_disc)

for thing in my_disc:
  print(my_disc[thing])

my_dict = {
    "fruits": ["apple", "banana", "cherry"],
    "vegetables": ["carrot", "broccoli"]
}


print(my_dict["fruits"][2])


data = {
    "person1": {
        "name": "Alice",
        "hobbies": ["reading", "cycling", "painting"]
    },
    "person2": {
        "name": "Bob",
        "hobbies": ["chess", "gaming"]
    }
}

print(data["person2"]["hobbies"][1])    #gaming