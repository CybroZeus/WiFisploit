# WiFisploit\wsf\modules\scanners\scan_net.py

import os
from pystyle import Colors, Colorate

gradient_colors = Colors.red_to_white

interface = input(Colorate.Horizontal(gradient_colors, "wsf (Interface) > ")).strip()
if interface.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Interface => {interface}"))

bssid = input(Colorate.Horizontal(gradient_colors, "wsf (BSSID) > ")).strip()
if bssid.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"BSSID => {bssid}"))

os.system(f"airodump-ng --bssid {bssid} -M {interface}")