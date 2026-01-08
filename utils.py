def parse_ports(port_input):
    ports = set()

    try:
        if "," in port_input:
            for p in port_input.split(","):
                p = int(p)
                if 1 <= p <= 65535:
                    ports.add(p)

        elif "-" in port_input:
            start, end = port_input.split("-")
            start, end = int(start), int(end)

            if start > end:
                raise ValueError

            for p in range(start, end + 1):
                if 1 <= p <= 65535:
                    ports.add(p)

        else:
            p = int(port_input)
            if 1 <= p <= 65535:
                ports.add(p)

    except ValueError :
        raise ValueError(
                       "Invalid port format. Use examples: 80 | 1-1000 | 22,80,443"
                       )

    if not ports:
        raise ValueError("No valid ports found in input.")

    return sorted(ports)
