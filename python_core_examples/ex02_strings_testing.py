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

