#!/usr/bin/env python3

# WiFisploit
# Telegram Channel: https://t.me/wannacryzero
# GitHub: https://github.com/CybroZeus
# Telegram: https://t.me/CybroZeus
# Author: CybroZeus

import os
import sys
import time
import platform
import subprocess
from pystyle import *

gradient_colors = Colors.red_to_white


def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

clear_screen()

def root_check():
    try:
        if os.geteuid() != 0:
            print(Colorate.Horizontal(gradient_colors, "[-] Please run as root!"))
            sys.exit(1)
    except AttributeError:
        pass

root_check()

def startup(message="[*] Starting WiFisploit", duration=3.0, speed=1):
    frames = ["|", "/", "-", "\\"]
    dots = ["", ".", "..", "..."]
    start = time.time()
    i = 0
    j = 0
    try:
        while (time.time() - start) < duration:
            spin = frames[i % len(frames)]
            dot = dots[j % len(dots)]
            text = f"{message}{dot} {spin}"
            colored = Colorate.Horizontal(gradient_colors, text)
            sys.stdout.write("\r" + colored)
            sys.stdout.flush()
            time.sleep(speed)
            i += 1
            if i % 4 == 0:
                j += 1
        sys.stdout.flush()
    except KeyboardInterrupt:
        sys.stdout.write("\n"); sys.stdout.flush()
        
startup("[*] Starting WiFisploit", duration=3.0, speed=0.05)
clear_screen()

WiFisploit = """
 ▄█     █▄   ▄█     ▄████████  ▄█     ▄████████    ▄███████▄  ▄█        ▄██████▄   ▄█      ███
███     ███ ███    ███    ███ ███    ███    ███   ███    ███ ███       ███    ███ ███  ▀█████████▄
███     ███ ███▌   ███    █▀  ███▌   ███    █▀    ███    ███ ███       ███    ███ ███▌    ▀███▀▀██
███     ███ ███▌  ▄███▄▄▄     ███▌   ███          ███    ███ ███       ███    ███ ███▌     ███   ▀
███     ███ ███▌ ▀▀███▀▀▀     ███▌ ▀███████████ ▀█████████▀  ███       ███    ███ ███▌     ███
███     ███ ███    ███        ███           ███   ███        ███       ███    ███ ███      ███
███ ▄█▄ ███ ███    ███        ███     ▄█    ███   ███        ███▌    ▄ ███    ███ ███      ███
 ▀███▀███▀  █▀     ███        █▀    ▄████████▀   ▄████▀      █████▄▄██  ▀██████▀  █▀      ▄████▀
                                                             ▀
WiFisploit - Wireless Hacking Framework

GitHub: https://github.com/CybroZeus/WiFisploit
Telegram Channel: @wannacryzero
Telegram: @CybroZeus
Author: CybroZeus

╔══════════════════════════╗
║ [+] Total modules   : 19 ║
║ [+] Scan modules    : 6  ║
║ [+] Tools modules   : 5  ║
║ [+] Attack modules  : 5  ║
║ [+] Capture modules : 3  ║
╚══════════════════════════╝
"""

print(Colorate.Horizontal(gradient_colors, WiFisploit))

while True:
    try:
        cmd = input(Colorate.Horizontal(gradient_colors, "\nwsf > "))
        if not cmd:
            continue
        if cmd.lower() == "help":
            help = """
WiFisploit Help

    Command           Description

0   help              Display help menu
1   clear             Clean terminal screen
2   ifconfig          Display network interface settings
3   iwconfig          Display wireless network interfaces settings
4   kill              Prepare your wireless adapter
5   start             Start monitor mode
6   stop              Stop monitor mode
7   modules           Display all modules
8   banner            Print WiFisploit banner
9   about             About
10  exit              Leave the tool
"""
            print(Colorate.Horizontal(gradient_colors, help))

        elif cmd.lower() == "clear":
            os.system("clear")

        elif cmd.lower() == "ifconfig":
            os.system("ifconfig")

        elif cmd.lower() == "iwconfig":
            os.system("iwconfig")

        elif cmd.lower() == "kill":
            os.system("airmon-ng check kill")
            os.system("systemctl restart NetworkManager")

        elif cmd.startswith("start"):
            os.system("airmon-ng start wlan0")

        elif cmd.startswith("stop"):
            os.system("airmon-ng stop wlan0mon")

        elif cmd.lower() == "modules":
            modules = """
WiFisploit Modules

    Module                                      Description

0   modules/scanners/scan_all                   Scanning all networks
1   modules/scanners/scan_net                   Scanning single network
2   modules/scanners/scan_wash                  Scanning with wash
3   modules/scanners/scan_wps                   Scanning WPS networks
4   modules/scanners/net_discover               Scanning with netdiscover
5   modules/captures/capture_traffic            Capturing traffic on network
6   modules/captures/capture_handshake          Capturing 4-way handshake
7   modules/scanners/arpscan                    ARP scan (arp-scan wrapper)
8   modules/captures/tcpdump                    Tcpdump wrapper/Packet captures
9   modules/attacks/brute_force                 Wi-Fi Brute Force without wordlist
10  modules/attacks/crack_handshake             Cracking handshake with wordlist
11  modules/attacks/dos_attack                  Network Denial of Service Attack
12  modules/attacks/wps_attack                  Start WPS PIN Attack
13  modules/attacks/honeypot_attack             Start Honeypot Attack
14  modules/tools/airgeddon                     Multi-use wireless audit bash script
15  modules/tools/bettercap                     Swiss-army MITM/network tool (bettercap)
16  modules/tools/wifite                        Automated wireless attack tool (wifite)
17  modules/tools/wireshark                     Network sniffer for capturing/analyzing packets
"""
            print(Colorate.Horizontal(gradient_colors, modules))
            
        elif cmd.lower() == "use scan_all" or cmd.lower() == "use 0":
            os.system("python3 modules/scanners/scan_all.py")

        elif cmd.lower() == "use scan_net" or cmd.lower() == "use 1":
            os.system("python3 modules/scanners/scan_net.py")

        elif cmd.lower() == "use scan_wash" or cmd.lower() == "use 2":
            os.system("python3 modules/scanners/scan_wash.py")

        elif cmd.lower() == "use scan_wps" or cmd.lower() == "use 3":
            os.system("python3 modules/scanners/scan_wps.py")

        elif cmd.lower() == "use net_discover" or cmd.lower() == "use 4":
            os.system("python3 modules/scanners/net_discover.py")

        elif cmd.lower() == "use capture_traffic" or cmd.lower() == "use 5":
            os.system("python3 modules/captures/capture_traffic.py")

        elif cmd.lower() == "use capture_handshake" or cmd.lower() == "use 6":
            os.system("python3 modules/captures/capture_handshake.py")

        elif cmd.lower() == "use arpscan" or cmd.lower() == "use 7":
            os.system("python3 modules/scanners/arpscan.py")

        elif cmd.lower() == "use tcpdump" or cmd.lower() == "use 8":
            os.system("python3 modules/captures/tcpdump.py")

        elif cmd.lower() == "use brute_force" or cmd.lower() == "use 9":
            os.system("python3 modules/attacks/brute_force.py")

        elif cmd.lower() == "use crack_handshake" or cmd.lower() == "use 10":
            os.system("python3 modules/attacks/crack_handshake.py")

        elif cmd.lower() == "use dos_attack" or cmd.lower() == "use 11":
            os.system("python3 modules/attacks/dos_attack.py")

        elif cmd.lower() == "use wps_attack" or cmd.lower() == "use 12":
            os.system("python3 modules/attacks/wps_attack.py")

        elif cmd.lower() == "use honeypot_attack" or cmd.lower() == "use 13":
            os.system("python3 modules/attacks/honeypot_attack.py")

        elif cmd.lower() == "use airgeddon" or cmd.lower() == "use 14":
            os.system("python3 modules/tools/airgeddon.py")

        elif cmd.lower() == "use bettercap" or cmd.lower() == "use 15":
            os.system("python3 modules/tools/bettercap.py")

        elif cmd.lower() == "use wifite" or cmd.lower() == "use 16":
            os.system("python3 modules/tools/wifite.py")

        elif cmd.lower() == "use wireshark" or cmd.lower() == "use 17":
            os.system("python3 modules/tools/wireshark.py")

        elif cmd.lower() == "banner":
            banner = """
 ▄█     █▄   ▄█     ▄████████  ▄█     ▄████████    ▄███████▄  ▄█        ▄██████▄   ▄█      ███
███     ███ ███    ███    ███ ███    ███    ███   ███    ███ ███       ███    ███ ███  ▀█████████▄
███     ███ ███▌   ███    █▀  ███▌   ███    █▀    ███    ███ ███       ███    ███ ███▌    ▀███▀▀██
███     ███ ███▌  ▄███▄▄▄     ███▌   ███          ███    ███ ███       ███    ███ ███▌     ███   ▀
███     ███ ███▌ ▀▀███▀▀▀     ███▌ ▀███████████ ▀█████████▀  ███       ███    ███ ███▌     ███
███     ███ ███    ███        ███           ███   ███        ███       ███    ███ ███      ███
███ ▄█▄ ███ ███    ███        ███     ▄█    ███   ███        ███▌    ▄ ███    ███ ███      ███
 ▀███▀███▀  █▀     ███        █▀    ▄████████▀   ▄████▀      █████▄▄██  ▀██████▀  █▀      ▄████▀
                                                             ▀
WiFisploit - Wireless Hacking Framework

GitHub: https://github.com/CybroZeus/WiFisploit
Telegram Channel: @wannacryzero
Telegram: @CybroZeus
Author: CybroZeus

╔══════════════════════════╗
║ [+] Total modules   : 19 ║
║ [+] Scan modules    : 6  ║
║ [+] Tools modules   : 5  ║
║ [+] Attack modules  : 5  ║
║ [+] Capture modules : 3  ║
╚══════════════════════════╝
"""
            print(Colorate.Horizontal(gradient_colors, banner))

        elif cmd.lower() == "about":
            about = """About WiFisploit:
----------------------
Description          : WiFisploit - Wireless Hacking Framework
Version              : 2
Programming language : Python
Interface language   : English
Author               : CybroZeus
GitHub               : https://github.com/CybroZeus/WiFisploit
Telegram Channel     : https://t.me/wannacryzero
Telegram             : https://t.me/CybroZeus
"""
            print(Colorate.Horizontal(gradient_colors, about))

        elif cmd.lower() == "exit":
            quit()

        else:
            try:
                ret = subprocess.run(cmd, shell=True)
                if ret.returncode != 0:
                    print(Colorate.Horizontal(gradient_colors, f"[!] Command exited with code {ret.returncode}"))
            except KeyboardInterrupt:
                print(Colorate.Horizontal(gradient_colors, "\n[!] Command interrupted by user"))
            except Exception as e:
                print(Colorate.Horizontal(gradient_colors, f"[!] Failed to run command: {e}"))
    except Exception:
        print(Colorate.Horizontal(gradient_colors, "[!] Syntax error!"))
