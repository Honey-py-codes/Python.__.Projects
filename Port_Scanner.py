# importing the important module
import socket

# procedure to start scanning
def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    try:
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

# ---- Inputs from user ----
host = input("Enter host (ip or website): ").strip()
start = int(input("Start port: ").strip())
end = int(input("End port: ").strip())

print(f"\nScanning {host} from port {start} to {end}...\n")

for port in range(start, end + 1):
    if scan_port(host, port):
        print(f"[OPEN]  {port}")

