# -*- coding: utf-8 -*-
"""
Modified for Termux (Non-Rooted Android)
Original Author: new92
"""

import sys
import os
import json
import requests
import instagrapi
import instaloader
from time import sleep
from datetime import datetime
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED

# Function to clear the screen
def clear():
    os.system("clear")

# Function to check username validity
def checkUser(username: str) -> bool:
    return not username or len(username) > 30

# Function to validate if an Instagram user exists
def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

# Function to display the banner
def banner() -> str:
    return f"""{YELLOW}
    ███████╗ ██████╗ ███████╗███╗   ██╗██╗   ██╗
    ██╔════╝██╔═══██╗██╔════╝████╗  ██║██║   ██║
    ███████╗██║   ██║█████╗  ██╔██╗ ██║██║   ██║
    ╚════██║██║   ██║██╔══╝  ██║╚██╗██║██║   ██║
    ███████║╚██████╔╝███████╗██║ ╚████║╚██████╔╝
    ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
    """

# Function to start follower automation
def start_bot():
    clear()
    print(banner())
    print("\n")
    print(f"{YELLOW}[+] IGFollowersIncreaser for Termux - Instagram Automation")
    print("\n")

    # Get username and validate
    username = input(f"{YELLOW}[>] Enter your Instagram username: ").strip().lower()
    while checkUser(username) or valUser(username):
        print(f"{RED}[!] Invalid username. Please try again.")
        username = input(f"{YELLOW}[>] Enter your Instagram username: ").strip().lower()

    # Get password securely
    password = input(f"{YELLOW}[>] Enter your Instagram password: ").strip()

    print(f"{GREEN}[+] Logging in...")

    # Login to Instagram
    client = instagrapi.Client()
    try:
        login = client.login(username, password)
        if login:
            print(f"{GREEN}[✓] Login successful!")
        else:
            print(f"{RED}[×] Login failed. Check your credentials.")
            sys.exit(1)
    except Exception as ex:
        print(f"{RED}[!] Error logging in: {ex}")
        sys.exit(1)

    sleep(2)
    clear()

    print(f"{YELLOW}[+] Starting follower automation...")
    sleep(2)

    # List of high-profile Instagram accounts to follow/unfollow
    accounts = [
        173560420,   # Cristiano Ronaldo
        1436859892,  # Cardi B
        18428658,    # Kim Kardashian
        7719696,     # Ariana Grande
        451573056,   # Nicki Minaj
        247944034,   # Beyonce
        460563723,   # Selena Gomez
        6860189,     # Justin Bieber
        427553890,   # Lionel Messi
        26669533,    # Neymar Jr
        4213518589,  # Kylian Mbappe
        12281817,    # Kylie Jenner
        290023231,   # Real Madrid
        1269788896   # Champions League
    ]

    followed = 0
    unfollowed = 0

    for account in accounts:
        try:
            client.user_follow(account)
            followed += 1
            print(f"{GREEN}[+] Followed account ID {account}")
            sleep(3)  # Delay to reduce bot detection

            client.user_unfollow(account)
            unfollowed += 1
            print(f"{YELLOW}[-] Unfollowed account ID {account}")
            sleep(3)
        except Exception as e:
            print(f"{RED}[!] Error following/unfollowing {account}: {e}")
            continue

    print(f"{GREEN}[✓] Automation complete! Followed: {followed}, Unfollowed: {unfollowed}")

if __name__ == "__main__":
    start_bot()
