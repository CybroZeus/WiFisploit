# wifisploit/modules/scan_wps.py

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

os.system(f"airodump-ng -M --wps {interface}")