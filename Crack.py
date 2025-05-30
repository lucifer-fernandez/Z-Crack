#!/usr/bin/env python3
import sys
import os
import time
from termcolor import colored

# ASCII ব্যানার
BANNER = """
\033[1;31m
            ███████   ██  ██████      ██████  ██████    █████   ██████  ██    ██    ███████  ██████   ███████    ██     
               ███    ██  ██   ██      ██      ██   ██   ██  ██   ██      ██   ██        ██     ██    ██  ██    ██   ██    
             ███     ██  ██████       ██      ██████   ███████  ██      █████          ██     ██    ██  ██    ██   ██     
           ███      ██   ██           ██      ██  ██    ██   ██  ██      ██   ██        ██     ██    ██  ██    ██   ██     
          ███████  ██   ██           ██████ ██    ██  ██   ██  ██████ ██     ██      ██     ███████   ███████   ███████
          
                                                                                                           
\033[1;33m                    Created by Rayhan
\033[0m
"""

# ডিফল্ট ওয়ার্ডলিস্ট পাথ (রিপোজিটরিতে থাকবে)
DEFAULT_WORDLIST = os.path.join(os.path.dirname(__file__), "passwords.txt")

def check_requirements():
    """Termux-এ প্রয়োজনীয় টুল চেক করা"""
    required_tools = ["unrar", "7z"]
    missing_tools = []
    for tool in required_tools:
        if os.system(f"which {tool} > /dev/null 2>&1") != 0:
            missing_tools.append(tool)
    if missing_tools:
        print(colored(f"[!] Missing tools: {', '.join(missing_tools)}. Install them using:", "red"))
        print(colored("pkg install unrar p7zip", "yellow"))
        sys.exit(1)
    try:
        import pyzipper, pikepdf, termcolor
    except ImportError as e:
        print(colored(f"[!] Missing Python library: {str(e).split()[-1]}", "red"))
        print(colored("Install it using: pip install pyzipper pikepdf termcolor", "yellow"))
        sys.exit(1)

def get_file_size(file_path):
    """ওয়ার্ডলিস্ট ফাইলের সাইজ গণনা"""
    try:
        return sum(1 for line in open(file_path, "r", errors="ignore"))
    except:
        return 0

def crack_zip(file, wordlist):
    import pyzipper
    total = get_file_size(wordlist)
    with pyzipper.AESZipFile(file) as zf:
        for i, pwd in enumerate(open(wordlist, "r", errors="ignore"), 1):
            try:
                zf.extractall(pwd=pwd.strip().encode())
                print(colored(f"[+] ZIP Password Found: {pwd.strip()}", "green"))
                return True
            except:
                print(colored(f"[-] ZIP Trying ({i}/{total}): {pwd.strip()}", "yellow"))
    print(colored("[-] Password not found in wordlist.", "red"))
    return False

def crack_rar(file, wordlist):
    total = get_file_size(wordlist)
    for i, pwd in enumerate(open(wordlist, "r", errors="ignore"), 1):
        cmd = f'unrar x -p"{pwd.strip()}" "{file}" > /dev/null 2>&1'
        if os.system(cmd) == 0:
            print(colored(f"[+] RAR Password Found: {pwd.strip()}", "green"))
            return True
        else:
            print(colored(f"[-] RAR Trying ({i}/{total}): {pwd.strip()}", "yellow"))
    print(colored("[-] Password not found in wordlist.", "red"))
    return False

def crack_7z(file, wordlist):
    total = get_file_size(wordlist)
    for i, pwd in enumerate(open(wordlist, "r", errors="ignore"), 1):
        cmd = f'7z x -p"{pwd.strip()}" "{file}" -oextracted > /dev/null 2>&1'
        if os.system(cmd) == 0:
            print(colored(f"[+] 7Z Password Found: {pwd.strip()}", "green"))
            return True
        else:
            print(colored(f"[-] 7Z Trying ({i}/{total}): {pwd.strip()}", "yellow"))
    print(colored("[-] Password not found in wordlist.", "red"))
    return False

def crack_pdf(file, wordlist):
    import pikepdf
    total = get_file_size(wordlist)
    for i, pwd in enumerate(open(wordlist, "r", errors="ignore"), 1):
        try:
            pikepdf.open(file, password=pwd.strip())
            print(colored(f"[+] PDF Password Found: {pwd.strip()}", "green"))
            return True
        except:
            print(colored(f"[-] PDF Trying ({i}/{total}): {pwd.strip()}", "yellow"))
    print(colored("[-] Password not found in wordlist.", "red"))
    return False

def main():
    print(BANNER)
    check_requirements()
    
    # ইন্টারেক্টিভ ইনপুট
    print(colored("Enter the path to the file (e.g., /sdcard/file.zip, document.pdf):", "cyan"))
    file = input().strip()
    
    # ফাইল চেক
    if not os.path.exists(file):
        print(colored(f"[!] File not found: {file}", "red"))
        sys.exit(1)
    
    # ওয়ার্ডলিস্ট নির্বাচন
    print(colored("Use default wordlist (passwords.txt)? [y/n]:", "cyan"))
    use_default = input().strip().lower()
    if use_default == 'y':
        wordlist = DEFAULT_WORDLIST
        if not os.path.exists(wordlist):
            print(colored(f"[!] Default wordlist not found: {wordlist}", "red"))
            print(colored("Please provide a custom wordlist.", "yellow"))
            wordlist = input(colored("Enter the path to the wordlist: ", "cyan")).strip()
    else:
        wordlist = input(colored("Enter the path to the wordlist: ", "cyan")).strip()
    
    # ওয়ার্ডলিস্ট চেক
    if not os.path.exists(wordlist):
        print(colored(f"[!] Wordlist not found: {wordlist}", "red"))
        sys.exit(1)

    print(colored(f"[*] Starting password cracking for {file}...", "blue"))
    start_time = time.time()

    # ফাইল টাইপ অনুযায়ী ক্র্যাকিং
    if file.endswith(".zip"):
        crack_zip(file, wordlist)
    elif file.endswith(".rar"):
        crack_rar(file, wordlist)
    elif file.endswith(".7z"):
        crack_7z(file, wordlist)
    elif file.endswith(".pdf"):
        crack_pdf(file, wordlist)
    else:
        print(colored("[-] Unsupported file type! Supported types: .zip, .rar, .7z, .pdf", "red"))
        sys.exit(1)

    print(colored(f"[*] Time taken: {time.time() - start_time:.2f} seconds", "blue"))

if __name__ == "__main__":
    main()
