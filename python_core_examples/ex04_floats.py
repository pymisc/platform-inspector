# This is the place for float data types and related examples.
"""
STEP 4 — Floats

Floats are numbers that contain decimal values.

Platform engineering examples:
- CPU usage
- Memory usage
- Disk utilization
- Load average
- Network latency
- Network bandwidth
- Temperature
- Uptime

Run:
    python ex04_floats.py
"""

#----------------------------
# Example 1: basic float
#----------------------------
cpu_usage = 37.5
print("CPU usage:", cpu_usage)

#----------------------------
# Example 2: checking data type
#----------------------------
memory_usage = 68.2
print("Memory usage:", memory_usage)
print("Memory usage data type is:", type(memory_usage))

#----------------------------
# Example 3: Memory size in GB
#----------------------------
total_memory_gb = 32.0
used_memory_gb = 21.5

print("Total memory:", total_memory_gb, "GB")
print("Used memory:", used_memory_gb, "GB")

#----------------------------
# Example 4: Calculating available memory
#----------------------------
available_memory_gb = total_memory_gb - used_memory_gb
print("Available memory:", available_memory_gb, "GB")

#----------------------------
# Example 5: Disk utilization percentage
#----------------------------
disk_usage_pecentage = 73.8
print("Disk usage:", disk_usage_pecentage, "%")

#----------------------------
# Example 6: Calculating memory usage percentage
#----------------------------
memory_usage_percent = (used_memory_gb / total_memory_gb) * 100
print("Memory usage percentage:", memory_usage_percent, "%")

#----------------------------
# Example 7: formatting memory percentage to two decimal points
#----------------------------
print(f"Memory usage: {memory_usage_percent:.2f}%")


#----------------------------
# Example 8: Important - FLOAT PRECISION EXAMPLE
#----------------------------

result = 0.1 + 0.2

print(result)
print(result == 0.3)

# Above example (which shows False) introduces an important real-world idea: 
# that floating-point numbers are approximations internally.

