# Core platform variables
hostname = "app-server-01"
os_name = "Linux"
env_name = "Production"

# 01: Basic assignment
platform = "Ubuntu 22.04"
architecture = 'x86_64'

# 02: f-strings (modern formatting)
summary=f"Host: {hostname} | OS: {os_name} | Env: {env_name}"
print(summary)

# 03: String concatenation (+)
uptime = 45 # in days
status = hostname + " has been running for " + str(uptime) + " days"
print(status)

# 04: Multiple-line Strings ("""")
report=f"""
=========================================
    PLATFORM INSPECTOR v0.1.0
=========================================
Hostname: {hostname}
OS: {os_name}
Environment: {env_name}
"""
print(report)


# 05: The .format method
log_message = "[{}] The system {} is running on {}".format(env_name, hostname, os_name )
print(log_message)

# 06: String repetition
separator="-"*40
print(separator)

# 07: String slicing ([start:stop])
server_id=hostname[-2:]
print(server_id)

# 08: Checking sub-strings (in)
if "app" in hostname:
    print("This is an application server")

# 09: Finding substring positions (.find())
hyphen_index=hostname.find("-")
print(f"The first position of hyphen is {hyphen_index}")

# 09.a Finding ALL occurances of a substring positions (using .find())
text = "part1-part2-part3-part4"
positions=[] # initializing a list to hold positions
# finding first occurance 
text_to_find="ar"
index=text.find(text_to_find)
print(index)
while index != -1:
    positions.append(index)
    index = text.find(text_to_find, index+1)
print(positions)
print(type(positions))


# 10. Replacing text
new_text=os_name.replace("Linux", "Windows")
print(f"new OS is: {new_text}")

# 11. Upper and lower case conversion
print(f"Original value of OS:{os_name}")
print(f"Upper case of OS: {os_name.upper()}")
print(f"this is lower case example: {os_name.lower()}")
print("Upper case of OS: ", format(os_name.upper()), " This is supposed to be in UPPER case")


# 12. Splitting strings (.split())
host_parts = hostname.split("-")
print(type(host_parts))
print(host_parts)

# 13. Joining strings
tags = ["web", "frontend", "backend"]
tag_string = ",".join(tags)
print(type(tag_string))
print(tag_string)

# 14. Stripping Whitespaces (.strip())
test_txt = "   this is a sample text   "
print(test_txt)
print(test_txt.strip())

# 15. Checking prefix and suffix with .startswith() and .endswith()
if hostname.startswith("app"):
    print("This is an application server")
elif hostname.endswith("01"):
    print("This is the primary node")

# 16. Checking strings for alphabets, numbers and alphanumeric)
port_number = "abc"
if port_number.isalnum():
    print("The given text is alpha-numeric")

if port_number.isnumeric():
    print("The given text is a number")

if port_number.isalpha():
    print("The given text is alphbets")

# 17. Padding strings (.ljust, .rjust, .center)
print(os_name.center(20), "  test  ", env_name.center(20), sep="|")

# 18. Raw strings
windows_path1 = "C:\System32\new\table\hosts"
windows_path2 = r"C:\System32\new\table\hosts"
print(windows_path1)
print(windows_path2)

# 19. Capitalization & title casing (.capitalize() , .title() )
raw_text = "staging area"
print("Original text:", raw_text)
print("Capitalize example: ", raw_text.capitalize())
print("Title example: ", raw_text.title())

# 20. zero-padding (.zfill())
node="11"
print("Original text:", node)
print("Zero padding / ZFILL example:", node.zfill(10))
