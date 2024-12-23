import subprocess

result_fping = subprocess.run(["fping", "-a", "-g", "192.168.1.0/24"], capture_output=True, text=True)

address_list = result.stdout.splitlines()

for index, item in enumerate(address_list, start=1):
	print(f"{index}. {item}")

result_nmap = subprocess.run(['nmap', '-sn', '192.168.1.0/24'], capture_output=True, text=True)

lines = result.stdout.split('\n')

nmap_reports = [line for line in lines if 'Nmap scan report for' in line]

device_name = [line.split()[4] for line in nmap_reports]

