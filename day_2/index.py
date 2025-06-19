#sub string
print("hello"[4])  #o
print("hello"[-1]) #o

#type error

print(type("dcs"))    # <class 'str'>
print(type(123))
print(type(453.2))
print(type(True))
print(type(False))

# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'bool'>


#--- type casting --#
# print("hello" + 123)  #TypeError: can only concatenate str (not "int") to str

# An f-string (formatted string literal) in Python is a way to embed expressions inside string literals, using a concise syntax introduced in Python 3.6.
print(f"hello {123}") # hello 123
      

print("number of letter in your name " + str(len(input("Enter Your Name: "))))

#PEMDAS    #left to right

print(6/3)  #2.0
print(6//3)  #2
print(type(6//3))    
print(type(6/3))

# <class 'int'>
# <class 'float'>

print(3*3+3/3-3)  #7.0
   #9+1.0-3
   # 10.0-3 = 7.0

#bmi calculator  
   
height = 1.65 
weight = 84
bmi = weight / (height ** 2)

print(bmi)  #30.85399449035813
print(int(bmi))  #30   flooring
print(round(bmi)) #31   rounding
print(round(bmi,2))  #30.85