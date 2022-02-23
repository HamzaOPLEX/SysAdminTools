import os
import csv

# PinginfoView Config
PinginfoView__Name = "PingInfoView.exe"
PinginfoView__FolderPath = "."
PinginfoView__Path = os.path.join(PinginfoView__FolderPath,PinginfoView__Name)

# host file Config
HostsFile__Name = "hosts.txt"
HostsFile__FolderPath = "."
HostsFile__Path = os.path.join(HostsFile__FolderPath,HostsFile__Name)

# host file Config
OutputFile__Name = "output.csv"
OutputFile__FolderPath = "."
OutputFile__Path = os.path.join(OutputFile__FolderPath,OutputFile__Name)

# Simulating Database of hosts
hosts = ["192.168.1."+str(i) for i in range(254)]


# Create hosts.txt file and add hosts from Database
with open(HostsFile__Name,"w") as HostsFile :
    for host in hosts : 
        HostsFile.write(host+"\n")

# run ping tool
PingCommand = f"{PinginfoView__Path}  /loadfile {HostsFile__Path} /scomma {OutputFile__Path}"
os.system(PingCommand)


# Read Output.csv
with open(OutputFile__Path, 'r') as OutputFile:
    reader = csv.reader(OutputFile)
    for row in reader:
        print(row[0],"=>",row[10])