import zipfile
import os
import sys
import time




def x(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()




os.system("clear")
time.sleep(1)
x("\n\t\t\t\033[1;32mConnecting...")
time.sleep(3)
os.system("clear")
time.sleep(1)


print("""\033[1;32m

 _______        _______  _______  _______  _______  _       
/ ___   )      (  ____ \\(  ____ )(  ___  )(  ____ \\| \\    /\\
\\/   )  |      | (    \\/| (    )|| (   ) || (    \\/|  \\  / /
    /   )_____ | |      | (____)|| (___) || |      |  (_/ / 
   /   /(_____)| |      |     __)|  ___  || |      |   _ (  
  /   /        | |      | (\\ (   | (   ) || |      |  ( \\ \\ 
 /   (_/\\      | (____/\\| ) \\ \\__| )   ( || (____/\\|  /  \\ \\
(_______/      (_______/|/   \\__/|/     \\|(_______/|_/    \\/
                                                            
     
\033[1;31m================================================================
    \033[1;34mTools Author: \033[1;33mMohammad Rayhan Khan 
    \033[1;34mVersion     : \033[1;33m1.0
    \033[1;34mTool Name   : \033[1;33mZ-Crack Tool
    \033[1;34mFacebook    : \033[1;33mhttps://www.facebook.com/azad.farabi.2024
    \033[1;34mGithub      : \033[1;33mhttps://github.com/lucifer-fernandez/Z-Crack.git
\033[1;31m================================================================
""")





def main():    
    print("\033[1;36mEnter ZIP file path (e.g., /sdcard/file.zip):\033[0m")
    zip_path = input("\033[1;36m>> \033[1;33m").strip()

    if not os.path.exists(zip_path):
        print("\033[1;31m[!] ZIP file not found!\033[0m")
        sys.exit()

    if not zip_path.endswith(".zip"):
        print("\033[1;31m[-] Only .zip files are supported!\033[0m")
        sys.exit()

    print("\033[1;36mUse default wordlist (passwords.txt)? [y/n]:\033[0m")
    use_default = input("\033[1;36m>> \033[1;33m").strip().lower()

    if use_default == "y":
        wordlist = os.path.join(os.path.dirname(__file__), "passwords.txt")
    else:
        print("\033[1;36mEnter your wordlist path:\033[0m")
        wordlist = input("\033[1;36m>> \033[1;33m").strip()

    if not os.path.exists(wordlist):
        print("\033[1;31m[!] Wordlist not found!\033[0m")
        sys.exit()

    x("\n\t\t\033[1;31m[*] Starting password cracking...\033[0m")
    time.sleep(3)
    start = time.time()

    try:
        zip_file = zipfile.ZipFile(zip_path)
        passwords = open(wordlist, "r", errors="ignore")
        lines = passwords.readlines()
        total = len(lines)
        count = 0

        for line in lines:
            count += 1
            pwd = line.strip()

            try:
                zip_file.extractall(pwd=pwd.encode('utf-8'))
                print(f"\n\033[1;32m[+] Password Found: {pwd}\033[0m")
                break
            except:
                print(f"\033[1;33m[-] Trying ({count}/{total}): {pwd}\033[0m")

        else:
            print("\n\033[1;31m[-] Password not found in wordlist.\033[0m")

        zip_file.close()
        passwords.close()

    except zipfile.BadZipFile:
        print("\033[1;31m[!] Not a valid ZIP file!\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Error: {e}\033[0m")

    end = time.time()
    print(f"\n\033[1;35m[*] Time taken: {end - start:.2f} seconds\033[0m")
    x("\n\n\t\t\t\033[1;31m☯️ System closed.\033[0m\n\n\n")
main()
