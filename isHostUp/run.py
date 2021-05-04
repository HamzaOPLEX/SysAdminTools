import yaml
from threading import Thread
import subprocess

with open(r'config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    print('--> Start Checking connection ....')

def PingHost(IP):
    HOST_Status  = 'Conntected :)' if subprocess.run('ping -n 3 '+IP,shell=True,capture_output=True,text=True).returncode == 0 else 'not Connected :('
    
    theMsg = f'{IP} is {HOST_Status}' 
    print(theMsg)


def CheckConnection():
    DatabaseConfig = config['DATABASE_CONFIG']
    Threads = []
    for IP in DatabaseConfig:
        theThread = Thread(target=PingHost,args=(IP,))
        theThread.start()
        Threads.append(theThread)
    for th in Threads:
        theThread.join()

CheckConnection()
