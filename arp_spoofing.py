import socket
import subprocess

result_fping = subprocess.run(
    ["fping", "-a", "-g", "192.168.1.0/24"], 
    capture_output=True, 
    text=True
)

address_list = result_fping.stdout.splitlines()

if not address_list:
    print("No IP addresses found by fping.")

def get_device_name(ip_address):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname.replace(".bbrouter", "")
    except socket.herror:
        return "Hostname not found"

devices = dict()

for ip in address_list: 
    hostname = get_device_name(ip)
    devices[ip] = hostname  

if not devices:
    print("No devices were resolved.")
else:
    for index, (ip, name) in enumerate(devices.items(), start=1):
        print(f"{index}. {ip} - {name}")

print("\n")

choice = input("Enter the number of the device you want to arp spoofing -> ")

