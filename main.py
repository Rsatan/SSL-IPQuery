import re
import random
import socket
import ssl
import base64
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def print_colored(text):
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
    reset_color = "\033[0m"
    selected_color = random.choice(colors)
    print(selected_color + text + reset_color)

def print_logo():
    logo = r'''
       __________ __         ________  ____                       
      / ___/ ___// /        /  _/ __ \/ __ \__  _____  _______  __
      \__ \\__ \/ /  ______ / // /_/ / / / / / / / _ \/ ___/ / / /
     ___/ /__/ / /__/_____// // ____/ /_/ / /_/ /  __/ /  / /_/ / 
    /____/____/_____/    /___/_/    \___\_\__,_/\___/_/   \__, /  
                                                         /____/                                                                                                                                                                                                                                                                                                                    
    '''
    author = "Author: Rsa7an"
    
    print_colored(logo)
    print_colored(author)

def get_host_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except Exception as e:
        raise e

def get_cert_ips(domain, port=443, timeout=10000):
    try:
        ip = get_host_ip(domain)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        with ssl.create_connection((ip, port), timeout=timeout) as sock:
            with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                der_cert = ssock.getpeercert(binary_form=True)
                cert = x509.load_der_x509_certificate(der_cert, default_backend())
                serial = cert.serial_number

        response = requests.get("https://fofa.info/result", params={"qbase64": base64.b64encode(f"cert='{serial}'".encode()).decode()})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        ips = set([a.text.strip() for a in soup.select('.hsxa-meta-data-list-main-left a') if re.match(r"^\d+\.\d+\.\d+\.\d+$", a.text.strip())])
        return {"serial": serial, "ips": list(ips)}
    except Exception as e:
        raise e
    
def get_cert_ips_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        print(f"\nFound {len(lines)} domains")
        results = []
        for line in lines:
            parts = line.strip().split(":")
            domain = parts[0]
            port = int(parts[1]) if len(parts) > 1 else 443
            result = get_cert_ips(domain, port)
            results.append({"domain": domain, "serial": result['serial'], "ips": result['ips']})
        
        return results
    except Exception as e:
        raise e

def save_results_to_file(results, output_file):
    try:
        with open(output_file, "w") as file:
            for result in results:
                file.write("\nDomain:\n")
                file.write(f"- {result['domain']}\n")
                file.write("\nCert Serial:\n")
                file.write(f"- {result['serial']}\n")
                file.write("\nIPs:\n")
                for ip in result['ips']:
                    file.write(f"- {ip}\n")
    except Exception as e:
        raise e

if __name__ == "__main__":
    import argparse
    print_logo()
    try:
        parser = argparse.ArgumentParser(description="Get IPs from SSL certificate serial number")
        parser.add_argument("domain", type=str, nargs="?", help="domain to query")
        parser.add_argument("--port", "-p", type=int, default=443, help="Port number (Default: 443)")
        parser.add_argument("--timeout", "-t", type=int, default=10000, help="Timeout milliseconds (Default: 10000)")
        parser.add_argument("--file", "-f", type=str, help="Path to file containing domains and ports")
        parser.add_argument("--output", "-o", type=str, help="Path to output file")
        args = parser.parse_args()

        if args.file:
            results = get_cert_ips_from_file(args.file)
            if args.output:
                save_results_to_file(results, args.output)
            else:
                for result in results:
                    print_colored("\nDomain:")
                    print(f"- {result['domain']}")
                    print_colored("\nCert Serial:")
                    print(f"- {result['serial']}")
                    print_colored("\nIPs:")
                    for ip in result['ips']:
                        print(f"- {ip}")
        elif args.domain:
            result = get_cert_ips(args.domain, args.port, args.timeout)
            if args.output:
                save_results_to_file([result], args.output)
            else:
                print_colored("\nDomain:")
                print(f"- {args.domain}")
                print_colored("\nCert Serial:")
                print(f"- {result['serial']}")
                print(f"\nFound {len(result['ips'])} IPs")
                if len(result['ips']) > 0:
                    print_colored("IPs:")
                    for ip in result['ips']:
                        print(f"- {ip}")
    except SystemExit:
        pass
    except Exception as e:
        print(f"Error: {e}")


