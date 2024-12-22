import subprocess

result = subprocess.run(["fping", "-a", "-g", "192.168.1.0/24"], capture_output=True, text=True)

address_list = result.stdout.splitlines()
print(address_list)
