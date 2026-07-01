import subprocess

print("=" * 35)
print(" Linux System Information")
print("=" * 35)
print()

# Hostname
hostname = subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True,
)

# Current User
current_user = subprocess.run(
    ["whoami"],
    capture_output=True,
    text=True,
)

# Operating System
os = subprocess.run(
    ["cat", "/etc/os-release"],
    capture_output=True,
    text=True,
)

os_version = ""

lines = os.stdout.splitlines()

for line in lines:
    if line.startswith("PRETTY_NAME"):
        parts = line.split("=")
        os_version = parts[1].strip('"')
        break

print("Hostname      :", hostname.stdout.strip())
print("Current User  :", current_user.stdout.strip())
print("OS Version    :", os_version)