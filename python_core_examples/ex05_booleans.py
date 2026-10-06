"""
STEP 5 — Booleans

Booleans represent two possible states:

    True
    False

Platform engineering examples:
- Docker installed or not
- Host reachable or not
- Configuration file exists or not
- CPU usage healthy or unhealthy
- Window
"""

import os
import platform
import shutil
import socket


# ---------------------------------------------------------
# Example 1: Basic boolean values
# ---------------------------------------------------------

docker_installed = True
cluster_reachable = False

print("Docker installed:", docker_installed)
print("Cluster reachable:", cluster_reachable)

# ---------------------------------------------------------
# Example 2: Checking boolean data type
# ---------------------------------------------------------

healthy = True

print("Healthy:", healthy)
print("Type:", type(healthy))

#-----------------------------------------------------------
# Example 3: Comparing return booleans
#-----------------------------------------------------------
cpu_usage = 42.5
print("Whether CPU Usage is below 80%:", cpu_usage < 80)
print("Whether CPU Usage is above 90%:", cpu_usage > 90)

#------------------------------------------------------------
# Example 4: Equality comparison
#------------------------------------------------------------
expected_port = 443
actual_port = 443
port_match = ( expected_port == actual_port )
print("Result whether actual port and expected port matches:", port_match)


# ---------------------------------------------------------
# Example 5: Not equal comparison
# ---------------------------------------------------------
current_version = "1.34"
required_version = "1.33"

version_different = current_version != required_version

print("Version is different:", version_different)

#-----------------------------------------------------------
# Example 6: detecting OS - whether its Windows or Linux
#-----------------------------------------------------------
is_windows = (platform.system() == "Windows")
print("This is Windows system:", is_windows)

# ---------------------------------------------------------
# Example 7: Detect Linux
# ---------------------------------------------------------
is_linux = platform.system() == "Linux"
print("Running on Linux:", is_linux)

print(platform.python_branch())
print(platform.processor())
print(platform.node())
print(platform.python_build())


# ---------------------------------------------------------
# Example 8: Check whether Docker command exists
# Works on Windows and Linux
# ---------------------------------------------------------
docker_installed = shutil.which("docker") is not None
print("Docker installed check result:", docker_installed)

print(shutil.which("docker"))


#----------------------------------------------------------
# Example 9: Checking if python is installed
#----------------------------------------------------------

python_found = (
    shutil.which("python") is not None
    or shutil.which("python3") is not None
)
print("Whether Python found on this system:", python_found)


#-----------------------------------------------------------
# Example 10: Checking if a file exists
#-----------------------------------------------------------

config_file_exists = os.path.exists("settings.ini")
print("Settings file exist:", config_file_exists)

# ---------------------------------------------------------
# Example 11: Check whether a directory exists
# ---------------------------------------------------------

logs_directory_exists = os.path.isdir("logs")

print("logs directory exists:", logs_directory_exists)

# ---------------------------------------------------------
# Example 12: Use of AND with booleans
# ---------------------------------------------------------
docker_installed = shutil.which("docker") is not None
config_file_exists = os.path.exists("settings.ini")
platform_ready_check = docker_installed and config_file_exists
print("Platform ready check:", platform_ready_check)

#----------------------------------------------------------
# Example 13: Use of "not" with booleans
#----------------------------------------------------------

maintenance_mode = False
normal_operation = not maintenance_mode
print("Maintenance mode:", maintenance_mode)
print("Normal operation:", normal_operation)

# ---------------------------------------------------------
# Example 15: Check whether a TCP port is reachable
# Works on Windows and Linux
# ---------------------------------------------------------

hostname = "aaravsharma.net"
port = 443

try:
    connection = socket.create_connection(
        (hostname, port),
        timeout=3
    )
    connection.close()

    tcp_port_reachable = True

except OSError:
    tcp_port_reachable = False

print(
    f"TCP connection to {hostname}:{port}:",
    tcp_port_reachable
)