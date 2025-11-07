# WiFisploit\wsf\modules\attacks\honeypot_attack.py

import socket
import chardet
import threading
from pystyle import Colors, Colorate

gradient_colors = Colors.red_to_white
gradient_colors2 = Colors.green_to_cyan

host = input(Colorate.Horizontal(gradient_colors, "wsf (HOST) > ")).strip()
if host.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"HOST => {host}"))

port = 23

def handle_client(conn, addr):
    print(Colorate.Horizontal(gradient_colors2, f"Connected by {addr}"))
    conn.sendall("Successfully login to Windows 10 23h2!\n".encode("utf-8"))
    while True:
        conn.sendall("telnet> ".encode("utf-8"))
        data = conn.recv(1024)
        if not data:
            break

        result = chardet.detect(data)
        encoding = result.get("encoding") or "utf-8"
        
        try:
            decoded = data.decode(encoding, errors="replace")
            print(Colorate.Horizontal(gradient_colors, f"{addr} Try command: {decoded.strip()}"))
        except UnicodeDecodeError:
            decoded = data.decode("utf-8", errors="replace")
            print(Colorate.Horizontal(gradient_colors, f"{addr} Try command (fallback): {decoded.strip()}"))
    try:
        conn.close()
    except Exception:
        pass

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.daemon = True
        thread.start()