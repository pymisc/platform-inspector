import os
import psutil

import sys
# print(sys.stdlib_module_names)
# print(str(sys.stdlib_module_names))
print("\n\nTesting boolean results:")
print("os:", "os" in sys.stdlib_module_names)
print("subprocess:", "subprocess" in sys.stdlib_module_names)
print("psutil:", "psutil" in sys.stdlib_module_names)



cpu_count=os.cpu_count()
print(cpu_count)

cpu_count1=psutil.cpu_count()
print(cpu_count1)

total_memory=(psutil.virtual_memory().total)/(1024*1024*1024)
print(f"Total memory: {total_memory:.1f} GB")
print(type(total_memory))

available_memory=(psutil.virtual_memory().available)/(1024*1024*1024)
print(f"Available memory: {available_memory:.1f} GB")

print(f"Percent memory utilization: {psutil.virtual_memory().percent}%")


# Alternate ways to check size (other integer operations)
total_memory_alt1=(psutil.virtual_memory().total/(1024**3))
print("Total memory (exponent method of calculation):", total_memory_alt1)

total_memory_alt2=(psutil.virtual_memory().total//(1024**3))
print("Total memory (floor method of calculation):", total_memory_alt2)


