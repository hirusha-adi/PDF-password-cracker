from random import choice as rand_choice
import os
import platform
import sys

if platform.system().lower().startswith('win'):
    LINUX = True
    PIP = "pip3"
    PYTHON = "python3"
    CLEAR = "cls"
else:
    LINUX = False
    PIP = "pip"
    PYTHON = "python"
    CLEAR = "clear"


def clear_screen():
    os.system(CLEAR)


def pip_install(module_name: str, clear_s: bool = True):
    if clear_s:
        clear_screen()
    os.system(f"""{PIP} install {module_name}""")


try:
    import pikepdf
except ImportError:
    pip_install(module_name="pikepdf", clear_s=True)
    import pikepdf


try:
    from tqdm import tqdm
except ImportError:
    pip_install(module_name="tqdm", clear_s=True)
    from tqdm import tqdm

# Start
print(r"""
 ____  ____  _____                   _
|  _ \|  _ \|  ___|__ _ __ __ _  ___| | __
| |_) | | | | |_ / __| '__/ _` |/ __| |/ /
|  __/| |_| |  _| (__| | | (_| | (__|   <
|_|   |____/|_|  \___|_|  \__,_|\___|_|\_\
PDFcrack - The simple PDF Password Cracker
""")

file_yn = True
if "nf" in sys.argv:
    file_yn = False

if file_yn:
    print("+ Save password: True")
else:
    print("+ Save password: False")


# Selecting the .pdf file
# If more than one .pdf file exists in the current dircetory, the file will be randomly picked!
all_pwd_file = []
for file in os.listdir(os.getcwd()):
    if file.lower().endswith("pdf"):
        all_pwd_file.append(file)

try:
    pdf_filename = rand_choice(all_pwd_file)
except IndexError:
    print("- No .pdf files found in the current directory")
    exit()
except Exception as e:
    print("- Error:", e)

print("+ Selected:", pdf_filename)

if "wordlist.lst" in os.listdir(os.getcwd()):
    word_list = "wordlist.lst"
elif "wordlist.txt" in os.listdir(os.getcwd):
    word_list = "wordlist.txt"
else:
    word_list = input("? Enter the path to the wordlist: ")


# Password
password_list = [line.strip() for line in open("wordlist.lst", "r")]

for password in tqdm(password_list, "Cracking Password"):

    try:
        with pikepdf.open(pdf_filename, password=password) as pdf:
            print("+ Password found:", password)
            with open(f"{pdf_filename}_password.txt", "w", encoding="utf-8") as lgf:
                lgf.write(f"{password}")
            break

    except pikepdf._qpdf.PasswordError:
        continue

    except Exception as e:
        print("- Error:", e)


# BYE
print("!! HAVE A NICE DAY!")
