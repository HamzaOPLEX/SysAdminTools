from getpass import getpass
from netmiko import ConnectHandler
import sys
import notify2
import os
import logging
from time import sleep

import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # IOError: Broken pipe
signal.signal(signal.SIGINT, signal.SIG_DFL)  # KeyboardInterrupt: Ctrl-C


username = input('Enter Username :')
sshpassword = getpass('enter ssh password : ')
enablepassword = getpass('enter enable password : ')

logging.basicConfig(level=logging.WARNING, filemode='a',
                    filename='SSHMONITOR.log', format='%(asctime)s - %(message)s')

devices = {'device_type': 'cisco_ios', 'host': '172.16.100',
           'username': username, 'password': sshpassword, 'secret': enablepassword
           }


Trusted_IPS = ['172.16.0.1']

print('[!] waiting ssh connection')
try:
    connection = ConnectHandler(**devices)
    connection.enable()
    print('[+] ssh connection complet')
    print('[+] start Lestning for any inkown SSH Client')
except Exception as err:
    print('[!] we could not connect because :\n', err)
    sys.exit()



NOTTRUSTEDCLIENTS = []

while True:

    sshclients = connection.send_command('sh tcp brief | i ESTAB')
    sshclientconn = sshclients.split('\n')
    for client in sshclientconn:
        TCPCONNECTION = [i for i in client.split(' ') if i]
        CONNECTEDCLIENT = os.path.splitext(TCPCONNECTION[2])[0]
        if CONNECTEDCLIENT not in Trusted_IPS and CONNECTEDCLIENT not in NOTTRUSTEDCLIENTS:
            NOTTRUSTEDCLIENTS.append(CONNECTEDCLIENT)
            Logmsg = f'{CONNECTEDCLIENT} has Connect to your Router'
            logging.warning(Logmsg)
            notify2.init('NEW SSH CLINT DETECTED')
            n = notify2.Notification("NOTICE",
                                     f"{CONNECTEDCLIENT} Has Connect to your router",
                                     )
            n.show()

    sleep(30)
