from pexpect import pxssh
from time import sleep


                            #This code was made in Python 3.7 
                            #coded by HamzaOPLEX 
                            #Facebook : facebook.com/Hamza0plex
                            #Youtube : https://www.youtube.com/channel/UCbeSJJWGNppv5decBIjsfuw
                            #github : github.com/HamzaOPLEX


# HOSTNAME : [HOSTIP,SSH_USERNAME,SSH_PASSWORD,ENABEL_PASSWORD]

Devices = {'R1':['172.16.0.10','Admin','Admin','EnAdmin'],'R2':['172.16.0.11','Admin','Admin','EnAdmin']}

TFTP_SERVER = '172.16.0.9' # TFTP Server IP

for dev in Devices.keys() :
    child = pxssh.pxssh(timeout=1)    
    Routername = dev
    RouterExpectname = f'{Routername}.*'
    IPADDR = Devices[Routername][0]
    SSH_Username = Devices[Routername][1]
    SSH_Passwd = Devices[Routername][2]
    Enabel_Passwd = Devices[Routername][3]

    print(f'[!] Waiting SSH Connection to {Routername}::{IPADDR}')
    child.login(IPADDR,SSH_Username,SSH_Passwd,auto_prompt_reset=False)
    print(f'[+] SSH Connection successful to {Routername}::{IPADDR} ')
    child.sendline('\n')
    child.expect(RouterExpectname)
    child.sendline('en')
    child.expect('Password.*')
    child.sendline(Enabel_Passwd)
    child.expect(RouterExpectname)
    child.sendline('copy running-config tftp:')
    child.expect('Address.*')
    child.sendline(TFTP_SERVER)
    child.expect('Destination.*')
    child.sendline(f'{Routername}-Config')
    print(f'[!] Waiting the Upload of {Routername}-Config file to {TFTP_SERVER} TFTP Server')
    sleep(1)
    child.expect(RouterExpectname)
    print(f'[+] successfuly upload {Routername}-Config to {TFTP_SERVER} TFTP Server ')
    sleep(1)
    child.logout()
