import argparse
from scanner import scan_target
from utils import parse_ports

def main():
    parser = argparse.ArgumentParser(
        description="ExaRecon - Lightweight Network Reconnaissance Tool"
    )

    parser.add_argument(
        "-t", "--target",
        required=True,
        help="Target IP address or hostname"
    )

    parser.add_argument(
        "-p", "--ports",
        default="1-1024",
        help="Port range (e.g. 1-1000 or 80,443,22)"
    )

    parser.add_argument(
        "-T", "--threads",
        type=int,
        default=50,
        help="Number of concurrent threads (default: 50)"
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=1.0,
        help="Socket timeout in seconds (default: 1.0)"
    )

    args = parser.parse_args()

    try:
        ports = parse_ports(args.ports)
    except ValueError as e:
        print(f"[!] Error: {e}")
        return

    print(f"\n[+] ExaRecon Scan Started")
    print(f"[+] Target   : {args.target}")
    print(f"[+] Ports    : {len(ports)} ports")
    print(f"[+] Threads  : {args.threads}")
    print(f"[+] Timeout  : {args.timeout}s\n")

    print("PORT\tSTATE\tSERVICE\tBANNER")

    try:
        scan_target(
            target=args.target,
            ports=ports,
            threads=args.threads,
            timeout=args.timeout
        )
    except KeyboardInterrupt:
        print("\n[!] Scan aborted by user.")



if __name__ == "__main__":
    main()
