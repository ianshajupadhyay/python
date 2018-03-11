correctpass = "anshajpc"
name = input("Enter name:")
password = input("Enter passsword :")
while correctpass!=password:
    print("Wrong password! Enter password again")
    password = input("Enter passsword :")
print("Congrats %s you Loged in Successfully" %name)
