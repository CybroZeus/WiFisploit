# WiFisploit\wsf\modules\attacks\crack_handshake.py

import os
from pystyle import Colors, Colorate

gradient_colors = Colors.red_to_white

handshake = input(Colorate.Horizontal(gradient_colors, "wsf (Handshake) > ")).strip()
if handshake.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Handshake => {handshake}"))

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

wordlist = input(Colorate.Horizontal(gradient_colors, "wsf (Wordlist) > ")).strip()
if wordlist.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Wordlist => {wordlist}"))

os.system(f"aircrack-ng -b {bssid} -c {channel} -w {wordlist} {handshake}")