from random import *

password = input("input a password ")

passwordkeys =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
     '0','1','2','3','4','5','6','7','8','9',"!","@",'#','$','%','^','&','*','-','_','=',"+","~",'`',';',':','?',".",",","<",'>','/']

hackpassword =""

while hackpassword != password:
    hackpassword = ""
    for latter in range (len(password)):
        gauss_password = passwordkeys[randint(0,35)]
        hackpassword = str(gauss_password) + str(hackpassword)
        print(hackpassword)
        print("creating password...please wait")
print(f"your password is {hackpassword}")