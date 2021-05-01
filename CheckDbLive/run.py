import yaml
import socket

with open(r'config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

def set_up_config():
    default_port = config['Default']['Port']
    DatabaseConfig = config['DATABASE_CONFIG']
    for db in DatabaseConfig:
        theDB = config['DATABASE_CONFIG'][db]
        if 'Port' not in theDB:
            config['DATABASE_CONFIG'][db]['Port'] = default_port

def CheckConnection():
    DatabaseConfig = config['DATABASE_CONFIG']
    soc = socket.socket()
    TIME_OUT = 4
    soc.settimeout(TIME_OUT)
    for db in DatabaseConfig:
        soc = socket.socket(socket. AF_INET, socket. SOCK_STREAM)
        soc.settimeout(TIME_OUT)
        BIND = (
                    config['DATABASE_CONFIG'][db]['IP'],
                    config['DATABASE_CONFIG'][db]['Port']
                )
        try :
            print('--> Start Checking connection ....')
            soc.connect(BIND)
            soc.close()
            print(BIND , 'connected :)\n')
        except:
            print(BIND , 'not connected :(\n')

set_up_config()
CheckConnection()
