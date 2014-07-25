'''
Created on Jul 18, 2014

@author: Chandan
'''
import os,string
def hostping2(host):
    switch={1:'-t',2:'-n',3:'-l'}
    print "The options for switches are as follows\n\n"
    print "1.\tPing the remote host until manual abort\n"
    print "2.\tPing the remote host with custom packet count\n"
    print "3.\tPing the remote host with custom packet size\n"
    opt=string.atoi(raw_input("Enter your choice:"))
    if opt == 1:
        cmd2="ping\t"+switch[1]+"\t"+host
        os.system(cmd2)
    elif opt == 2:
        pcount=string.atoi(raw_input("Enter desired number of packets:"))
        if pcount<0 or pcount>1000:
            print "Packet count is invalid"
        else:
            cmd3="ping\t"+switch[2]+"\t"+str(pcount)+"\t"+host
            os.system(cmd3)
    elif opt == 3:
        psize=string.atoi(raw_input("Enter custom packet size:"))
        if psize<0 or psize>30000:
            print "Packet size is invalid."
        else:
            cmd4="ping\t"+switch[3]+"\t"+str(psize)+"\t"+host
            os.system(cmd4)
    else:
        print "Invalid switch.\nPlease enter a valid switch:"

if __name__=='__main__':
    try:
        print "##########################################"
        print "######______HOST PING SCRIPT______######\n"
        print "#___________By Chandan___________#\n"
        while True:
            rhost=raw_input("Enter a host name or IP address:")
            s=raw_input("Would you like to opt for switches(y/n)?")
            if s=='n':
                cmd1="ping\t"+rhost
                os.system(cmd1)
                if(raw_input("\nWould you like to continue(y/n):")=='y'):
                    continue
                else:
                    print "Closing the program...."
                    break
            elif s=='y':
                hostping2(rhost)
                if(raw_input("\nWould you like to continue(y/n):")=='y'):
                    continue
                else:
                    print "Closing the program....."
                    break
            else:
                if(raw_input("\nInvalid choice. Would you like to continue(y/n):")=='y'):
                    continue
                else:
                    print "Closing the program....."
                    break
    except KeyboardInterrupt:
        print "\nCtrl+C pressed\nProgram exiting"  
