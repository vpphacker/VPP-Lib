import os
import time
import sys

#This Program is Made for pentesting#

#You Dont Become Coder By Changing Cradits#

def menu():

    def slowprint(s):
        for c in s + '\n' :
           sys.stdout.write(c)
           sys.stdout.flush()
           time.sleep(3. / 100)
    os.system("clear")
    os.system("figlet VPP Lib | lolcat")
    print("""\033[94m
+----------------------------------------+
| Coded By VPP Hacker                    |
| Contact Me on Instagram : VPP Hacker   |
| Date : 12/06/2019                      |
| Search In YouTube : VPP Hacker         |
|       [+] www.vpphacker.ml [+]         |
+----------------------------------------+""")
    slowprint("""\033[93m
[01] System Information
[02] Dns Lookup
[03] Whois
[04] Traceroute
[05] GeoIP Lookup
[06] Port Scan
[07] Reverse IP Lookup
[08] Reverse DNS Lookup """)

loop = True


while loop:

    menu()

    print("\033[95m   ")
    what = input("#VPPLib >> ")
    if what == "1":
        os.system("clear")
        os.system("figlet SyS Inform | lolcat")
        print("""\033[92m
+----------------------------------------+
| Coded By VPP Hacker                    |
| Date : 12/06/2019                      |
| Contact Me on Instagram : VPP Hacker   |
| Join Us On Telegram : @VPPHacker       |
| Search In YouTube : VPP Hacker         |
+----------------------------------------+""")
        os.system("screenfetch | lolcat")
        print("\033[96m   ")
        rmenu = input("[#] Back To VPPLib (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break

    elif what == "2":
          os.system("clear")
          os.system("figlet DNS Lookup | lolcat")
          print("""\033[93m
+----------------------------------------+
| Coded By VPP Hacker                    |
| Date : 12/06/2019                      |
| Contact Me on Instagram : VPP Hacker   |
| Join Us On Telegram : @VPPHacker       |
| Search In YouTube : VPP Hacker         |
+----------------------------------------+""")
          print("\033[97m               ")
          vpp = input("#VPP Lib\033[91m Enter Website\033[97m >>  ")
          os.system("curl http://api.hackertarget.com/dnslookup/?q=" + vpp )
          print("\033[95m  ")
          rmenu = input("[#] Back To VPPLib (y/n): ")
          if rmenu == "y":
              menu()
          else:
              break

    elif what == "3":
          os.system("clear")
          os.system("figlet Whois Lookup | lolcat")
          print("""\033[93m
+----------------------------------------+
| Coded By VPP Hacker                    |
| Date : 12/06/2019                      |
| Contact Me on Instagram : VPP Hacker   |
| Join Us On Telegram : @VPPHacker       |
| Search In YouTube : VPP Hacker         |
+----------------------------------------+""")
          print("\033[97m               ")
          vpp = input("#VPP Lib\033[91m Enter Website\033[97m >>  ")
          os.system("curl http://api.hackertarget.com/whois/?q=" + vpp )
          os.system("pwd")
          print("File : Whois.txt" +vpp)
          rmenu = input("[#] Back To VPPLib (y/n): ")
          if rmenu == "y":
              menu()
          else:
              break

    elif what == "4":
          os.system("clear")
          os.system("figlet Traceroute | lolcat")
          print("""\033[93m
+----------------------------------------+
| Coded By VPP Hacker                    |
| Date : 12/06/2019                      |
| Contact Me on Instagram : VPP Hacker   |
| Join Us On Telegram : @VPPHacker       |
| Search In YouTube : VPP Hacker         |
+----------------------------------------+""")
          print("\033[97m       ")
          vpp = input("#VPP Lib\033[91m Enter Website\033[97m >> :")
          os.system("curl http://api.hackertarget.com/mtr/?q=" + vpp )
          rmenu = input("[#] Back To VPPLib (y/n): ")
          if rmenu == "y":
              menu()
          else:
              break

    elif what == "5":
          os.system("clear")
          os.system("figlet GeoIP Lookup | lolcat")
          print("""\033[93m
+----------------------------------------+
| Coded By VPP Hacker                    |
| Date : 12/06/2019                      |
| Contact Me on Instagram : VPP Hacker   |
| Join Us On Telegram : @VPPHacker       |
| Search In YouTube : VPP Hacker         |
+----------------------------------------+""")
          print("\033[97m               ")
          vpp = input("#VPP Lib\033[91m Enter Website\033[97m >> :")
          os.system("curl http://api.hackertarget.com/geoip/?q=" + vpp )
          rmenu = input("[#] Back To VPPLib (y/n): ")
          if rmenu == "y":
              menu()
          else:
              break

    elif what == "6":
          os.system("clear")
          os.system("figlet Port Scan")
          print("""\033[93m
+----------------------------------------+
| Coded By VPP Hacker                    |
| Date : 12/06/2019                      |
| Contact Me on Instagram : VPP Hacker   |
| Join Us On Telegram : @VPPHacker       |
| Search In YouTube : VPP Hacker         |
+----------------------------------------+""")
          print("\033[96m           ")
          vpp = input("#VPP Lib\033[91m Enter Website\033[97m >> :")
          os.system("curl http://api.hackertarget.com/nmap/?q=" + vpp )
          rmenu = input("[#] Back To VPPLib (y/n): ")
          if rmenu == "y":
              menu()
          else:
              break

    elif what == "7":
          os.system("clear")
          os.system("figlet Reverse IP Lookup | lolcat")
          print("""\033[93m
+----------------------------------------+
| Coded By VPP Hacker                    |
| Date : 12/06/2019                      |
| Contact Me on Instagram : VPP Hacker   |
| Join Us On Telegram : @VPPHacker       |
| Search In YouTube : VPP Hacker         |
+----------------------------------------+""")
          vpp = input('Enter IP Or Domain : ')
          os.system("wget http://api.hackertarget.com/reverseiplookup/?q=" + vpp )
          print("")
          print("\033[91m\033[1mFile Saved On : ")
          os.system("pwd")
          print("File : index.html?q=" +d3)
          print("\033[0m")
          rmenu = input("[#] Back To VPPLib (y/n): ")
          if rmenu == "y":
              menu()
          else:
              break
    elif what == "8":
          os.system("clear")
          os.system("figlet ReverseDNS | lolcat")
          print("""\033[93m
+----------------------------------------+
| Coded By VPP Hacker                    |
| Date : 12/06/2019                      |
| Contact Me on Instagram : VPP Hacker   |
| Join Us On Telegram : @VPPHacker       |
| Search In YouTube : VPP Hacker         |
+----------------------------------------+""")
          print("\033[97m               ")
          vpp = input("#VPP Lib\033[91m Enter Website\033[97m >> :")
          os.system("curl https://api.hackertarget.com/reversedns/?q=" + vpp)
          rmenu = input("[#] Back To VPPLib (y/n): ")
          if rmenu == "y":
              menu()
          else:
              break
