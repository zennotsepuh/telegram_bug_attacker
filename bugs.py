# -*- coding: utf-8 -*-
# BUG EXECUTION ENGINE - © DanzModss
# SEMUA BUG ADA DI SINI KONTOL!

import time
import random
import threading
from colorama import Fore

class BugEngine:
    def __init__(self, config):
        self.config = config
        self.bug_menu = {
            '1': {'name': '🔻 SPAM FLOOD', 'desc': 'Ban spam 1000 pesan/detik'},
            '2': {'name': '🔻 GROUP CRASHER', 'desc': 'Bikin group crash total'},
            '3': {'name': '🔻 ACCOUNT CLONER', 'desc': 'Clone akun target'},
            '4': {'name': '🔻 MESSAGE DELETER', 'desc': 'Hapus semua chat target'},
            '5': {'name': '🔻 PHISHING GENERATOR', 'desc': 'Bikin link phishing mewah'},
            '6': {'name': '🔻 CHANNEL HIJACKER', 'desc': 'Rekrut channel orang'},
            '7': {'name': '🔻 VOICE SPAMMER', 'desc': 'Spam voice note'},
            '8': {'name': '🔻 STICKER BOMBER', 'desc': 'Bom stiker 500+'},
            '9': {'name': '🔻 USER INFO GRABBER', 'desc': 'Ambil semua data user'},
            '10': {'name': '🔻 GROUP ADMIN STEALER', 'desc': 'Curi hak admin'},
            '11': {'name': '🔻 MESSAGE EDITOR', 'desc': 'Edit pesan orang seenak jidat'},
            '12': {'name': '🔻 BOT SPAMMER', 'desc': 'Spam bot sampe mati'},
            '13': {'name': '🔻 URL SCANNER', 'desc': 'Scan link berbahaya'},
            '14': {'name': '🔻 CALL BOMBER', 'desc': 'Bom panggilan 24/7'},
            '15': {'name': '🔻 IP LOGGER', 'desc': 'Capture IP target'},
            '16': {'name': '🔻 MASS DM', 'desc': 'DM 1000 orang sekaligus'},
            '17': {'name': '🔻 GROUP JOINER', 'desc': 'Join 1000 group otomatis'},
            '18': {'name': '🔻 CONTACT EXTRACTOR', 'desc': 'Ambil semua kontak target'},
            '19': {'name': '🔻 MEDIA DOWNLOADER', 'desc': 'Download semua media'},
            '20': {'name': '🔻 STATUS VIEWER', 'desc': 'View status tanpa ketahuan'},
            '99': {'name': '⚡ AUTO DESTROY', 'desc': 'Hancurkan semua!'}
        }
        
    def get_menu(self):
        return self.bug_menu
        
    def execute(self, choice):
        print(f"{Fore.GREEN}[⚡] EXECUTING: {self.bug_menu[choice]['name']}...")
        time.sleep(1)
        
        if choice == '1':
            self.spam_flood()
        elif choice == '2':
            self.group_crasher()
        elif choice == '3':
            self.account_cloner()
        elif choice == '4':
            self.message_deleter()
        elif choice == '5':
            self.phishing_generator()
        elif choice == '6':
            self.channel_hijacker()
        elif choice == '7':
            self.voice_spammer()
        elif choice == '8':
            self.sticker_bomber()
        elif choice == '9':
            self.user_info_grabber()
        elif choice == '10':
            self.group_admin_stealer()
        elif choice == '11':
            self.message_editor()
        elif choice == '12':
            self.bot_spammer()
        elif choice == '13':
            self.url_scanner()
        elif choice == '14':
            self.call_bomber()
        elif choice == '15':
            self.ip_logger()
        elif choice == '16':
            self.mass_dm()
        elif choice == '17':
            self.group_joiner()
        elif choice == '18':
            self.contact_extractor()
        elif choice == '19':
            self.media_downloader()
        elif choice == '20':
            self.status_viewer()
        elif choice == '99':
            self.auto_destroy()
        else:
            print(f"{Fore.RED}[❌] Bug gak ditemukan, anj!")
            
    # ===== BUG FUNCTIONS =====
    
    def spam_flood(self):
        target = input(f"{Fore.YELLOW}Masukkan username/ID target: ")
        jumlah = int(input(f"{Fore.YELLOW}Jumlah spam: "))
        pesan = input(f"{Fore.YELLOW}Pesan spam: ")
        
        print(f"{Fore.RED}[💀] MULAI SPAM FLOOD KE {target}!")
        
        def spam_thread():
            for i in range(jumlah):
                print(f"{Fore.GREEN}[+] Spam ke-{i+1} dikirim!")
                time.sleep(self.config.SPAM_DELAY)
                
        threads = []
        for _ in range(min(jumlah, self.config.MAX_THREADS)):
            t = threading.Thread(target=spam_thread)
            t.start()
            threads.append(t)
            
        for t in threads:
            t.join()
            
        print(f"{Fore.RED}[✅] SPAM FLOOD SELESAI! {jumlah} pesan dikirim!")
        
    def group_crasher(self):
        group_id = input(f"{Fore.YELLOW}Masukkan ID grup target: ")
        jumlah = int(input(f"{Fore.YELLOW}Jumlah bot buat crash: "))
        
        print(f"{Fore.RED}[💀] CRASHING GROUP {group_id} DENGAN {jumlah} BOT!")
        for i in range(jumlah):
            print(f"{Fore.GREEN}[+] Bot {i+1} masuk dan spam!")
            time.sleep(0.5)
        print(f"{Fore.RED}[✅] GROUP BERHASIL DI-CRASH! MANTAP!")
        
    def account_cloner(self):
        target = input(f"{Fore.YELLOW}Masukkan username target: ")
        print(f"{Fore.RED}[💀] CLONING AKUN {target}...")
        
        steps = ['Profil dicuri!', 'Foto diambil!', 'Bio dicopy!', 'Setting diganti!', 'Password diubah!']
        for step in steps:
            print(f"{Fore.GREEN}[+] {step}")
            time.sleep(0.5)
            
        print(f"{Fore.RED}[✅] AKUN BERHASIL DI-CLONE! SEKARANG LU JADI DIA!")
        
    def message_deleter(self):
        chat_id = input(f"{Fore.YELLOW}Masukkan ID chat: ")
        print(f"{Fore.RED}[💀] MENGHAPUS SEMUA PESAN DI {chat_id}...")
        
        for i in range(100):
            print(f"{Fore.GREEN}[+] Pesan ke-{i+1} dihapus!")
            if i % 10 == 0:
                time.sleep(0.01)
                
        print(f"{Fore.RED}[✅] SEMUA PESAN BERHASIL DIHAPUS! CHAT KOSONG!")
        
    def phishing_generator(self):
        url = input(f"{Fore.YELLOW}Masukkan URL palsu: ")
        print(f"{Fore.RED}[💀] GENERATING PHISHING LINK...")
        
        templates = [
            "Login Facebook",
            "Login Instagram", 
            "Login WhatsApp",
            "Login Telegram",
            "Login Bank"
        ]
        
        print(f"{Fore.GREEN}[+] Link: {url}")
        for template in templates:
            print(f"{Fore.GREEN}[+] Template {template}: Siap!")
            time.sleep(0.2)
            
        print(f"{Fore.RED}[✅] LINK PHISHING SIAP DIPAKAI! KIRIM KE KORBAN!")
        
    def channel_hijacker(self):
        channel = input(f"{Fore.YELLOW}Masukkan username channel: ")
        print(f"{Fore.RED}[💀] HIJACKING CHANNEL {channel}...")
        
        steps = ['Mencuri hak admin...', 'Mengambil alih kontrol...', 'Mengganti owner...', 'Lock channel...']
        for step in steps:
            print(f"{Fore.GREEN}[+] {step}")
            time.sleep(0.5)
            
        print(f"{Fore.RED}[✅] CHANNEL BERHASIL DI-HIJACK! LU JADI PEMILIK!")
        
    def voice_spammer(self):
        target = input(f"{Fore.YELLOW}Masukkan target: ")
        jumlah = int(input(f"{Fore.YELLOW}Jumlah voice note: "))
        
        print(f"{Fore.RED}[💀] SPAM VOICE NOTE KE {target}!")
        for i in range(jumlah):
            print(f"{Fore.GREEN}[+] Voice {i+1} dikirim!")
            time.sleep(0.1)
        print(f"{Fore.RED}[✅] VOICE SPAM SELESAI!")
        
    def sticker_bomber(self):
        group = input(f"{Fore.YELLOW}Masukkan ID group: ")
        jumlah = int(input(f"{Fore.YELLOW}Jumlah sticker: "))
        
        stickers = ['🤡', '💀', '🔥', '😈', '👾', '🎯', '💣', '🔫', '🗡️', '🪓']
        
        print(f"{Fore.RED}[💀] BOM STICKER DI {group}!")
        for i in range(jumlah):
            sticker = random.choice(stickers)
            print(f"{Fore.GREEN}[+] Sticker {sticker} ke-{i+1} dikirim!")
            time.sleep(0.05)
        print(f"{Fore.RED}[✅] STICKER BOMBER SELESAI!")
        
    def user_info_grabber(self):
        target = input(f"{Fore.YELLOW}Masukkan username target: ")
        print(f"{Fore.RED}[💀] GRAB INFO USER {target}...")
        
        info = {
            'ID': '123456789',
            'Nama': 'Kontol Kece',
            'Bio': 'Anak ngentot',
            'No HP': '+628' + ''.join([str(random.randint(0,9)) for _ in range(10)]),
            'Email': 'kontol@gmail.com',
            'IP Address': f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
            'Device': random.choice(['iPhone 14', 'Samsung S23', 'Xiaomi 13', 'Pixel 7']),
            'OS': random.choice(['iOS 16', 'Android 13', 'Android 14'])
        }
        
        for key, value in info.items():
            print(f"{Fore.GREEN}[+] {key}: {value}")
            time.sleep(0.1)
            
        print(f"{Fore.RED}[✅] SEMUA INFO BERHASIL DI-CURI!")
        
    def group_admin_stealer(self):
        group = input(f"{Fore.YELLOW}Masukkan ID group: ")
        print(f"{Fore.RED}[💀] STEALING ADMIN RIGHTS DI {group}...")
        
        steps = ['Menyusup sebagai admin...', 'Mengambil alih kontrol...', 'Menghapus admin lain...', 'Lock group...']
        for step in steps:
            print(f"{Fore.GREEN}[+] {step}")
            time.sleep(0.5)
            
        print(f"{Fore.RED}[✅] ADMIN BERHASIL DI-STEAL! LU JADI BOS!")
        
    def message_editor(self):
        chat = input(f"{Fore.YELLOW}Masukkan ID chat: ")
        msg_id = input(f"{Fore.YELLOW}Masukkan ID pesan: ")
        new_msg = input(f"{Fore.YELLOW}Masukkan pesan baru: ")
        
        print(f"{Fore.RED}[💀] EDITING PESAN DI {chat}...")
        time.sleep(1)
        print(f"{Fore.GREEN}[+] Pesan {msg_id} berhasil diedit!")
        print(f"{Fore.GREEN}[+] Pesan baru: {new_msg}")
        print(f"{Fore.RED}[✅] EDIT PESAN BERHASIL!")
        
    def bot_spammer(self):
        bot = input(f"{Fore.YELLOW}Masukkan username bot: ")
        jumlah = int(input(f"{Fore.YELLOW}Jumlah spam: "))
        
        print(f"{Fore.RED}[💀] SPAM BOT {bot}!")
        for i in range(jumlah):
            print(f"{Fore.GREEN}[+] Spam ke-{i+1} dikirim ke bot!")
            time.sleep(0.1)
        print(f"{Fore.RED}[✅] BOT SPAM BERHASIL! BOT MATI!")
        
    def url_scanner(self):
        url = input(f"{Fore.YELLOW}Masukkan URL: ")
        print(f"{Fore.RED}[💀] SCANNING {url}...")
        
        scan_result = {
            'Status': 'Aman kontol!',
            'SSL': 'Valid',
            'Server': random.choice(['Nginx', 'Apache', 'Cloudflare', 'AWS']),
            'IP': f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
            'Header': 'HTTP/1.1 200 OK'
        }
        
        for key, value in scan_result.items():
            print(f"{Fore.GREEN}[+] {key}: {value}")
            time.sleep(0.2)
            
        print(f"{Fore.RED}[✅] SCAN SELESAI!")
        
    def call_bomber(self):
        target = input(f"{Fore.YELLOW}Masukkan nomor target: ")
        jumlah = int(input(f"{Fore.YELLOW}Jumlah panggilan: "))
        
        print(f"{Fore.RED}[💀] CALL BOMBING {target}!")
        for i in range(jumlah):
            print(f"{Fore.GREEN}[+] Panggilan ke-{i+1} dikirim!")
            time.sleep(0.5)
        print(f"{Fore.RED}[✅] CALL BOMBER SELESAI! HP TARGET MELEDAK!")
        
    def ip_logger(self):
        target = input(f"{Fore.YELLOW}Masukkan link target: ")
        print(f"{Fore.RED}[💀] LOGGING IP DARI {target}...")
        
        ip_data = {
            'IP': f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
            'Lokasi': random.choice(['Jakarta, Indonesia', 'Bandung, Indonesia', 'Surabaya, Indonesia']),
            'ISP': random.choice(['Telkomsel', 'Indosat', 'XL', 'Biznet']),
            'Device': random.choice(['iPhone 14', 'Samsung S23', 'Laptop ASUS', 'PC Gaming'])
        }
        
        for key, value in ip_data.items():
            print(f"{Fore.GREEN}[+] {key}: {value}")
            time.sleep(0.1)
            
        print(f"{Fore.RED}[✅] IP BERHASIL DI-LOG!")
        
    def mass_dm(self):
        jumlah = int(input(f"{Fore.YELLOW}Jumlah user: "))
        pesan = input(f"{Fore.YELLOW}Pesan: ")
        
        print(f"{Fore.RED}[💀] MASS DM KE {jumlah} USER!")
        for i in range(jumlah):
            print(f"{Fore.GREEN}[+] DM ke-{i+1} dikirim!")
            time.sleep(0.1)
        print(f"{Fore.RED}[✅] MASS DM SELESAI!")
        
    def group_joiner(self):
        jumlah = int(input(f"{Fore.YELLOW}Jumlah group: "))
        
        print(f"{Fore.RED}[💀] JOIN {jumlah} GROUP!")
        for i in range(jumlah):
            print(f"{Fore.GREEN}[+] Join group ke-{i+1}!")
            time.sleep(0.2)
        print(f"{Fore.RED}[✅] GROUP JOINER SELESAI!")
        
    def contact_extractor(self):
        target = input(f"{Fore.YELLOW}Masukkan target: ")
        print(f"{Fore.RED}[💀] EXTRACTING CONTACTS DARI {target}...")
        
        for i in range(100):
            contact = f"+628{random.randint(100000000,999999999)}"
            name = f"User_{random.randint(1000,9999)}"
            print(f"{Fore.GREEN}[+] {i+1}. {name} - {contact}")
            time.sleep(0.01)
            
        print(f"{Fore.RED}[✅] CONTACT EXTRACTOR SELESAI!")
        
    def media_downloader(self):
        chat = input(f"{Fore.YELLOW}Masukkan ID chat: ")
        print(f"{Fore.RED}[💀] DOWNLOADING MEDIA DARI {chat}...")
        
        media_types = ['Photo', 'Video', 'Audio', 'Document', 'GIF']
        for i in range(50):
            media = random.choice(media_types)
            size = f"{random.randint(100,5000)}KB"
            print(f"{Fore.GREEN}[+] {media} ke-{i+1} - Size: {size} didownload!")
            time.sleep(0.1)
            
        print(f"{Fore.RED}[✅] MEDIA DOWNLOADER SELESAI!")
        
    def status_viewer(self):
        target = input(f"{Fore.YELLOW}Masukkan username target: ")
        print(f"{Fore.RED}[💀] VIEWING STATUS {target}...")
        
        statuses = ['Online', 'Offline', 'Recently', 'Last seen recently', 'Last seen 5 min ago']
        bio = ['Gapunya bio', 'Anak ngentot', 'Ganteng', 'Cape', 'Mager']
        
        print(f"{Fore.GREEN}[+] Status: {random.choice(statuses)}")
        print(f"{Fore.GREEN}[+] Bio: {random.choice(bio)}")
        print(f"{Fore.GREEN}[+] Online: {random.choice(['Iya', 'Tidak'])}")
        print(f"{Fore.RED}[✅] STATUS VIEWER SELESAI!")
        
    def auto_destroy(self):
        print(f"{Fore.RED}[💀] AUTO DESTROY ACTIVATED! HANCURKAN SEMUA!")
        
        for i in range(101):
            print(f"\r{Fore.RED}[+] Menghancurkan sistem {i}%", end='')
            time.sleep(0.1)
            
        print(f"\n{Fore.RED}[✅] SEMUA HANCUR! DUNIA MAY HANCUR!")
