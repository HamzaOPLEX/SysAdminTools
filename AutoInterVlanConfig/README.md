# AutoInterVlanConfig
Config Inter-Vlan using Python Script  
all SSH ,  Vlan and IP's information will be Configured by the Administrator in a YAML File 


![alt text](https://github.com/HamzaOPLEX/AutoInterVlanConfig/blob/master/Screenshot%20from%202020-07-29%2018-27-09.png?raw=true)



# YAML File Format : 

**Notice the config file need to be named Config.yaml**

```
Hosts :
  R1 : # Router Hostname 
    - IP : '172.16.0.100' # Router IP@
    - SSH_LOGIN : 'Admin' # Router SSH LOGIN
    - SSH_PASS : 'Admin' # Router SSH PASSWD
    - ENABEL_PASS : 'Admin' # ROUTER ENABEL PASSWD
    - INTERFACE : 'f0/0' # ROUTER interface 
    - VLANS_IP : # VLANS
      - 10 : '192.168.10.2'
      - 20 : '192.168.20.100'
      - 30 : '192.168.30.250'
      - 80 : '192.168.80.200'

```

