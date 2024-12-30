import time
import random
import os
from colorama import Fore, Style

# ล้างหน้าจอ
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ฟังก์ชันแสดงข้อความปลอมแบบสุ่ม
def fake_hacking_effect():
    messages = [
        "[!] Accessing secure files...",
        "[!] Downloading sensitive data...",
        "[!] Uploading malware...",
        "[!] Encrypting files...",
        "[!] System breach detected...",
        "[!] Initiating fake shutdown..."  # ข้อความหลอก
    ]
    for _ in range(100):  # จำนวนรอบที่จะแสดง
        print(Fore.GREEN + random.choice(messages) + Style.RESET_ALL)
        time.sleep(0.05)  # ช้าลงเพื่อให้ดูสมจริง

# ฟังก์ชันสร้างหรือแก้ไขไฟล์ข้อความบนเดสก์ท็อป
def create_or_update_text_file():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    file_path = os.path.join(desktop, "Happy_New_2025.txt")

    if os.path.exists(file_path):
        # หากไฟล์มีอยู่แล้ว ให้แก้ไขข้อความ
        with open(file_path, "w") as file:
            file.write("Happy New Computer")
    else:
        # หากไฟล์ไม่มีอยู่ ให้สร้างใหม่
        with open(file_path, "w") as file:
            file.write("Happy New 2025")

# ฟังก์ชันแสดงหน้าจอ "ถูกแฮ็ก"
def hacked_screen():
    clear_screen()
    print(Fore.GREEN + "=" * 50)
    print("!!! SYSTEM HACKED !!!".center(50))
    print("=" * 50 + Style.RESET_ALL)
    time.sleep(2)  # รอ 2 วินาที
    fake_hacking_effect()
    create_or_update_text_file()
    print(Fore.GREEN + "\n!!! Just Kidding :) !!!")
    print("Your system is safe. Have a nice day!" + Style.RESET_ALL)
    time.sleep(3)

# เริ่มโปรแกรม
if __name__ == "__main__":
    hacked_screen()
