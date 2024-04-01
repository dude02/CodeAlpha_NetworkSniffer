from scapy.all import *

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"Source IP: {ip_src}, Destination IP: {ip_dst}")

        if TCP in packet:
            tcp_sport = packet[TCP].sport
            tcp_dport = packet[TCP].dport
            print(f"Source Port: {tcp_sport}, Destination Port: {tcp_dport}")

            raw_data = packet[TCP].payload
            print(f"Raw Data: {raw_data}")

# Sniff packets
sniff(prn=packet_callback, store=0)
