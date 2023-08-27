# SSL Certificate IP Extractor

This Python script is designed to help users extract IP addresses associated with a specific SSL certificate serial number. By utilizing socket connections and SSL/TLS handshakes, the script is able to retrieve the certificate's serial number and uses the FOFA search engine to query for all IP addresses that share the same certificate serial number.



## Features

- Retrieves IP addresses associated with a given SSL certificate serial number.
- Supports custom domain and port for SSL connection.
- Adjustable socket connection timeout.
- Displays the queried domain, certificate serial number, and a list of IP addresses.



## Get Started

1. **Prerequisites**: Ensure that you have Python installed on your system.

2. **Installation**:

   - To install the required dependencies individually, use the following command:

     ```bash
     pip install cryptography requests beautifulsoup4
     ```

   - Alternatively, you can use the provided `requirements.txt` file to install the dependencies in one command:

     ```bash
     pip install -r requirements.txt
     ```



## Usage

Run the script using the command-line interface:

```bash
python CertIPs.py [domain] [--port PORT] [--timeout TIMEOUT]
```

- `domain`: The domain to query for SSL certificate IPs.

- `--port`: (Optional) Port number for the SSL connection (default is 443).

- `--timeout`: (Optional) Timeout in milliseconds for the socket connection (default is 10000).

  

## Example

```bash
python CertIPs.py www.baidu.com --port 443 --timeout 15000

   ____                      __       ______      ____     ____       
  /\  _`\                   /\ \__   /\__  _\    /\  _`\  /\  _`\     
  \ \ \/\_\     __    _ __  \ \ ,_\  \/_/\ \/    \ \ \L\ \\ \,\L\_\   
   \ \ \/_/_  /'__`\ /\`'__\ \ \ \/     \ \ \     \ \ ,__/ \/_\__ \   
    \ \ \L\ \/\  __/ \ \ \/   \ \ \_     \_\ \__   \ \ \/    /\ \L\ \ 
     \ \____/\ \____\ \ \_\    \ \__\    /\_____\   \ \_\    \ `\____\
      \/___/  \/____/  \/_/     \/__/    \/_____/    \/_/     \/_____/
                                                                                                                                                                                                                                                                           
Author: Rsa7an

Domain:
- www.baidu.com

Cert Serial:
- 26585094245224241434632730821

IPs:
- 183.232.231.201
- 112.80.255.43
- 124.237.176.143
- 103.211.221.12
- 220.181.112.72
- 110.185.186.49
- 182.61.248.47
- 182.61.200.142
- 112.80.255.214
- 182.61.200.83
```



## References

Apache-2.0 © Rsa7an