# -*- coding: utf-8 -*-
# MAIN EXECUTION FILE - © DanzModss
# JALANKAN INI BUAT MULAI NGACURIN TELEGRAM!

import sys
import time
from colorama import Fore

# Import modules
from config import *
from ui import UIManager
from bugs import BugEngine
from utils import Logger, SystemChecker, TargetValidator

class TelegramBugAttacker:
    def __init__(self):
        self.logger = Logger(LOG_FILE)
        self.ui = UIManager(config)
        self.bug_engine = BugEngine(config)
        self.session_active = True
        
        # Cek dependencies
        missing = SystemChecker.check_dependencies()
        if missing:
            print(f"{Fore.RED}[❌] Missing dependencies: {', '.join(missing)}")
            print(f"{Fore.YELLOW}[+] Install with: pip install {' '.join(missing)}")
            sys.exit(1)
            
        # Cek koneksi
        if not SystemChecker.check_internet():
            print(f"{Fore.RED}[❌] No internet connection!")
            sys.exit(1)
            
        self.logger.log("System initialized successfully", "SUCCESS")
        
    def run(self):
        while self.session_active:
            try:
                # Show UI
                self.ui.show_banner()
                
                # Get menu
                menu = self.bug_engine.get_menu()
                self.ui.show_menu(menu)
                
                # Get user input
                choice = self.ui.get_input("Pilih bug (nomor): ")
                
                if choice == '0':
                    self.session_active = False
                    print(f"{Fore.RED}[💀] KELUAR DARI SYSTEM...")
                    self.logger.log("User exited system", "INFO")
                    break
                    
                if choice in menu:
                    self.bug_engine.execute(choice)
                    self.logger.log(f"Executed bug: {menu[choice]['name']}", "SUCCESS")
                else:
                    self.ui.show_error("Nomor bug gak ada, anj!")
                    
                input(f"\n{Fore.CYAN}[>] Tekan Enter buat lanjut...")
                
            except KeyboardInterrupt:
                print(f"\n{Fore.RED}[💀] SISTEM DIHENTIKAN OLEH BOS!")
                self.logger.log("System interrupted by user", "WARNING")
                break
            except Exception as e:
                self.ui.show_error(str(e))
                self.logger.log(f"Error: {str(e)}", "ERROR")
                
                if AUTO_RESTART:
                    print(f"{Fore.YELLOW}[+] Auto-restarting...")
                    time.sleep(3)
                    continue
                break
                
        print(f"{Fore.RED}[✅] SAMPAI JUMPA BOSS! JANGAN LUPA BAYAR!")
        self.logger.log("System shutdown", "INFO")

if __name__ == "__main__":
    attacker = TelegramBugAttacker()
    attacker.run()
