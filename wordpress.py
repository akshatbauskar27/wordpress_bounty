#!/usr/bin/python3

import urllib.request
import os
import subprocess
import sys
import pdb
import sublist3r
from datetime import date

def banner():
	print ("""
		 _____ __     _  _     ____  _____     ____   ____  _____  ____  _     _  _____  ____
		|   __|\ \   | || |   |  __||  _  |   |    \ |  __||  ___||  __|| \   | ||   __||  __|
		|  |    \ \__| || |__ | |__ | |_| |   |  _  || |__ | |__  | |__ |  \  | ||  |   | |__
		|  |     \___| || '_ ||  __||  _  \   | |_| ||  __||  __| |  __||   \ | ||  |   |  __|
		|  |__   ____| || |_||| |__ | | |  |  |     || |__ |  |   | |__ | |\ \| ||  |__ | |__
                |_____| |______||_.__||____||_| |__|  |____/ |____||__|   |____||_| \___||_____||____|

					"All rights are resiverd to cyber-defence"
				WARNING:- Do not replicate or use without written permission,
					if done owner will have no responsiblities, and a legal
						 action would be taken!!

		""")


def subdomain(filename,command):
	f= open(filename,'r')
	lines = f.readlines()
	for a in lines:
		a = a.rstrip()
		print (a)
		cmd = command + '/subdomain.txt'
		print (cmd)
#		domain= subprocess.call(cmd, shell=True)
		subdomains = sublist3r.main(a, 40, cmd, ports= None, silent=True, verbose= False, enable_bruteforce= False, engines=None)

def active(command):
	changedir = command+'/subdomain.txt'
	g= open(changedir,'r')
	lines = g.readlines()
	for b in lines:
		d = "http://"+b.rstrip()
		req = urllib.request.Request(d)
#			print (type(b))
		try:
			c=urllib.request.urlopen(d)
			if  c.code == 200:
				cmd1= "echo {} >> {}/active.txt".format(d,command)
#				cmd1= "echo {b} >> {command}/active.txt"
#				cmd1 = "echo" + " " +  b + " " + ">>" + " " +  command + "/active.txt"
#				cmd1 = 'echo' +' ' +  b +'>>' + command + '/active.txt'
#				print (cmd1)
				do = subprocess.call (cmd1, shell = True)
				print (c.code)
#				print (c.read())
				print('===========')

		except urllib.error.URLError  as e:
#				print (e)
#				print("Failed to open URL {0}".format(d))
			print('===========')

		z = "https://"+b.rstrip()
		req = urllib.request.Request(z)
		try:
			w=urllib.request.urlopen(z)
			if  w.code == 200:
				cmd2= "echo {} >> {}/active.txt".format(z,command)
#				print (cmd2)
				do = subprocess.call (cmd2, shell = True)
				print (w.code)
#                               print (c.read())
				print('===========')

		except urllib.error.URLError  as o:
			print ('===========')


def wordpress(command):
	changedir1 = command + '/active.txt'
	h = open(changedir1,'r')
	lines1 = h.readlines()
	for l in lines1:
		l = l.rstrip()
		cmd2 = "wpscan --url" + " " + l + " " +"--no-banner"
		do1 = subprocess.Popen(cmd2,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
		std_out, std_error = do1.communicate()
		print (std_out)
		file1 = input("enter y to save")
		if file1 == "y":
			file = input ("Enter report name")
			cmd3 = command + "/" + file
			with open(cmd3, 'ab+') as out:
				out.write(std_out)
		else:
                       print ("last report not saved for {}".format(l))
                       continue

#		file = input("Y to Save report")
#		if file == 'y' or 'Y' :
#			for t in do1.readlines():
#				file1 = input ("Enter report name")
#				cmd3 = "echo {} >> {}/{}".format(t,command,file1)
#				do1 = subprocess.call (cmd3, shell = True)
#		else:
#			print ("last report not saved for {}".format(l))
#			continue

def main():

	dir = input("enter the new dir name:-")
	today = date.today()
	command = '/home/kali/Desktop/python/bugbounty/' + dir +  str(today)
	command1 = 'mkdir' + ' ' + command
#	command2 = 'cd' + ' ' + command
#	print (command2)
	directory = subprocess.Popen(command1, shell = True)
#	changedir = subprocess.call(command2, shell = True)
#	ls = subprocess.call ('pwd', shell=True)
	banner()
	subdomain(sys.argv[1],command)
	active (command)
	wordpress (command)

if __name__ == "__main__":
    main()
