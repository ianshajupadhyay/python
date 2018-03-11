myfile = open("fruits.txt")
x = myfile.read()
x = x.splitlines()
print(x)
for i in x:
    print(len(i))
