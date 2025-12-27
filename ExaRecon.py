import socket
from concurrent.futures import ThreadPoolExecutor

def grab_banner(ip, port, service):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        if s.connect_ex((ip, port)) != 0:
            return None

        try:
            banner = s.recv(1024).decode(errors="ignore").strip()
        except:
            banner = "Unknown"

        s.close()
        return f"{port}/tcp\topen\t{service}\t{banner}"

    except:
        return None


def main():
    target_ip = "IP_here"  # Replace with the target IP address

    ports = {
        21: "ftp",
        22: "ssh",
        23: "telnet",
        25: "smtp",
        53: "dns",
        80: "http",
        81: "http-alt",
        110: "pop3",
        139: "netbios",
        143: "imap",
        389: "ldap",
        445: "smb",
        636: "ldaps",
        2049: "nfs",
        3306: "mysql",
        3389: "rdp",
        5432: "postgres",
        5900: "vnc",
        6379: "redis",
        8080: "http-alt",
        8443: "https-alt",
        9200: "elasticsearch",
        27017: "mongodb"
    }

    print(f"\nExaRecon scan report for {target_ip}")
    print("PORT\tSTATE\tSERVICE\tVERSION")

    with ThreadPoolExecutor(max_workers=50) as executor:
        tasks = [
            executor.submit(grab_banner, target_ip, port,    service)
            for port, service in ports.items()
        ]

        for task in tasks:
            result = task.result()
            if result:
                print(result)


if __name__ == "__main__":
    main()
