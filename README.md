[English](README.md) | [简体中文](README_ZH.md)

# SSL Certificate IP Extractor🕵️

This Python script is designed to help users extract IP addresses associated with a specific SSL certificate serial number. By utilizing socket connections and SSL/TLS handshakes, the script is able to retrieve the certificate's serial number and uses the [FOFA](https://fofa.info) search engine to query for all IP addresses that share the same certificate serial number.



## Features

- Retrieve IP addresses associated with a given SSL certificate serial number.
- Support custom domain and port for SSL connections.
- Adjustable socket connection timeout.
- Display the queried domain, certificate serial number, and a list of IP addresses.
- Batch query by importing a list of domains from a text file.
- Export query results to a text file for easy reference.



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
python main.py [domain] [--port PORT] [--timeout TIMEOUT] [--file FILE] [--output OUTPUT]
```

- `domain`: The domain to query for SSL certificate IPs.
- `--port` (Optional): Specify the port number for the SSL connection (default is 443).
- `--timeout` (Optional): Set the timeout in milliseconds for the socket connection (default is 10000).
- `--file` (Optional): Provide a file path containing a list of domains and ports in the format `domain:port` for batch queries.
- `--output` (Optional): Specify an output file path to save the results. If not provided, the results will be displayed in the console.



## Example

### Single Domain Query

You can query SSL certificate information for a single domain as follows:

```bash
python main.py example.com --port 443 --timeout 15000
```

The output will look like this:

```bash
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
- example.com

Cert Serial:
- 16115816404043435608139631424403370993

IPs:
- 68.232.45.14
- 68.232.44.115
- 192.210.190.104
- 68.232.35.34
- 68.232.34.14
- 116.196.84.120
- 93.184.215.14
- 67.225.138.85
- 164.90.215.163
```

This example demonstrates how to query SSL certificate information for a single domain, providing optional parameters for port and timeout.

You can also use the `--file` and `--output` options for batch queries and result storage.



## License

Apache License 2.0.  © Rsa7an