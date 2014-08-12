'''
Created on Aug 12, 2014

@author: Chandan
'''
from socket import *
import subprocess
hostAddress='127.0.0.1'
port=51000
sock1=socket(AF_INET, SOCK_STREAM)
sock1.bind((hostAddress,port))
sock1.listen(5)
conn1, addr1=sock1.accept()
data1=conn1.recv(1024)
sys2=subprocess.Popen(data1,shell=False,stdout=subprocess.PIPE)
p2=sys2.communicate()
data2=p2.__getitem__(0)
conn1.send(data2)
conn1.close()
