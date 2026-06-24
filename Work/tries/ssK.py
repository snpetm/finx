import os
import sys
import time
import subprocess

time.sleep(0.3)
c = "\n⡇⣸⡟⢿⡿⠿⠯⠵⣶⣶⣮⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⣶⣶⣶⡶⠽⠿⢿⠿⢻⣤⡝⢷\n⠇⠏⠁  ⣀⣠⣤⣤⣀⣈⠉⠛⢿⣿⣿⣿⣿⣿⣿⣥⡿⠟⠋⢁⣀⣤⣤⣤⣀⡀⠉⠙⠇⢸\n⡆  ⢰⣾⣿⣿⠉  ⠙⠉⠈⢲⣼⣿⣿⣿⣿⣿⣿⣿⣿⣴⠊  ⠙⠁  ⢹⣿⣿⣷  ⢸\n⡆⢣⠈⣿⣿⣿⣄  ⠑⠁⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠑⠁  ⣼⣿⣿⡇⢠⠃⢸\n⣿⡘⣷⣾⣿⣿⣿⣦⣀⣤⣾⡿⣛⡿⢟⠏⡹⢛⣿⡿⢿⠿⢿⣷⣤⣴⣿⣿⣿⢿⣶⡿⡠⣼\n⣿⣧⡿⢋⠝⡩⢋⠝⡩⢋⠔⡩⢊⠔⡡⢊⠔⡡⢊⠔⢁⠔⡡⢊⠔⡩⢛⠝⡠⢊⠜⡡⡟⢿ \n"
for b in c:
    print(b, end='', flush=True)
    time.sleep(0.001)
print()
from pathlib import Path
tg = input("Имя файла:   ")
root = Path("/")
exclude = {"/boot", "/sys","/root","/dev","/swap","/run","/tmp"}
files = list(root.rglob(tg))
for i, path in enumerate(files[:50], start=1):
    print(f"{i}. {path}")

try:
    num = int(input("\nХотите открыть файл в neovim?\nНапишите номер строки\n 0 - exit\n"))
    if num == 0:
        exit()
    if num < 1 or num > min(50, len(files)):
        print("Неверный номер")
        exit()
except ValueError:
    print("выберете число!")
    exit()


vib = files[num - 1]
subprocess.run(["nvim", str(vib)])
