Keep in mind this script is for **Arch users only**. This little Python script downloads TOR and Proxychains if the user does not have these packages allready installed. It really do not do anything special, it just starts TOR for you and runs Proxychains with your specified program.

## Recommendation
I recommend going into your /etc/proxychains.conf file and changing the mode from strict to dynamic, at the bottom of your config file you can also change from socks4 to socks5
```bash
sudo nano /etc/proxychains.conf
```
## Installation
Download the repo:
```bash
git clone https://github.com/luddekn/arch-proxychains
```
Download colorama:
```bash
sudo pacman -Sy python-colorama
```
## Usage example
```bash
python3 proxychains.py -p firefox
```
```bash
python3 proxychains.py --program firefox
```
