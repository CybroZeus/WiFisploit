# wifisploit/modules/brute_force.py

import os
from pystyle import Colorate, Colors
from colorama import init
init(autoreset=True)

gradient_colors = Colors.red_to_white

bssid = input(Colorate.Horizontal(gradient_colors, "wsf (BSSID) > "))
if bssid.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"BSSID => {bssid}"))

handshake = input(Colorate.Horizontal(gradient_colors, "wsf (Handshake) > "))
if handshake.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Handshake => {handshake}"))

channel = input(Colorate.Horizontal(gradient_colors, "wsf (Channel) > "))
if channel.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Channel => {channel}"))

min_len = input(Colorate.Horizontal(gradient_colors, "wsf (Minimum) > "))
if min_len.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Minimum => {min_len}"))

max_len = input(Colorate.Horizontal(gradient_colors, "wsf (Maximum) > "))
if max_len.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Maximum => {max_len}"))

type_ = input(Colorate.Horizontal(gradient_colors, "wsf (Type) > "))
if type_.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Type => {type_}"))

os.system(f"crunch {min_len} {max_len} \"{type_}\" | aircrack-ng -b {bssid} -c {channel} {handshake}")