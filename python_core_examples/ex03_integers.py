import os
import psutil

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

# Some other arithmetic with integers:
double_cpu_count = cpu_count * 2
half_cpu_count = cpu_count / 2
floor_half_cpu_count = cpu_count // 2
remainder_cpu = cpu_count % 2

print("Double CPU:", double_cpu_count)
print("Half CPUs:", half_cpu_count)
print("Floor half CPUs:", floor_half_cpu_count)
print("Remainder when divided by 2:", remainder_cpu)

# One basic minus example
desired_replicas = 10
actual_replicas = 9
missing_replicas = desired_replicas - actual_replicas
print("Missing replicas count (if any):", missing_replicas)

### just some more examples :D
restart_count = "12"
print(type(restart_count))

restart_count = int(restart_count)
print(type(restart_count))
print(restart_count + 1)


print("**** Different way to represent: ****")
memory_bytes = psutil.virtual_memory().total

print("Memory in bytes:", memory_bytes)
print("Type:", type(memory_bytes))

memory_gib = memory_bytes // (1024 ** 3)

print("Memory in whole GiB:", memory_gib)
print("Type:", type(memory_gib))

print("Using / :", memory_bytes / (1024 ** 3))
print("Using //:", memory_bytes // (1024 ** 3))

print(type(memory_bytes / (1024 ** 3)))
print(type(memory_bytes // (1024 ** 3)))