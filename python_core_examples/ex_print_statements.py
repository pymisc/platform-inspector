print("10 ways to use a print statement")

# 1 - Simplest hello
print("Hello")

# 2 - Printing blank line
print()

# 3 - Printing a variable with some fixed text
varSpeed=75
print("Top speed allowed for a bus is ", varSpeed, " MPH")

# 4 - f-Strings (modern variable interpolation)(from python 3.6 and up)
name = "pymisc"
age = 30
print(f"User {name} is {age} years old")
print(f"{name} will be {age+1} years old next year!")
print("User {name} is {age} years old") # Why f is needed. :D

# 5 - Custom separator (sep)
print("2026", "08", "17", sep="-")
varSeparator="\n"
print("2026", "08", "17", sep=varSeparator)

# 6 - Custom end character (end)
print("first line", end="...")
print("second line!")

# 7 - multi-line printing
print("""
This is line 1
second line
line3
""")

print(f"""
This is line 1
second line
This is a test line {age+1} with text interpolation
line3
""")

# 8 - The .format() method - old method, pre f-strings
item="Masala chai"
price=3.50
count=2
print("The cost of {}  {} is ${:.2f} USD".format(count, item, price*count))

# 9 - String concatenation
user="pymisc"
messages=5
print("Hello " + user + ", you have " + str(messages) + " unread messages!")


# 10 - Print / write into a file (append in this case, create if absent)
with open("a.txt", "+a") as myfile:
  print("test", file=myfile)

