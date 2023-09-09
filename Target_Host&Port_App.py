import socket

def scan_port(target_host, target_port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for the connection attempt (adjust as needed)
        sock.settimeout(1)

        # Attempt to connect to the target host and port
        sock.connect((target_host, target_port))

        # If the connection succeeds, the port is open
        print(f"Port {target_port} on {target_host} is open")

        # Close the socket
        sock.close()

    except socket.error:
        # If there is an error (e.g., connection refused), the port is closed
        print(f"Port {target_port} on {target_host} is closed")

if __name__ == "__main__":
    target_host = input("Enter the target host (IP address or domain): ")
    target_port = int(input("Enter the target port to scan: "))

    scan_port(target_host, target_port)
