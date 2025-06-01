from os import system as c
import os
import time
import random

A = '\033[1;97m'
R = '\033[1;31m'
Y = '\033[1;33m'
G = '\033[1;32m'
C = '\033[1;36m'

def logo():
    c('clear')
    print(f"""{G}
██╗    ██╗██╗███████╗██╗
██║    ██║██║██╔════╝██║
██║ █╗ ██║██║█████╗  ██║
██║███╗██║██║██╔══╝  ██║
╚███╔███╔╝██║███████╗███████╗
 ╚══╝╚══╝ ╚═╝╚══════╝╚══════╝
  {Y}WIFI HACKING ROOT PRANK TOOL
{A}----------------------------
""")

def check_root():
    if os.geteuid() != 0:
        print(f"\n{R}[!] Root Permission Not Granted!")
        print(f"{Y}[!] This Tool Only Works On Rooted Devices!")
        exit()

def wifi_hack():
    logo()
    check_root()
    print(f"{Y}[+] Scanning Nearby WiFi Networks...\n")
    time.sleep(2)

    wifi_list = ['WiFi_Zone_24G', 'Home_Network', 'Cafe_Wifi', 'Public_Hotspot', 'VIP_Net']
    for wifi in wifi_list:
        print(f"{C}[*] Found: {wifi}")
        time.sleep(1)

    target = input(f"\n{C}[+] Enter Target WiFi Name: ")
    print(f"{Y}[+] Connecting to {target}...")
    time.sleep(2)
    print(f"{Y}[+] Starting Password Bruteforce...\n")

    passwords = ['12345678', 'password123', 'qwertyuiop', 'adminadmin', 'letmein123']

    for pw in passwords:
        print(f"{C}[*] Trying Password: {pw}")
        time.sleep(1)

    print(f"\n{G}[✓] WiFi Password Cracked Successfully!")
    print(f"{Y}[!] Password: {R}{random.choice(passwords)}")
    input(f"\n{A}Press Enter To Exit...")

wifi_hack()