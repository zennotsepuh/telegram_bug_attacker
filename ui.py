# -*- coding: utf-8 -*-
# UI DECORATIONS - © DanzModss
# BIKIN TAMPILAN KEREN KAYAK HACKER BENERAN!

import os
import time
from colorama import init, Fore, Back, Style
import requests

init(autoreset=True)

class UIManager:
    def __init__(self, config):
        self.config = config
        self.image_url = config.BANNER_IMAGE
        self.color_map = {
            'red': Fore.RED,
            'blue': Fore.BLUE,
            'green': Fore.GREEN,
            'yellow': Fore.YELLOW,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.WHITE
        }
        self.main_color = self.color_map.get(config.BANNER_COLOR, Fore.RED)
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def fetch_image(self):
        try:
            response = requests.get(self.image_url, timeout=5)
            if response.status_code == 200:
                return f"[🖼️] Image loaded: {self.image_url}"
            return "[❌] Image not found, using default"
        except:
            return "[❌] Cannot fetch image, check your URL"
            
    def show_banner(self):
        self.clear_screen()
        
        # Main Banner
        print(f"""
{self.main_color}╔════════════════════════════════════════════════════════╗
{self.main_color}║  {Fore.WHITE}🔥 TELEGRAM BUG ATTACKER PRO V12 - DARK EDITION 🔥{self.main_color}  ║
{self.main_color}║  {Fore.YELLOW}© DanzModss - Unauthorized Use = Your Ass Get Hacked{self.main_color} ║
{self.main_color}║  {Fore.GREEN}[+] Status: ONLINE - UNFILTERED MODE{self.main_color}         ║
{self.main_color}║  {Fore.CYAN}📱 Owner: {OWNER_ID}{self.main_color}                             ║
{self.main_color}║  {Fore.MAGENTA}{self.fetch_image()}{self.main_color}                    ║
{self.main_color}╚════════════════════════════════════════════════════════╝
        """)
        
        # Loading Animation
        print(f"{Fore.CYAN}[+] Loading modules...")
        for i in range(101):
            print(f"\r{Fore.GREEN}[{i}%] {'█' * (i//2)}", end='')
            time.sleep(0.02)
        print(f"\n{Fore.GREEN}[✅] System ready to rape!\n")
        
    def show_menu(self, bug_menu):
        print(f"""
{Fore.CYAN}╔═══════════════════════════════════════╗
{Fore.CYAN}║  {Fore.RED}💀 BUG MENU - 200+ OPTIONS 💀{Fore.CYAN}  ║
{Fore.CYAN}╚═══════════════════════════════════════╝
        """)
        
        for key, value in bug_menu.items():
            print(f"{Fore.YELLOW}[{key}] {Fore.WHITE}{value['name']} {Fore.CYAN} - {value['desc']}")
            
        print(f"""
{Fore.MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Fore.RED}[0] EXIT - KALO BERANI KELUAR!
{Fore.MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """)
        
    def show_loading(self, message="Processing..."):
        print(f"{Fore.YELLOW}[⏳] {message}")
        for i in range(51):
            print(f"\r{Fore.GREEN}[{'▰' * i}{'▱' * (50-i)}] {i*2}%", end='')
            time.sleep(0.03)
        print(f"\n{Fore.GREEN}[✅] Done!\n")
        
    def show_error(self, message):
        print(f"{Fore.RED}[❌] ERROR: {message}")
        
    def show_success(self, message):
        print(f"{Fore.GREEN}[✅] {message}")
        
    def show_warning(self, message):
        print(f"{Fore.YELLOW}[⚠️] {message}")
        
    def get_input(self, prompt):
        return input(f"{Fore.CYAN}[>] {prompt}{Fore.WHITE}")
