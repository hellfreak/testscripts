'''
Created on Jul 22, 2014

@author: Chandan
'''
import os,string
def ping1():
    dom=[]
    n=string.atoi(raw_input("Enter the no. of domains:"))
    for i in range(n):
        domain=raw_input("\nEnter domain name:")
        dom.insert(i, domain)
    print dom
    for i in range(0,n):
        cmd="nslookup "+str(dom[i])
        os.system(cmd)

if __name__=="__main__":
    try:
        ping1()
    except KeyboardInterrupt:
        print "\nProgram Exiting"
    
    
