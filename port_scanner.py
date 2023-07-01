import argparse
import socket
import threading


def scan_ports(host, ports, scan_type, service_identification, banner_grabbing, os_fingerprinting, vulnerability_scanning):
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            
            if scan_type == "tcp":
                result = sock.connect_ex((host, int(port)))
            elif scan_type == "udp":
                result = sock.sendto(b"Probe", (host, int(port)))
            else:
                print(f"Invalid scan type: {scan_type}")
                return
                
            if result == 0:
                print(f"Port {port}: OPEN")
                if service_identification:
                    # Perform service identification logic
                    pass
                if banner_grabbing:
                    # Perform banner grabbing logic
                    pass
                if os_fingerprinting:
                    # Perform OS fingerprinting logic
                    pass
                if vulnerability_scanning:
                    # Perform vulnerability scanning logic
                    pass
            else:
                print(f"Port {port}: CLOSED")
                
            sock.close()
        except socket.error:
            print(f"Port {port}: ERROR")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Port Scanner")
    parser.add_argument("host", help="Target host/IP address")
    parser.add_argument("ports", help="Target ports (comma-separated)")
    parser.add_argument("-t", "--type", choices=["tcp", "udp"], default="tcp", help="Scan type (TCP/UDP)")
    parser.add_argument("-r", "--range", help="Scan port range (e.g., 1000-2000)")
    parser.add_argument("-c", "--common", action="store_true", help="Scan common ports")
    parser.add_argument("-s", "--service", action="store_true", help="Perform service identification")
    parser.add_argument("-b", "--banner", action="store_true", help="Perform banner grabbing")
    parser.add_argument("-o", "--os", action="store_true", help="Perform OS fingerprinting")
    parser.add_argument("-v", "--vulnerability", action="store_true", help="Perform vulnerability scanning")

    args = parser.parse_args()
    
    if args.range:
        start, end = map(int, args.range.split("-"))
        ports = list(range(start, end + 1))
    elif args.common:
        ports = [80, 443, 21]  # Add more common ports if needed
    else:
        ports = list(map(int, args.ports.split(",")))

    print(f"Scanning {args.host}...\n")
    scan_ports(
        args.host,
        ports,
        args.type,
        args.service,
        args.banner,
        args.os,
        args.vulnerability
    )
    print("\nScan completed!")
    print("\nProject Made By Tanmay Shrinmali A Cyber Security Engineer")    
