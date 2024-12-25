import socket
import subprocess

# IP adreslerini tarama
result_fping = subprocess.run(
    ["fping", "-a", "-g", "192.168.1.0/24"], 
    capture_output=True, 
    text=True
)

# Tarama sonuçlarını listeye çevirme
address_list = result_fping.stdout.splitlines()

# Hostname alma fonksiyonu
def get_device_name(ip_address):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror:
        return "Hostname not found"

# Cihazları saklamak için boş bir dictionary
devices = dict()

# IP adreslerini ve cihaz adlarını ekleme
for ip in address_list: 
    hostname = get_device_name(ip)
    devices[ip] = hostname  # Hostname veya hata mesajını ekle

# Sonuçları yazdırma
for ip, name in devices.items():
    print(f"{ip} - {name}")
