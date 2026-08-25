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


# 11 - playing with special charaters
# repr() / !r — display the developer-friendly representation of a value,
# making hidden characters such as \n, \t, and spaces easier to identify.
# For Platform Engineering work, this is especially handy when debugging 
# environment variables, parsed files, API responses, command output, 
# whitespace, tabs, and newline characters.
value=" testing \n"
print(value)
print(repr(value))
print(f"{value!r}")


# 12 - quick variable debugging with = in an f-string
pod_count = 8
failed_pod = 2
print(f"{pod_count=}")
print(f"{failed_pod=}")


# 13 - Formatting numbers for cpu, memory, latency etc.
cpu_usage = 30.2234
memory_bytes = 1048000
print(f"CPU usage: {cpu_usage:.2f}%")
print(f"Memory usage: {memory_bytes:,} bytes")


# 14 - Print with alignment - like a well formatted report
# <20 = left-align in a minimum 20-character field.
# Shorter text is space-padded; longer text is NOT truncated.
print(f"{'RESOURCE':<20}{'STATUS':<10}")
print(f"{'kubernetes':<20}{'HEALTHY':<10}")
print(f"{'DR site':<20}{'NOT HEALTHY ajdj':<10}")
print(f"{'COLO Site':<20}{'HEALTHY':<10}")

# 15 - Printing to stderr - very valuable while writing apps & scripts
import sys
print("Platform Inspector started")  # supposed to go to stdout
print("ERROR: Kubernetes API unavailable", file=sys.stderr)  # supposed to go to stderr
