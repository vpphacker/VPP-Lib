import os
import time
import sys


def slowprint(s):
    for c in s + '\n' :
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(3. / 100)
slowprint("Installing Packages........................")
os.system("apt install python3 -y")
os.system("apt install screenfetch -y")
os.system("apt install figlet -y")
os.system("apt install ruby -y")
os.system("gem install lolcat")
os.system("clear")
os.system("python3 vpplib.py")
