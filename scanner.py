import socket
from concurrent.futures import ThreadPoolExecutor

COMMON_SERVICES = {
                    21: "ftp",
                    22: "ssh",
                    23: "telnet",
                    25: "smtp",
                    53: "dns",
                    80: "http" ,
                    110: "pop3",
                    139: "netbios",
                    143: "imap",
                    389: "ldap" ,
                    445: "smb",
                    3306: "mysql",
                    3389: "rdp",
                    5432: "postgres",
                    6379: "redis",
                    8080: "http-alt",
                    8443: "https-alt"
                 }

def grab_banner(target, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        if sock.connect_ex((target, port)) != 0:
            return None

        try:
            banner = sock.recv(1024).decode(errors="ignore").strip()
            if not banner:
                banner = "Unknown"
        except:
            banner = "Unknown"

        service = COMMON_SERVICES.get(port, "unknown")
        return f"{port}/tcp \topen \t{service} \t{banner}"

    except:
        return None



    finally:

        try:
            sock.close()
        except:
            pass


def scan_target(target, ports, threads, timeout):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        tasks = [
            executor.submit(grab_banner, target, port, timeout)
            for port in ports
        ]

        for task in tasks:
            result = task.result()
            if result:
                print(result)
