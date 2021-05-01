# Send_SSH_KEY
this script use Python3 and Nornir Framework for sending ssh key to the Cisco Devices 



# Instalation : 

$ git clone https://github.com/HamzaOPLEX/Send_SSH_KEY/

$ cd Send_SSH_KEY

$ pip3 install nornir==2.4.0 --force-reinstall

- After That go to hots.yaml and add your hosts
- Then go to defaults.yaml and add ssh username&password and OS type(ios for cisco)
- Then run 

$ python3 run.py
