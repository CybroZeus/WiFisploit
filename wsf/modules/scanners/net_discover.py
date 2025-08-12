# wifisploit/modules/net_discover.py

import os
from pystyle import Colorate, Colors
from colorama import init
init(autoreset=True)

gradient_colors = Colors.red_to_white

print(Colorate.Horizontal(gradient_colors, "\nMake sure you are not in monitor mode!\n"))
host = input(Colorate.Horizontal(gradient_colors, "wsf (HOST) > "))
if host.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"HOST => {host}"))

os.system(f"netdiscover -r {host}")