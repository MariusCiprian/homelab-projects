import subprocess

#hostname = input("Write the hostname:  ")
#current_user = input("Write the current user:  ")
print()
print()
print("=" * 35)
print(" Linux System Information")
print("=" * 35)
print()
print()

hostname= subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True,
    );
current_user= subprocess.run(
    ["whoami"],
    capture_output=True,
    text=True,
);

os_version= subprocess.run(
     ["cat", "/etc/os-release"],
     capture_output=True,
     text=True,

);

# lines= os_version.stdout.splitlines()
# #print(lines);
# for line in lines :
#     if line.startswith("PRETTY_NAME"):
#         print(line);

text = 'PRETTY_NAME="Ubuntu 25.10"'

parts = text.split("=");
print(parts[1]);

#os_version = os.VERSION_ID;
#print(os.split)
#print(os_version);
# hostname = result.stdout;
# print(hostname)
# print(result)
# print(result.stdout)
# #print("Hostname            : " + hostname)
# #print("Current User        : " + current_user)
# print("Hostname:" + hostname.stdout)
# print("Current user:" + current_user.stdout);
# print("OS Version:" + os_version);
