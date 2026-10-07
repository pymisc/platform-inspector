# Strings formatting
hostname = "platform-node-01"
cpu_usage = 32.643
memory_usage = 71.233
disk_usage = 43.443
docker_installed = True
cluster_reachable = False

print()
print("="*42)
# Note: The carrot below ^ makes alignment to center
print(f"{'PLATFORM INSPECTOR':^42}")
print("="*42)

print(f"{'Hostname':<22}: {hostname}")
print(f"{'CPU Usage':<22}: {cpu_usage:.2f}%")
print(f"{'Memory Usage':<22}: {memory_usage:.2f}%")
print(f"{'Disk Usage':<22}: {disk_usage:.2f}%")
print(f"{'Docker Installed':<22}: {docker_installed}")
print(f"{'Cluster Reachable':<22}: {cluster_reachable}")

print("="*42)

print(f"{'Overall status':<22}: { 'ONLINE' if cluster_reachable else 'OFFLINE'}")

print("="*42)
