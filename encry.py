print("PASSWORD ENCRYPTER")
print("==================")
s=str(input("Enter the password you want to encrypt: "))
a=len(s)
s=list(s)
for i in range(0,a):
    if((i%2==0)and(s[i].islower())):
        s[i]=chr(ord(s[i])-32+(int(i/2))+1)  
    elif(s[i].islower()):
        s[i]=chr(ord(s[i])-64)   
s="".join(s)
print("The encrypted password is: ")
print(s)
