#Chen, Hao
#2017,Spring
#chen579@usc.edu

import hashlib
import itertools
import string
import time

#This funtion is to read the input file
def read(fileName):
    textList = []
    textFile = open(fileName, "r")
    #Using for loop to set every line in the passwords file to be an element in a lsit
    for line in textFile:
        line=line.strip()
        textList.append(line)
    textFile.close()
    return textList

#This function uses hashlib to the MD5 value of a string
def get_md5_value(str):
    m = hashlib.md5()
    m.update(repr(str).encode('utf-8'))
    return m.hexdigest()

def main():

    passwords=read("pw.txt")
    print(get_md5_value("AbCdE"))
    length=1   #initialize the length of the password to 1
    for item in passwords:
        start=time.time()  #record the start time
        pw=itertools.product(string.printable,repeat=length)  #Create a library to store all permutation of every string character with given length
        for i in pw:
            #Set each element in the passwords library to string type.
            c=""
            for iele in i:
                c+=iele
            MD5=get_md5_value(c)
            #Find which element in the password library has the same MD5 value with the MD5 value in the given hashed password file.
            if MD5==str(item):
                print("When the password is",c)
                break #when the macthed result is found, starts to crack next hashed password in passwords file.
        elapsed=(time.time() - start)   #Calculating the cracking time for each turn
        print("Cracking time is",str(elapsed))
        print()
        length=length+1  # increase the string length of the password by 1 for each turn

main()
