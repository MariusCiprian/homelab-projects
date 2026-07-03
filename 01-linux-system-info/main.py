import subprocess

print("=" * 35)
print(" Linux System Information")
print("=" * 35)
print()

# Hostname
def get_hostname():
      hostname = subprocess.run(
      ["hostname"],
      capture_output=True,
      text=True,
)
      return hostname.stdout.strip()


# Current User
def get_current_user():
    current_user = subprocess.run(
    ["whoami"],
    capture_output=True,
    text=True,
)     
    return current_user.stdout.strip()


# Operating System

def get_os_version():
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
        return os_version;

hostname = get_hostname();
current_user = get_current_user();
os_version = get_os_version();

# # print("Hostname      :", hostname.stdout.strip())
# # print("Current User  :", current_user.stdout.strip())
# # print("OS Version    :", os_version)
print("Hostname     :", hostname )
print("Current User    :",  current_user )
print("OS Version    :", os_version );


def run_command(command):
    print(command);
    
run_command(['hostname']);
run_command(['whoami']);