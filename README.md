# ExaRecon 🔍

**ExaRecon** is a lightweight Python-based reconnaissance tool built to enumerate exposed ports and fingerprint running services using banner grabbing techniques.

---

## 🚀 Features

- Scans common and high‑risk ports
- Performs service banner grabbing
- Identifies exposed services (SSH, FTP, HTTP, SMB, DBs, etc.)
- Graceful error handling and timeouts
- Readable, well-documented Python code

---

## 🧠 Why ExaRecon?

During the reconnaissance phase, attackers enumerate open ports and fingerprint services to:

- Identify potential attack vectors  
- Discover weak or legacy services  
- Understand the target’s attack surface  

**ExaRecon replicates this workflow** in a controlled, ethical learning environment.

---

## ⚙️ How It Works (High Level)

1. Establishes TCP connections using Python sockets  
2. Iterates through a list of common and “juicy” ports  
3. Extracts service banners where available  
4. Displays results for further enumeration  

---

## 📸 Screenshots

![Tool Running](images/Scan.png)

## ▶️ Usage

```bash
 python ExaRecon.py
 ```
