# PDF-password-cracker
The simple, easy, PDF password cracker

# Usage
The PDF file should be in the current working directory

## Ubuntu/Debian

1. Install dependencies
```
sudo apt install python3 python3-pip git wget
```

2. clone the repository and cd into it
```bash
git clone https://github.com/hirusha-adi/PDF-password-cracker.git
cd ./PDF-password-cracker
```

3. Download a wordlist. below command is to download a wordlist with 10 million passwords
```bash
wget "https://github.com/danielmiessler/SecLists/raw/master/Passwords/xato-net-10-million-passwords-1000000.txt" -o "wordlist.txt"
```

4. Copy your .pdf file to the current working directory

5. Start the script
```bash
python3 main.py
```
