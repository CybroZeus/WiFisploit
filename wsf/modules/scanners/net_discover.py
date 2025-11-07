# WiFisploit\wsf\modules\scanners\net_discover.py

import os
from pystyle import Colors, Colorate

gradient_colors = Colors.red_to_white

print(Colorate.Horizontal(gradient_colors, "\nMake sure you are not in Monitor mode!\n"))
host = input(Colorate.Horizontal(gradient_colors, "wsf (HOST) > ")).strip()
if host.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"HOST => {host}"))

os.system(f"netdiscover -r {host}")