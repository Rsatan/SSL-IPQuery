# SSL Certificate IP Extractor

This Python script is designed to help users extract IP addresses associated with a specific SSL certificate serial number. By utilizing socket connections and SSL/TLS handshakes, the script is able to retrieve the certificate's serial number and uses the [FOFA](https://fofa.info) search engine to query for all IP addresses that share the same certificate serial number.



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
python main.py [domain] [--port PORT] [--timeout TIMEOUT]
```

- `domain`: The domain to query for SSL certificate IPs.

- `--port`: (Optional) Port number for the SSL connection (default is 443).

- `--timeout`: (Optional) Timeout in milliseconds for the socket connection (default is 10000).

  

## Example

```bash
python main.py www.baidu.com --port 443 --timeout 15000

   ____    ____    __             ______  ____    _____                                      
  /\  _`\ /\  _`\ /\ \           /\__  _\/\  _`\ /\  __`\                                    
  \ \,\L\_\ \,\L\_\ \ \          \/_/\ \/\ \ \L\ \ \ \/\ \  __  __     __   _ __   __  __    
   \/_\__ \\/_\__ \\ \ \  __  ______\ \ \ \ \ ,__/\ \ \ \ \/\ \/\ \  /'__`\/\`'__\/\ \/\ \   
     /\ \L\ \/\ \L\ \ \ \L\ \/\______\_\ \_\ \ \/  \ \ \\'\\ \ \_\ \/\  __/\ \ \/ \ \ \_\ \  
     \ `\____\ `\____\ \____/\/______/\_____\ \_\   \ \___\_\ \____/\ \____\\ \_\  \/`____ \ 
      \/_____/\/_____/\/___/         \/_____/\/_/    \/__//_/\/___/  \/____/ \/_/   `/___/> \
                                                                                       /\___/
                                                                                       \/__/                                                                      
Author: Rsa7an

Domain:
- www.baidu.com

Cert Serial:
- 26585094245224241434632730821

IPs:
- 124.237.208.70
- 221.204.49.47
- 124.237.208.40
- 157.0.148.19
- 39.177.47.142
- 110.242.68.236
- 106.12.1.190
- 124.237.208.104
- 223.109.81.161
```



## License

Apache License 2.0.  © Rsa7an