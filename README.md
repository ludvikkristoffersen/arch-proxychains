Keep in mind this script is for **Arch users only**. This little Python script downloads TOR and Proxychains if the user does not have these packages allready installed. It really do not do anything special, it just starts TOR for you and runs Proxychains with your specified program.

## Installation
Download the repo:
```bash
git clone https://github.com/luddekn/arch-proxychains
```
Download the script requirements:
```bash
pip3 install -r requirements.txt
```
## Usage example
```bash
python3 proxychains.py -p firefox
```
```bash
python3 proxychains.py --program firefox
```
