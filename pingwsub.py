'''
Created on Jul 22, 2014

@author: Chandan
'''
import subprocess,string
def ops(target,opt):
    try:
        if opt==1:
            p1=subprocess.Popen(["ping",target],shell=True,stdout=subprocess.PIPE)
            res1=p1.communicate()
            lines1=string.split(res1.__getitem__(0),'\n')
            for line in lines1:
                    print line    
        elif opt==2:
            p2=subprocess.Popen(["nslookup",target],shell=True,stdout=subprocess.PIPE)
            res2=p2.communicate()
            lines2=string.split(str(res2.__getitem__(0)),'\r\r\n')
            for line in lines2:
                    print line    
        else:
            print "\nInvalid input!!!"
    except KeyboardInterrupt:
        print "\n Interrupt detected.\nProgram exiting..."
            
if __name__=="__main__":
    try:
        print "Test Script by H3llfr3@k"
        while True:
            host=raw_input("Enter the domain name or IP:")
            print "_____OPTIONS_____\n"
            print "1. Ping the remote host\n"
            print "2. Perform nslookup on the host\n"
            n=string.atoi(raw_input("Enter your choice:"))
            ops(host,n)
            ch=raw_input("Do you want to continue:")
            if ch=='y':
                continue
            else:
                print "Program exiting..."
                break
    except KeyboardInterrupt:
        print "\n Interrupt detected.\nProgram exiting..."
