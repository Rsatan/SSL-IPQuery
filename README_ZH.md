[English](README.md) | [简体中文](README_ZH.md)

# SSL Certificate IP Extractor🕵️

此脚本能够帮助用户提取与特定SSL证书序列号相关联的IP地址。通过利用套接字连接和SSL/TLS握手，脚本能够检索证书的序列号，并使用[FOFA](https://fofa.info/)搜索引擎来查询所有共享相同证书序列号的IP地址。



## 特点

- 检索与SSL证书序列号相关联的IP地址。
- 支持自定义域名和SSL连接的端口。
- 可自定义连接超时时间。
- 显示查询的域名、证书序列号和IP地址列表。
- 通过导入文本文件中的域名列表进行批量查询。
- 将查询结果导出到文本文件以供参考。



## 入门指南

1. **环境**：确保您的系统上已安装Python。

2. **安装依赖库**：

   - 安装所需的依赖，请使用以下命令：

     ```bash
     pip install cryptography requests beautifulsoup4
     ```

   - 或者，您可以使用提供的`requirements.txt`文件，在一个命令中安装依赖项：

     ```bash
     pip install -r requirements.txt
     ```



## 用法

使用命令行界面运行脚本：

```bash
python main.py [domain] [--port PORT] [--timeout TIMEOUT] [--file FILE] [--output OUTPUT]
```

- `domain`：要查询SSL证书IP的域名。
- `--port`（可选）：指定SSL连接的端口号（默认为443）。
- `--timeout`（可选）：设置套接字连接的超时时间（默认为10000毫秒）。
- `--file`（可选）：提供包含批量查询的域名和端口的文件路径，格式为`domain:port`。
- `--output`（可选）：指定结果保存的输出文件路径。如果未提供，结果将显示在控制台中。



## 示例

### 单个域名查询

您可以按以下方式查询单个域名的SSL证书信息：

```bash
python main.py example.com --port 443 --timeout 15000
```

输出将类似于以下内容：

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

此示例演示了如何查询单个域名的SSL证书信息，并提供端口和超时的可选参数。您还可以使用`--file`和`--output`选项进行批量查询和结果存储。



## 许可证

Apache License 2.0.  © Rsa7an