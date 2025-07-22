# File : port_scanner_py
# Panayiotis Koutos
# IPv4 scanner for ICTPRG435 asst2 

import socket
import logging
import sys

# Validate IP format
def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# Validate port number range
def validate_port(port):
    return 1 <= port <= 65535

# Scan the port using a socket connection
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception as e:
        logging.error(f"Error scanning port {port}: {e}")
        return False 

# Main function to run the scanner
def main():
    # Configure Logging
    logging.basicConfig(
        filename="scan.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Getting Target IP
    while True:
        ip = input("Enter target IPv4 address: ")
        if validate_ip(ip):
            break
        else:
            print("Invalid IP address. Please try again.")

    # Getting Port Range
    while True:
        try:
            start_port = int(input("Start Port (1-65535): "))
            end_port = int(input("End Port (1-65535): "))
            if validate_port(start_port) and validate_port(end_port) and start_port <= end_port:
                break
            print("Invalid port range. Please Try Again.")
        except ValueError:
            print("Numbers Only!")

    # Scanning Ports
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            print(f"Port {port} - OPEN")
            open_ports.append(port)
            logging.info(f"Port {port} - OPEN")
        else:
            print(f"Port {port} : CLOSED")

    # Summary
    print(f"\nScan complete! Open Ports: {open_ports}")
    logging.info(f"Scan Finished! Open Ports: {open_ports}")

# Entry Point
if __name__ == "__main__":
    main()
