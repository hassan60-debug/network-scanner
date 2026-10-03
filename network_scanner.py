import nmap
import socket
import datetime
def scan_network(network):
    print(f"\n{'='*55}")
    print(f"  WiFi Network Scanner")
    print(f"  Target : {network}")
    print(f"  Time   : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*55}\n")

    scanner = nmap.PortScanner()
    
    print("  Scanning... please wait\n")
    scanner.scan(hosts=network, arguments='-sn')
    
    devices = scanner.all_hosts()
    
    if not devices:
        print("  No devices found.")
        return
    
    print(f"  {len(devices)} device(s) found on network:\n")
    
    for host in devices:
        hostname = "Unknown"
        try:
            hostname = socket.gethostbyaddr(host)[0]
        except:
            pass
        
        status = scanner[host].state()
        print(f"  {'='*45}")
        print(f"  IP       : {host}")
        print(f"  Hostname : {hostname}")
        print(f"  Status   : {status.upper()}")

    print(f"\n{'='*55}")
    print(f"  Scan complete — {len(devices)} device(s) found")
    print(f"{'='*55}\n")

# Apna network range likho
# 192.168.0.107 tha tera IP — toh range yeh hogi:
target = "192.168.0.0/24"
scan_network(target)