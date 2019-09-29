# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:35:50 2019

@author: Admin
"""
import importlib

moduleName = 'sdes'##from internet
sdes = importlib.import_module(moduleName)


mycode = [5,9,0,6,1,0,6,4,9]
#mycodetest = ["00000101","00001001","00000000","00000110","00000001","00000000","00000110","00000100","00001001"]
webcipher = "0b11010111,0b10111100,0b10100010,0b1011101,0b10010010,0b10100010,0b1011101,0b111,0b10111100,0b111,0b111,0b1101001,0b1011101,0b1101001,0b111,0b111,0b111111,0b11010111,0b111,0b10111110,0b10111100,0b11000,0b1011101,0b11010111,0b10010010,0b1101001,0b111111,0b10111100,0b10010010,0b10100010,0b111111,0b10111100,0b10111110,0b1101001,0b10111110,0b10100010,0b10010010,0b1101001,0b10100010,0b10010010,0b11010111,0b11000,0b11010111,0b11010111,0b11000,0b11000,0b10111100,0b1011101,0b10010010,0b10010010,0b111,0b111,0b1011101,0b10100010,0b10010010,0b11010111,0b10111110,0b111111,0b1011101,0b111,0b11010111,0b10111100,0b10010010,0b10010010,0b10111100,0b11000,0b111111,0b111,0b111111,0b111111,0b1101001,0b10010010,0b10100010,0b1101001,0b10010010,0b1101001,"



mykeylist = []
for i in range (1024):
    mykeylist.append(bin(i)[2:].zfill(10))

newkeylist = []
        
student_encode = webcipher[:-1].split(",")[0:9]

print("///// ENCRYPT TEST ///// test each 590610649 -[key]-> == cipher-text? /////")
for i in range(len(student_encode)): #590610649
    eachcipher = student_encode[i][2:].zfill(8)
    mycipher = bin(mycode[i])[2:].zfill(8)

    newkeylist = []
    
    for j in range (len(mykeylist)): # 2^10  key
        
        mybruteforce = sdes.enc(mykeylist[j],mycipher)
        
        if(mybruteforce == eachcipher):
            newkeylist.append(int(mykeylist[j],2))
            
    print("code",mycode[i],"to binary ",mycipher," keys found = ",newkeylist)
print("(key in decimal)")

print()
print("///// DECRYPT TEST ///// test each cipher-text -[key]-> == 590610649? /////")
for i in range(len(student_encode)): #590610649
    eachcipher = student_encode[i][2:].zfill(8)
    mycipher = bin(mycode[i])[2:].zfill(8)

    newkeylist = []
    
    for j in range (len(mykeylist)): # 2^10  key
        mybruteforce = sdes.dec(mykeylist[j],eachcipher)
        
        if(mybruteforce == mycipher):
            newkeylist.append(int(mykeylist[j],2))
            
    print("cipher ",eachcipher," keys found = ",newkeylist)
print("(key in decimal)")
#print(mykeylist)
















    
