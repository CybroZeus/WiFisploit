# WiFisploit
WiFisploit is a Python-based tool designed for Wi-Fi network penetration testing and security auditing. It provides a variety of functionalities to scan for WiFi networks, test their vulnerabilities, and perform attacks like deauthentication and password brute forcing. This tool is intended for educational and authorized security testing purposes only.

Features
Scan available WiFi networks.

Attempt to connect to targeted networks.

Perform deauthentication attacks to disconnect clients.

Brute force WiFi passwords.

Simple command-line interface for ease of use.

Capture Handshake.

Honeypot attack.

DoS attack.

Crack handshake.

WPS attack.

Discover network.

Usage:
Run the script with appropriate permissions (usually root) and follow the on-screen prompts to select your target and attack method.

Disclaimer: Use this tool responsibly and only on networks you own or have explicit permission to test. Unauthorized access or attacks on networks are illegal.

### Update:
```
apt update && apt full-upgrade -y
```
### Run:
```
cd WiFisploit/wsf/
```
```
python3 wsf.py
```
### Usage:
```
 __      __ ______________ __                __          __  __
/  \    /  \   \_   _____/|__| ____________ |  |   ____ |__|/  |_
\   \/\/   /   ||    __)  |  |/  ___/\____ \|  |  /  _ \|  \   __|
 \        /|   ||     \   |  |\___ \ |  |_> >  |_(  <_> )  ||  |
  \__/\  / |___|\___  /   |__/____  >|   __/|____/\____/|__||__|
       \/           \/            \/ |__|
WiFisploit - Wireless Hacking Framework

Github: https://github.com/CybroZeus/WiFisploit

Developed By CybroZeus

    Command                     Description

0   help                        Display help menu.
1   clear                       Clean terminal screen.
2   ifconfig                    Display network interface settings.
3   iwconfig                    Display wireless network interfaces settings.
4   kill                        Prepare your wireless adapter.
5   start                       Start monitor mode.
6   stop                        Stop monitor mode.
7   modules                     Display all modules.
8   tutorial                    Tool tutorial.
9   install                     Install requirements.
10  exit                        Leave the tool.

There is 12 modules you can use.
```