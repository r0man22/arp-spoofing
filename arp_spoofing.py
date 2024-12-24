import subprocess
import re
result_fping = subprocess.run(["fping", "-a", "-g", "192.168.1.0/24"], capture_output=True, text=True)

address_list = result_fping.stdout.splitlines()

for index, item in enumerate(address_list, start=1):
	print(f"{index}. {item}")

result_nmap = subprocess.run(['nmap', '-sn', '192.168.1.0/24'], capture_output=True, text=True)

lines = result_nmap.stdout.split('\n')

nmap_reports = [line for line in lines if 'Nmap scan report for' in line]

mix = [line.split()[4] for line in nmap_reports]
 
filtered_data = [item for item in mix if not re.match(r'^\d{1,3}(\.\d{1,3}){3}$', item)]

print()

for index, item in enumerate(filtered_data, start=1):
	print(f"{index}. {item}")


