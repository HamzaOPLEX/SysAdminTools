from netmiko import *
from time import sleep
import yaml
from pprint import pprint
import sys

with open('/home/hamzaoplex/Desktop/Python Project test/Config.yaml') as yaml_read:
    Devices = yaml.load(yaml_read, Loader=yaml.FullLoader)
Routernames = list(Devices['Hosts'].keys())  # it is List ,  use loop

for dev in Routernames:
    print('~'*50)
    IP = Devices['Hosts'][dev][0]['IP']
    SSH_LOGIN = Devices['Hosts'][dev][1]['SSH_LOGIN']
    SSH_PASS = Devices['Hosts'][dev][2]['SSH_PASS']
    ENABEL_PASS = Devices['Hosts'][dev][3]['ENABEL_PASS']
    INTERFACE = Devices['Hosts'][dev][4]['INTERFACE']  # Here is LAN interface
    VLANS = Devices['Hosts'][dev][5]['VLANS_IP']  # Here is VLAN ID and IP

    print(f'[+] Configuring Stuff on '+dev)
    try:
        conn = ConnectHandler(device_type='cisco_ios', host=IP, username=SSH_LOGIN,
                              password=SSH_PASS, secret=ENABEL_PASS)
        conn.enable()
        conn.config_mode()
        for Vlaninfo in VLANS:
            for k, v in Vlaninfo.items():
                vlan_ID = k
                vlan_IP = v
                interface_conf = f'interface {INTERFACE}.{vlan_ID}\n'
                encapsulation_cmd = f'encapsulation dot1q {vlan_ID}'
                ip_add = f'ip add {vlan_IP} 255.255.255.0'
                Config = [interface_conf, encapsulation_cmd, ip_add]
                conn.send_config_set(Config)
                conn.exit_config_mode()
        print(conn.send_command('sh ip interface brief'))
    except Exception as err:
        print(err)
