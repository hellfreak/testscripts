'''
Created on Jul 25, 2014

@author: Chandan
'''
import subprocess,os,sys,string
def pinghost(target):
    cmd="ping "+target
    sysping=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE)
    p1=sysping.communicate()
    if 'Lost = 4' in p1.__getitem__(0):
        print "\nHost unresponsive"
    else:
        print p1.__getitem__(0)

def nslookto(target):
    cmd="nslookup "+target
    os.system(cmd)

def tlnthost(target,port):
    cmd="telnet "+target+" "+str(port)
    os.system(cmd)
    
if __name__=='__main__':
    try:
        while True:
            host=raw_input("Enter a hostname or IP Address:")
            print "\n1. Ping the host"
            print "2. Perform a Nslookup on the host"
            print "3. Telnet a port on the host"
            opt=string.atoi(raw_input("Enter your choice:"))
            if opt==1:
                pinghost(host)
            elif opt==2:
                nslookto(host)
            elif opt==3:
                while True:
                    prt=string.atoi(raw_input("\nEnter a port number:"))
                    if prt < 0 or prt > 65535:
                        print "Invalid port number!!"
                        continue
                    else:
                        tlnthost(host,prt)
                        break
            else:
                if raw_input("Invalid choice.\nDo you want to continue(y/n):")=='y':
                    continue
                else:
                    break 
    except KeyboardInterrupt:
        print "\nExiting program!!!"
            
