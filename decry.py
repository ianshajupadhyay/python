print("PASSWORD DECRYPTER")
print("==================")
s=str(input("Enter the encrypted password you want to decrypt "))
a=len(s)
s=list(s)
for i in range(0,a):
    if((ord(s[i])>=65)and(ord(s[i])<=90)):
        s[i]=chr(ord(s[i])+32-(int(i/2))-1)
    #elif((i%2==0)and(s[i].isupper())):
    #    s[i]=chr(ord(s[i])+31)    
    elif((ord(s[i])>=33)and(ord(s[i])<=63)):
        s[i]=chr(ord(s[i])+64)
    #else:
    #    s[i]=chr(ord(s[i])+33)    
s="".join(s)
print("The decrypted password is ")
print(s)
