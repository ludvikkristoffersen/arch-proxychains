from colorama import *
import os
import subprocess
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--program", required=True, help="Specify what program you want to run with proxychains")
args = parser.parse_args()

# Function for starting and stopping tor and proxychains
def main(program):
    try:
            print(f"\n{Fore.GREEN + '[*]'} {Fore.BLUE + 'Starting TOR service' + Style.RESET_ALL}")
            os.system("sudo systemctl start tor")
            print(f"{Fore.GREEN + '[*]'} {Fore.BLUE + 'Starting proxychains with'} {program}\n" + Style.RESET_ALL)
            os.system(f"nohup proxychains -f /etc/proxychains.conf {program} > /dev/null 2>&1 &")
            kill_process = input(f"""{Fore.RED + '[!]'} {Fore.BLUE + 'Press "q" to quit:' + Style.RESET_ALL} """).lower()
            if kill_process == 'q':
                print(f"\n{Fore.MAGENTA + '[+]'} {Fore.BLUE + 'Killing proxychains process and stopping tor' + Style.RESET_ALL}")
                os.system(f"pkill {program}")
                time.sleep(1)
                os.system("sudo systemctl stop tor")
                time.sleep(1)
                quit()
            else:
                print(Fore.RED + "[!] Invalid input." + Style.RESET_ALL)
    except:
        quit()

# Installing packages if they are not installed
packages = ["proxychains-ng", "tor"]
for package in packages:
    try:
        subprocess.check_output(["pacman", "-Qi", package], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        if e.returncode == 1:
            print(f"{Fore.YELLOW + '[package]' + Style.RESET_ALL} {Fore.RED + package + Style.RESET_ALL} not installed")
            user_install = input(f"Would you like to install '{package}' (y/n): ").lower()
            if user_install == 'y':
                os.system(f"sudo nohup pacman -Sy {package} --noconfirm > /dev/null 2>&1")
            elif user_install == 'n':
                continue
            else:
                print(Fore.RED + "[!] Invalid input" + Style.RESET_ALL)

# Running proxychains for a user specified program
main(args.program)
