# -*- coding: utf-8 -*-
# UTILITY FUNCTIONS - © DanzModss
# FUNGSI BANTUAN BUAT SCRIPT INI

import os
import sys
import time
import json
import random
import string
from datetime import datetime
from colorama import Fore

class Logger:
    def __init__(self, log_file="attack_log.txt"):
        self.log_file = log_file
        
    def log(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        
        # Print to console
        if level == "ERROR":
            print(f"{Fore.RED}{log_entry}")
        elif level == "SUCCESS":
            print(f"{Fore.GREEN}{log_entry}")
        elif level == "WARNING":
            print(f"{Fore.YELLOW}{log_entry}")
        else:
            print(f"{Fore.CYAN}{log_entry}")
            
        # Save to file
        with open(self.log_file, "a", encoding='utf-8') as f:
            f.write(log_entry)
            
    def save(self, data, filename="attack_data.json"):
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
    def load(self, filename="attack_data.json"):
        try:
            with open(filename, "r", encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
            
class TargetValidator:
    @staticmethod
    def validate_telegram_id(id_str):
        """Validasi ID Telegram"""
        try:
            return int(id_str)
        except:
            return None
            
    @staticmethod
    def validate_username(username):
        """Validasi username Telegram"""
        if username.startswith('@'):
            username = username[1:]
        if username and len(username) >= 5:
            return username
        return None
            
    @staticmethod
    def validate_phone(phone):
        """Validasi nomor HP"""
        import re
        pattern = r'^\+?[0-9]{10,15}$'
        if re.match(pattern, phone):
            return phone
        return None
            
    @staticmethod
    def validate_url(url):
        """Validasi URL"""
        import re
        pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
        if re.match(pattern, url):
            return url
        return None

class PayloadGenerator:
    @staticmethod
    def generate_random_text(length=100):
        """Generate random text buat spam"""
        return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))
        
    @staticmethod
    def generate_username():
        """Generate random username"""
        prefix = random.choice(['user', 'hacker', 'anon', 'ghost', 'dark'])
        suffix = ''.join(random.choices(string.digits, k=4))
        return f"{prefix}_{suffix}"
        
    @staticmethod
    def generate_phishing_template(template_type="login"):
        """Generate template phishing"""
        templates = {
            "login": "Login your account here: {}",
            "verify": "Verify your account: {}",
            "update": "Update your password: {}",
            "secure": "Secure your account: {}"
        }
        return templates.get(template_type, "Click here: {}")
        
    @staticmethod
    def generate_sticker_bomb():
        """Generate sticker bomb"""
        stickers = ['💀', '🔥', '😈', '👾', '🎯', '💣', '🔫', '🗡️', '🪓', '💩', '🤡', '👹']
        return random.choices(stickers, k=random.randint(5, 20))
        
class SystemChecker:
    @staticmethod
    def check_internet():
        """Check koneksi internet"""
        try:
            import requests
            requests.get('https://www.google.com', timeout=5)
            return True
        except:
            return False
            
    @staticmethod
    def check_telegram_connection(api_id, api_hash):
        """Check koneksi ke Telegram"""
        try:
            from telethon import TelegramClient
            client = TelegramClient('temp', api_id, api_hash)
            client.connect()
            client.disconnect()
            return True
        except:
            return False
            
    @staticmethod
    def check_dependencies():
        """Check dependencies"""
        required = ['telethon', 'colorama', 'requests']
        missing = []
        
        for package in required:
            try:
                __import__(package)
            except:
                missing.append(package)
                
        return missing
        
    @staticmethod
    def get_system_info():
        """Dapatkan info sistem"""
        import platform
        info = {
            'OS': platform.system(),
            'OS Version': platform.version(),
            'Architecture': platform.machine(),
            'Python Version': sys.version,
            'CPU Cores': os.cpu_count(),
            'Memory Available': 'N/A'
        }
        return info
        
class Encryptor:
    @staticmethod
    def simple_encrypt(text, key=42):
        """Encrypt sederhana"""
        result = []
        for char in text:
            result.append(chr(ord(char) + key))
        return ''.join(result)
        
    @staticmethod
    def simple_decrypt(encrypted_text, key=42):
        """Decrypt sederhana"""
        result = []
        for char in encrypted_text:
            result.append(chr(ord(char) - key))
        return ''.join(result)
        
    @staticmethod
    def base64_encode(text):
        """Base64 encode"""
        import base64
        return base64.b64encode(text.encode()).decode()
        
    @staticmethod
    def base64_decode(encoded_text):
        """Base64 decode"""
        import base64
        return base64.b64decode(encoded_text).decode()
