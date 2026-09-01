# This file contains most common built-in functions we come across and their practical examples.
#
# Initial scope:
# 1. len()
# 2. type()
# 3. str()
# 4. int()
# 5. float()
# 6. bool()
# 7. input()
# 8. repr()
# 9. isinstance() - check whether an object is a particular type (returns true / false)

name = input("Enter your name:")
print("Hello ", name, "! How are you doing today?")
print("Hello ", name.strip(), "! How are you doing today?", sep="") # desired output without extra space

print("Your name is ", len(name), "characters long! (Without stripping)")
print("Raw length:", len(name))
print("Cleaned length:", len(name.strip()))


name_v1="name" + "\n" + "hello"
print(repr(name_v1))

print("The type of data you entered is a: ", type(name))

# Lets see how it shows a list for type
list1=['red', 'blue', 'green', 'white']
print("The data type of \"list1\" is:", type(list1), "\nand its value is:", list1)


# Playing with string -> int -> float

data1 = "8080"

print("Datatype:", type(data1), "Value:", data1)
print("Is digit:", data1.isdigit())

data1 = int(data1)
print("Datatype:", type(data1), "Value:", data1)

data1 = float(data1)
print("Datatype:", type(data1), "Value:", data1)
if isinstance(data1, float):
    print("data1 is a float")


# Playing with bool()
data1 = "hello"
data2 = ""
data3 = 100
data4 = 0

print("bool('hello'):", bool(data1))
print("bool(''):", bool(data2))
print("bool(100):", bool(data3))
print("bool(0):", bool(data4))

print("some more one liners")
print(bool("hello"))  # true
print(bool(""))       # false - because of empty string
print(bool(" "))      # true - because of non-empty string
print(bool("0"))      # true - because of "0" as a string
print(bool(0))        # false - because of 0 as number
print(bool(1))        # true
print(bool(-1))       # true

print("Here comes little more sophisticated example..")
user_input = "   "
print(bool(user_input))           # true - because user_input is still a non-empty string
print(bool(user_input.strip()))   # false - because strip method remove all spaces! :D
