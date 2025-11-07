# WiFisploit\wsf\modules\tools\wifite.py

import sys
import shutil
import subprocess
from time import sleep
from pystyle import Colors, Colorate

gradient_colors = Colors.red_to_white
gradient_colors2 = Colors.green_to_cyan

print(Colorate.Horizontal(gradient_colors2, "[+] Starting wifite..."))
sleep(3)

cmd = shutil.which("wifite")
if not cmd:
    print(Colorate.Horizontal(gradient_colors, "[-] wifite not found in PATH."))
    sys.exit(1)

print(Colorate.Horizontal(gradient_colors2, f"[+] Found at: {cmd} — launching..."))
try:
    subprocess.run([cmd])
except KeyboardInterrupt:
    print(Colorate.Horizontal(gradient_colors, "[!] Interrupted by user."))
except Exception as e:
    print(Colorate.Horizontal(gradient_colors, f"[!] Error launching wifite: {e}"))
finally:
        sleep(1)