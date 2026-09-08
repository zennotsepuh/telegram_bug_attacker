# -*- coding: utf-8 -*-
# CONFIGURATION FILE - © DanzModss
# JANGAN DIUTAK-ATIK KALO GAK MAU ERROR ANJING!

import os

# ===== TELEGRAM CONFIG =====
BOT_TOKEN = "8616635222:AAHJ9Z8umuAE_rfW2UCEEB_t-bW1MiJiEXU"  # Ganti punya lu!
API_ID = 39718088  # Ganti pake ID lu
API_HASH = "50336e25ba41a389103a4a93dbe1de94"  # Ganti pake hash lu
OWNER_ID = 7836052754  # ID Telegram lu

# ===== UI CONFIG =====
BANNER_IMAGE = "https://files.catbox.moe/dbzy37.png"  # Ganti link gambar
BANNER_COLOR = "red"  # Warna banner: red, blue, green, yellow, magenta, cyan, white

# ===== BUG CONFIG =====
SPAM_DELAY = 0.01  # Delay spam (detik) - makin kecil makin ganas!
MAX_THREADS = 100  # Max thread buat multi-processing
AUTO_RESTART = True  # Auto restart kalo error

# ===== LOGGING =====
LOG_FILE = "attack_log.txt"
SAVE_LOGS = True

# ===== PROXY CONFIG (OPSIONAL) =====
USE_PROXY = False
PROXY_LIST = [
    "socks5://127.0.0.1:9050",
    "http://127.0.0.1:8080"
]

print("[✅] Config loaded successfully, boss!")
