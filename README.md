# 🌟 Z-Crack - Unlock Your ZIP Files! 🔓

Welcome to **Z-Crack**, a sleek and powerful Python-based utility crafted by **Rayhan** to help you recover passwords from encrypted ZIP files. Whether you're an ethical hacker, digital forensics expert, or a curious learner — this tool is designed for **you**!
---

## 🚀 Features

✅ **ZIP Password Cracking** – Unlock encrypted ZIP files with ease  
🎨 **Colorful Terminal Banner** – Uses `figlet` and `lolcat` for stylish command-line visuals  
📂 **Built-in Wordlist** – Default `passwords.txt` for quick testing  
📁 **Custom Wordlist Support** – Load your own wordlist for extended cracking  
🖥️ **Interactive CLI** – Simple and intuitive input prompts, Termux-friendly  
📊 **Live Progress Output** – Colored feedback using `termcolor`  
📱 **Mobile Optimized** – Lightweight and ideal for Termux on Android devices

---

## 🎮 Demo Preview

Z-Crack Created by Rayhan

Enter the path to the ZIP file (e.g., /sdcard/file.zip):

> 🔍 Sit back and watch Z-Crack find the password — with real-time colorful output and time taken!

---

## 📦 Installation Guide

Follow these steps to set up Z-Crack Tool in **Termux**:

### 1️⃣ Grant Storage Permission:
```bash
termux-setup-storage
```

## 2️⃣ Update Your System:
```bash
pkg update && pkg upgrade -y
```

## 3️⃣ Install Required Packages:
```bash
pkg install git python figlet lolcat -y
pip install --upgrade pip
pip install pyzipper termcolor
```

## 4️⃣ Clone the Repository:
```bash
git clone https://github.com/lucifer-fernandez/Z-Crack.git
cd Z-Crack
```

## 5️⃣ Make Script Executable:
```bash
chmod +x crack.py
```

---

## ▶️ Usage
```bash
./crack.py
```

Then follow the prompts:

1. Enter the path to your ZIP file (e.g., /sdcard/file.zip)


2. Choose to use default wordlist (passwords.txt) or provide your own


3. Sit back and let the cracking begin!




---

## ⚠️ Disclaimer

> Z-Crack Tool is intended for educational and legal use only.
Using this tool on files you don't own or without permission is illegal and unethical.



Respect privacy, security laws, and use this tool responsibly.


---

## 📜 License

Z-Crack Tool is released under the MIT License.
For more information see the LICENCE file.


---

## 🤝 Contributing

Want to improve the tool? Found a bug?
Feel free to fork, star, and pull request! Contributions are highly appreciated.


---

## 🙌 Acknowledgements

Rayhan – Creator & Developer

figlet + lolcat – For beautiful banners

pyzipper + termcolor – For core functionality



---

## 🌐 Support

For queries, suggestions, or collaboration:

📬 Email: rayhankhan4u@gmail.com
📁 GitHub Issues: Submit a bug or feature request


---

> 🔐 Happy cracking — and always stay ethical!
