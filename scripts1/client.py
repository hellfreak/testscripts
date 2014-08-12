'''
Created on Aug 12, 2014

@author: Chandan
'''
from socket import *
hostAddress='127.0.0.1'
hostPort=51000

sock2=socket(AF_INET,SOCK_STREAM)
sock2.connect((hostAddress,hostPort))
cmd=raw_input("Enter command:")
sock2.send(cmd)
data=sock2.recv(2048)
print data
sock2.close()
