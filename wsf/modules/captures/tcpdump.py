# WiFisploit/wsf/modules/captures/tcpdump.py

import os
import sys
import shutil
import subprocess
from time import sleep
from pystyle import Colors, Colorate

gradient_colors = Colors.red_to_white
gradient_colors2 = Colors.green_to_cyan

print(Colorate.Horizontal(gradient_colors2, "[+] Starting tcpdump..."))
sleep(1)

tcpdump_bin = shutil.which("tcpdump")
if not tcpdump_bin:
    print(Colorate.Horizontal(gradient_colors, "[-] tcpdump not found."))
    sys.exit(1)

out_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "Logs", "Captures"))
try:
    os.makedirs(out_dir, exist_ok=True)
except Exception as e:
    print(Colorate.Horizontal(gradient_colors, f"[-] Failed to create capture directory: {e}"))
    sys.exit(1)

out_file = os.path.join(out_dir, "capture.pcap")

while True:
    iface = input(Colorate.Horizontal(gradient_colors, "wsf (Interface) > ")).strip()
    if iface.lower() == "back":
        quit()
    if iface:
        print(Colorate.Horizontal(gradient_colors, f"Interface => {iface}"))
        break

while True:
    v_input = input(Colorate.Horizontal(gradient_colors, "wsf (Verbose 0-3) > ")).strip()
    if v_input.lower() == "back":
        iface = ""
        while not iface:
            iface = input(Colorate.Horizontal(gradient_colors, "wsf (Interface) > ")).strip()
            if iface.lower() == "back":
                quit()
            if iface:
                print(Colorate.Horizontal(gradient_colors, f"Interface => {iface}"))
        continue
    if v_input.isdigit():
        verbose = int(v_input)
        print(Colorate.Horizontal(gradient_colors, f"Verbose => {verbose}"))
        break
    else:
        verbose = 0
        print(Colorate.Horizontal(gradient_colors, f"Verbose => {verbose}"))
        break

while True:
    s_input = input(Colorate.Horizontal(gradient_colors, "wsf (Snaplen bytes, 0=full) > ")).strip()
    if s_input.lower() == "back":
        while True:
            v_input = input(Colorate.Horizontal(gradient_colors, "wsf (Verbose 0-3) > ")).strip()
            if v_input.lower() == "back":
                iface = ""
                while not iface:
                    iface = input(Colorate.Horizontal(gradient_colors, "wsf (Interface) > ")).strip()
                    if iface.lower() == "back":
                            quit()
                    if iface:
                        print(Colorate.Horizontal(gradient_colors, f"Interface => {iface}"))
                continue
            if v_input.isdigit():
                verbose = int(v_input)
                print(Colorate.Horizontal(gradient_colors, f"Verbose => {verbose}"))
                break
            else:
                verbose = 0
                print(Colorate.Horizontal(gradient_colors, f"Verbose => {verbose}"))
                break
        continue
    if s_input.isdigit():
        snaplen = int(s_input)
        print(Colorate.Horizontal(gradient_colors, f"Snaplen => {snaplen}"))
        break
    else:
        snaplen = 0
        print(Colorate.Horizontal(gradient_colors, f"Snaplen => {snaplen}"))
        break

bpf_filter = input(Colorate.Horizontal(gradient_colors, "wsf (BPF filter) > ")).strip()
print(Colorate.Horizontal(gradient_colors, f"BPF filter => '{bpf_filter}'" if bpf_filter else "BPF filter => (none)"))

print(Colorate.Horizontal(gradient_colors, "\n[*] Type 'start' to begin capture or 'exit' to quit."))

while True:
    cmdline = input(Colorate.Horizontal(gradient_colors, f"wsf ({iface}) > ")).strip().lower()
    if cmdline == "start":
        out_file = os.path.join(out_dir, "capture.pcap")

        cmd = [tcpdump_bin, "-i", iface, "-s", str(snaplen), "-w", out_file, "-n"]
        if verbose > 0:
            cmd += ["-" + "v"*verbose]
        if bpf_filter:
            cmd.append(bpf_filter)

        print(Colorate.Horizontal(gradient_colors2, "[+] Starting tcpdump... Ctrl + C to stop."))
        try:
            p = subprocess.Popen(cmd)
            try:
                p.wait()
            except KeyboardInterrupt:
                print(Colorate.Horizontal(gradient_colors, "[!] Capture stopped by user. Stopping tcpdump..."))
                try:
                    p.terminate()
                    p.wait(timeout=3)
                except Exception:
                    p.kill()
                    p.wait()
        except FileNotFoundError:
            print(Colorate.Horizontal(gradient_colors, "[-] tcpdump binary disappeared or cannot be executed."))
            sys.exit(1)
        except Exception as e:
            print(Colorate.Horizontal(gradient_colors, f"[-] Error running tcpdump: {e}"))
            sys.exit(1)

        size = os.path.getsize(out_file) if os.path.exists(out_file) else 0
        if size > 0 and getattr(p, "returncode", 1) == 0:
            print(Colorate.Horizontal(gradient_colors2, f"[+] Capture saved to {out_file} ({size} bytes)"))
        elif size > 0:
            print(Colorate.Horizontal(gradient_colors2, f"[!] tcpdump exited with code {p.returncode}, partial capture saved to {out_file} ({size} bytes)"))
        else:
            print(Colorate.Horizontal(gradient_colors, f"[-] No capture saved. tcpdump exit code: {getattr(p, 'returncode', 'unknown')}"))
        break

    elif cmdline in ("exit", "quit"):
        print(Colorate.Horizontal(gradient_colors, "[!] Exiting without capture."))
        sys.exit(0)
    else:
        print(Colorate.Horizontal(gradient_colors, "[!] Unknown command. Type 'start' to begin or 'exit' to quit."))