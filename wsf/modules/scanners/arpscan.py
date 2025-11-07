# WiFisploit\wsf\modules\scanners\arpscan.py

import re
import csv
import subprocess
from pathlib import Path
from pystyle import Colors, Colorate

gradient_colors = Colors.red_to_white
gradient_colors2 = Colors.green_to_cyan

interface = input(Colorate.Horizontal(gradient_colors, "wsf (Interface) > ")).strip()
if interface.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Interface => {interface or '(auto)'}"))

target = input(Colorate.Horizontal(gradient_colors, "wsf (Target CIDR or 'local') > ")).strip()
if target.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"Target => {target or 'local'}"))

timeout_input = input(Colorate.Horizontal(gradient_colors, "wsf (Timeout seconds, default 60) > ")).strip()
if timeout_input.lower() == "back":
    quit()
try:
    timeout = int(timeout_input) if timeout_input else 60
except Exception:
    timeout = 60

save_csv = input(Colorate.Horizontal(gradient_colors, "wsf (Save results to CSV? Y/N) > ")).strip().lower()
if save_csv == "back":
    quit()
save_csv = save_csv == "y"

use_local = (target == "" or target.lower() == "local")
if use_local:
    cmd = ["arp-scan", "-l", "--interface", interface] if interface else ["arp-scan", "-l"]
else:
    cmd = ["arp-scan", target, "--interface", interface] if interface else ["arp-scan", target]

print(Colorate.Horizontal(gradient_colors2, f"\n[+] Running: {' '.join(cmd)} (timeout {timeout}s)\n"))

try:
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    out = proc.stdout + proc.stderr
except subprocess.TimeoutExpired:
    print(Colorate.Horizontal(gradient_colors, "[-] arp-scan timed out.\n"))
    quit()
except KeyboardInterrupt:
    print(Colorate.Horizontal(gradient_colors, "\n[-] Interrupted. Type 'back' to exit.\n"))
    quit()
except Exception as e:
    print(Colorate.Horizontal(gradient_colors, f"[-] Error running arp-scan: {e}\n"))
    quit()

pattern = re.compile(r"(\d{1,3}(?:\.\d{1,3}){3})\s+([0-9a-fA-F:]{17})(?:\s+(.*))?")
results = []
for line in out.splitlines():
    m = pattern.search(line)
    if m:
        ip = m.group(1)
        mac = m.group(2).lower()
        vendor = m.group(3).strip() if m.group(3) else ""
        results.append((ip, mac, vendor))

oui_path_candidates = [
    "/usr/share/arp-scan/ieee-oui.txt",
    "/usr/share/ieee-data/oui.csv",
    "/usr/share/misc/oui.txt"
]
oui_map = {}
for p in oui_path_candidates:
    pth = Path(p)
    if pth.exists():
        try:
            for l in pth.read_text(errors="ignore").splitlines():
                parts = l.strip().split(None, 1)
                if len(parts) >= 2:
                    key = parts[0].lower().replace("-", ":")
                    key = key.replace(".", "")
                    k = key
                    if len(k) >= 6:
                        knorm = ":".join([k[i:i+2] for i in range(0,6,2)])
                        oui_map[knorm] = parts[1].strip()
        except Exception:
            pass
        break

filled = []
for ip, mac, vendor in results:
    if not vendor and oui_map:
        prefix = mac.lower()[0:8]
        vendor = oui_map.get(prefix, "")
    filled.append((ip, mac, vendor))
results = filled

if not results:
    print(Colorate.Horizontal(gradient_colors, "[-] No hosts found or arp-scan produced no parseable output.\n"))
    quit()

header = f"{'IP':<16} {'MAC':<20} {'VENDOR'}"
print(Colorate.Horizontal(gradient_colors2, "[+] arp-scan Results\n"))
print(Colorate.Horizontal(gradient_colors, header))
print(Colorate.Horizontal(gradient_colors, "-" * 80))
for ip, mac, vendor in sorted(results, key=lambda x: x[0]):
    line = f"{ip:<16} {mac:<20} {vendor}"
    print(Colorate.Horizontal(gradient_colors, line))
print(Colorate.Horizontal(gradient_colors2, f"\n[+] Scan finished. {len(results)} host(s) found.\n"))

if save_csv:
    filename = "arp-scan_results.csv"
    try:
        current_file = Path(__file__).resolve()
        project_root = None
        for anc in current_file.parents:
            if anc.name.lower() == "wifisploit":
                project_root = anc
                break
        if project_root is None:
            if len(current_file.parents) >= 5:
                project_root = current_file.parents[4]
            else:
                project_root = Path.cwd()
    except Exception:
        project_root = Path.cwd()

    logs_dir = project_root / "Logs"
    try:
        logs_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(Colorate.Horizontal(gradient_colors, f"[-] Failed to create Logs dir: {e}\n"))
        logs_dir = Path.cwd() / "WiFisploit" / "Logs"
        logs_dir.mkdir(parents=True, exist_ok=True)

    outpath = logs_dir / filename

    try:
        with open(outpath, "w", newline="") as csvfile:
            cw = csv.writer(csvfile)
            cw.writerow(["IP", "MAC", "VENDOR"])
            for ip, mac, vendor in sorted(results, key=lambda x: x[0]):
                cw.writerow([ip, mac, vendor])
        print(Colorate.Horizontal(gradient_colors2, f"[+] Results saved to {outpath}\n"))
    except Exception as e:
        print(Colorate.Horizontal(gradient_colors, f"[-] Failed to save CSV: {e}\n"))

quit()