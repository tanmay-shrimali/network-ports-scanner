![screenshot](https://github.com/tanmay-shrimali/network-ports-scanner/assets/119653072/4b326087-7733-4154-9844-0025ed869af7)

# Network Port Scanner

A Python script that allows you to scan ports on a target host or IP address. This port scanner is created by Tanmay Shrimali, a cyber security engineer. It is designed to help identify open ports on a network and provide additional functionalities such as service identification, banner grabbing, OS fingerprinting, and vulnerability scanning.

## Introduction

A port scanner is a software tool that is used to analyze and scan the open ports on a network or a specific host. It helps in determining which ports are open, closed, or filtered on a target system. Port scanning is an essential technique in the field of cybersecurity, as it allows system administrators and security professionals to assess the security posture of their network and identify potential vulnerabilities.

## Advantages

- **Network Security**: Port scanning helps identify open ports that may indicate potential security vulnerabilities, such as improperly configured or unpatched services.
- **System Hardening**: By identifying open ports, system administrators can close unnecessary or unused ports, reducing the attack surface and enhancing system security.
- **Penetration Testing**: Port scanning is a crucial component of penetration testing, allowing ethical hackers to evaluate the security of a system and identify potential entry points for exploitation.

## Python Efficiency

The port scanning script is implemented in Python, a versatile and efficient programming language. Python offers several advantages for this task, including:

- **Ease of Use**: Python provides a simple and readable syntax, making it accessible to both beginner and experienced programmers.
- **Networking Libraries**: Python offers powerful networking libraries, such as `socket`, which enable efficient communication over TCP/IP protocols.
- **Multi-threading**: The script utilizes multi-threading to perform concurrent port scans, maximizing efficiency and reducing scan times.
- **Extensibility**: Python's extensive ecosystem of libraries and modules allows for easy integration of additional functionalities and customization.

## Legal and Educational Purposes

Please note that the network port scanner script is intended for **educational purposes only**. It is crucial to use this tool responsibly and with proper authorization. Before conducting any port scanning activities, ensure that you have obtained the necessary permissions from the network owner or system administrator. Unauthorized port scanning may be considered illegal and can result in severe consequences.

**Use this tool at your own risk. The author and contributors are not responsible for any misuse or damage caused by the script.**

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Clone this repository or download the `network_port_scanner.py` file.

## Usage

To use the script, open a terminal or command prompt and navigate to the directory where the `network_port_scanner.py` file is located.


Run the script using the following command:

python network_port_scanner.py host ports [-t TYPE] [-r RANGE] [-c] [-s] [-b] [-o] [-v]


Example usage Command:

python network_port_scanner.py example.com 80,443 -t tcp -s -b


- `host`: The target host or IP address to scan.
- `ports`: The target ports to scan, separated by commas. Example: `80,443,22`.
- `-t TYPE` or `--type TYPE`: Optional. Specify the scan type as either `tcp` or `udp` (default is `tcp`).
- `-r RANGE` or `--range RANGE`: Optional. Specify a port range to scan. Example: `1000-2000`.
- `-c` or `--common`: Optional. Scan common ports (80, 443, 21).
- `-s` or `--service`: Optional. Perform service identification.
- `-b` or `--banner`: Optional. Perform banner grabbing.
- `-o` or `--os`: Optional. Perform OS fingerprinting.
- `-v` or `--vulnerability`: Optional. Perform vulnerability scanning.



## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.
