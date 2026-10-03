# packet-sniffer
A Python network packet sniffer built with Scapy to analyze real-time network traffic
# 📡 Network Packet Sniffer

A real-time network packet sniffer built with Python and Scapy that captures and analyzes live network traffic.

## Features
- Captures live network packets in real-time
- Identifies TCP, UDP, and ICMP protocols
- Displays source and destination IPs
- Shows port numbers for each connection
- Detects DNS queries, HTTPS traffic, and ping packets

## Usage
```bash
python packet_sniffer.py
```
> Run as Administrator on Windows for full packet capture

## Example Output
[TCP] 192.168.0.107 → 84.32.102.196 | Port 52526 → 443
[UDP] 192.168.0.107 → 192.168.0.1 | Port 55174 → 53
[ICMP] 192.168.0.107 → 84.32.61.171 | Ping packet


## Technologies
- Python
- Scapy
- Network Traffic Analysis
- Protocol Analysis (TCP/UDP/ICMP)
