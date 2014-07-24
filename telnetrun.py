'''
Created on Jul 24, 2014

@author: Hellfreak
'''
import string,os,time

def telnt(ip,port):
    cmd='telnet '+ip+' '+port
    os.system(cmd)

if __name__=='__main__':
    try:
        host=raw_input("Enter IP Address or hostname:")
        p=raw_input("Enter port number:")
        count=string.atoi(raw_input("Enter the number of times to run command:"))
        for i in range(count):
            telnt(host,p)
            time.sleep(180)
    except KeyboardInterrupt:
        print "Program exiting...."
