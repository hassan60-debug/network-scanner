from scapy.all import sniff, IP, TCP, UDP, ICMP
import datetime

print("="*55)
print("  Network Packet Sniffer")
print(f"  Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("="*55 + "\n")

def analyze_packet(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        proto = ""
        info = ""

        if TCP in packet:
            proto = "TCP"
            info = f"Port {packet[TCP].sport} → {packet[TCP].dport}"
        elif UDP in packet:
            proto = "UDP"
            info = f"Port {packet[UDP].sport} → {packet[UDP].dport}"
        elif ICMP in packet:
            proto = "ICMP"
            info = "Ping packet"
        else:
            proto = "OTHER"
            info = ""

        print(f"  [{proto}] {src} → {dst}  |  {info}")

print("  Sniffing packets... (Press Ctrl+C to stop)\n")

try:
    sniff(prn=analyze_packet, store=0, count=20)
except KeyboardInterrupt:
    print("\n  Sniffer stopped.")
except Exception as e:
    print(f"\n  Error: {e}")