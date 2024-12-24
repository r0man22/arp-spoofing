import socket

def get_device_name(ip_address):
	try:
		
		hostname, _, _ = socket.gethostbyaddr(ip_address)
		return hostname
	except socket.herror:
		return "Hostname not found"

ip_address = "192.168.1.26"
device_name = get_device_name(ip_address)
print(f"Device name: {device_name}")

