from nornir import InitNornir 
from nornir.plugins.functions.text import print_result , print_title
from nornir.plugins.tasks.networking import netmiko_send_config
from nornir.plugins.tasks.text import template_file
import subprocess

import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # IOError: Broken pipe
signal.signal(signal.SIGINT, signal.SIG_DFL)  # KeyboardInterrupt: Ctrl-C

StringLenghtMax = 40
key = input('Enter your key path\nPress ENTER to use default path (~/.ssh/id_rsa.pub):') # get pub key 
username = subprocess.run('whoami',shell=True,capture_output=True,text=True).stdout.strip() # get current username

def SplitKey(Cnumber,key) : # Splite PUB kEY INTO PICIES eatch pices with 40 caracter
	a = 0
	text = ''
	KEY  = []
	for i in key :
		a = a + 1
		text = text + i
		if a == Cnumber :
			key = key.replace(text,'')
			KEY.append(text)
			text = ''
			a = 0
	KEY.append(key)

	return KEY

def readkey(keypath): # Read the Key and Remove some shit from it
	with open(keypath) as readkey  :
		key = readkey.readline().strip()
		key = key.replace('ssh-rsa','').strip()
		key = key.split(' ').pop(0)
		key = SplitKey(40,key)
		return key

if not key : 
	key = f'/home/{username}/.ssh/id_rsa.pub'
	KEY = readkey(key)
	
elif key :
	KEY = readkey(key)


nr = InitNornir(config_file="config.yaml")


def play(task):
	LoadJ2Config = task.run(task=template_file,name='Load Config',template='Cisco_cfg.j2',path='./') # Load J2 config
	commands = LoadJ2Config.result.split('\n')
	[commands.append(i) for i in KEY] # append KEY piceis into commands
	commands.append('exit') 
	task.run(task=netmiko_send_config,config_commands=commands,name='send config') # Send Them
print_result(nr.run(task=play,name='Send SSH key'))
