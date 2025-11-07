# WiFisploit\wsf\modules\captures\capture_traffic.py

import os
from pystyle import Colors, Colorate

gradient_colors = Colors.red_to_white

interface = input(Colorate.Horizontal(gradient_colors, "wsf (Interface) > ")).strip()
if interface.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Interface => {interface}"))

os.system(f"tcpdump -i {interface}")