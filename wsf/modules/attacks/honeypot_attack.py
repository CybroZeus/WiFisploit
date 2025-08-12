# wifisploit/modules/honeypot_attack.py

import socket
import threading
import chardet
import platform
import os
from pystyle import Colorate, Colors
from colorama import init
init(autoreset=True)

gradient_colors = Colors.red_to_white

host = input(Colorate.Horizontal(gradient_colors, "wsf (HOST) > "))
if host.lower() == "back":
    quit()
else:
    print(Colorate.Horizontal(gradient_colors, f"HOST => {host}"))

port = 23

def handle_client(conn, addr):
    print(Colorate.Horizontal(gradient_colors, f"Connected by {addr}"))
    conn.sendall(b"Successfully login to Windows 10 23h2!\n")
    while True:
        conn.sendall(b"telnet> ")
        data = conn.recv(1024)
        if not data:
            break
        result = chardet.detect(data)
        encoding = result["encoding"]

        try:
            data = data.decode(encoding)
            print(Colorate.Horizontal(gradient_colors, f"{addr} Try command: {data}"))
        except UnicodeDecodeError:
            print(Colorate.Horizontal(gradient_colors, "Failed to decode data!"))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()