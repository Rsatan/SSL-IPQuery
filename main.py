import sys
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
   ____    ____    __             ______  ____    _____                                      
  /\  _`\ /\  _`\ /\ \           /\__  _\/\  _`\ /\  __`\                                    
  \ \,\L\_\ \,\L\_\ \ \          \/_/\ \/\ \ \L\ \ \ \/\ \  __  __     __   _ __   __  __    
   \/_\__ \\/_\__ \\ \ \  __  ______\ \ \ \ \ ,__/\ \ \ \ \/\ \/\ \  /'__`\/\`'__\/\ \/\ \   
     /\ \L\ \/\ \L\ \ \ \L\ \/\______\_\ \_\ \ \/  \ \ \\'\\ \ \_\ \/\  __/\ \ \/ \ \ \_\ \  
     \ `\____\ `\____\ \____/\/______/\_____\ \_\   \ \___\_\ \____/\ \____\\ \_\  \/`____ \ 
      \/_____/\/_____/\/___/         \/_____/\/_/    \/__//_/\/___/  \/____/ \/_/   `/___/> \
                                                                                       /\___/
                                                                                       \/__/                                                                                                                                                                                                                                                                                                                    
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
        ips = set(text for text in [a.text for a in soup.select('.hsxa-meta-data-list-main-left a')] if re.match(r'^\d+\.\d+\.\d+\.\d+$', text))

        return {"serial": serial, "ips": list(ips)}
    except Exception as e:
        raise e

if __name__ == "__main__":
    import argparse
    print_logo()
    try:
        # 解析命令行参数
        parser = argparse.ArgumentParser(description="Get IPs from SSL certificate serial number")
        parser.add_argument("domain", type=str, nargs="?", help="domain to query")
        parser.add_argument("--port", "-p", type=int, default=443, help="Port number (Default: 443)")
        parser.add_argument("--timeout", "-t", type=int, default=10000, help="Timeout milliseconds (Default: 10000)")
        args = parser.parse_args()

        if args.domain:
            result = get_cert_ips(args.domain, args.port, args.timeout)
            print_colored("\nDomain:")
            print(f"- {args.domain}")
            print_colored("\nCert Serial:")
            print(f"- {result['serial']}")
            print_colored("\nIPs:")
            for ip in result['ips']:
                print(f"- {ip}")
    except SystemExit:
        pass
    except Exception as e:
        print(f"Error: {e}")
