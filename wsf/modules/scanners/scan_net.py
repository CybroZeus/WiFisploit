# wifisploit/modules/scan_all.py

import os
from pystyle import Colorate, Colors, Write
from colorama import init
init(autoreset=True)

gradient_colors = Colors.red_to_white

interface = Write.Input(Colorate.Horizontal(gradient_colors, "wsf (Interface) > "))
if interface.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Interface => {interface}"))

bssid = Write.Input(Colorate.Horizontal(gradient_colors, "wsf (BSSID) > "))
if bssid.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"BSSID => {bssid}"))

os.system(f"airodump-ng --bssid {bssid} -M {interface}")