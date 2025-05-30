#!/usr/bin/env python3
import sys
import os
import time
from termcolor import colored

# ব্যানার তৈরি করা (figlet এবং lolcat ব্যবহার)
def display_banner():
    try:
        # Z-Crack Tool বড় আকারে
        os.system("figlet 'Z-Crack Tool' | lolcat")
        # Created by Rayhan ছোট ফন্টে (mini)
        os.system("figlet -f mini 'Created by Rayhan' | lolcat")
        # চিকন লম্বা লাইন
        print(colored("-" * 60, "white"))
    except Exception as e:
        print(colored("[!] Error displaying banner. Ensure figlet and lolcat are installed using 'pkg install figlet lolcat'.", "red"))
        print(colored("Falling back to plain text:", "yellow"))
        print("Z-Crack Tool")
        print("Created by Rayhan")
        print("-" * 60)

# ডিফল্ট ওয়ার্ডলিস্ট পাথ (রিপোজিটরিতে থাকবে)
DEFAULT_WORDLIST = os.path.join(os.path.dirname(__file__), "passwords.txt")

def check_requirements():
    """Termux-এ প্রয়োজনীয় প্যাকেজ চেক করা"""
    try:
        import pyzipper, termcolor
    except ImportError as e:
        print(colored(f"[!] Missing Python library: {str(e).split()[-1]}", "red"))
        print(colored("Install it using: pip install pyzipper termcolor", "yellow"))
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

def main():
    display_banner()
    check_requirements()
    
    # ইন্টারেক্টিভ ইনপুট (নিচে সরানো)
    print("\n" * 2)  # দুটি নতুন লাইন যোগ করে নিচে সরানো
    print(colored("Enter the path to the ZIP file (e.g., /sdcard/file.zip):", "cyan"))
    file = input().strip()
    
    # ফাইল চেক
    if not os.path.exists(file):
        print(colored(f"[!] File not found: {file}", "red"))
        sys.exit(1)
    
    # ফাইল টাইপ চেক
    if not file.endswith(".zip"):
        print(colored("[-] Unsupported file type! Only .zip files are supported.", "red"))
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

    # ZIP ফাইল ক্র্যাকিং
    crack_zip(file, wordlist)

    print(colored(f"[*] Time taken: {time.time() - start_time:.2f} seconds", "blue"))

if __name__ == "__main__":
    main()
