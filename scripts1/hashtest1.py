'''
Created on Jul 30, 2014

@author: Chandan
'''
import hashlib,string
path1=raw_input("Enter name of the wordlist:")
f1=open(path1,'r')
f2=open('Hashfile.txt','w')
seq2=[]
seq3=[]
for line in f1.readlines():
    line2=string.strip(line,'\n')
    seq2.append(line2)
    line1=hashlib.md5(line2).hexdigest()
    seq3.append(line1)
print seq2
print seq3
for i in range(len(seq3)):
    f2.write(seq3.__getitem__(i))
    f2.write('\n')    
f1.close()
f2.close()
