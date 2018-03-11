myfile = open("sample.txt")
content = myfile.read()
z = myfile.read()
myfile.close()

print("-------------------------------------------")

print(str(content))
print(type(content))
contents = content.splitlines()
print(contents)
print("-------------------------------------------")

print(z)
print("-------------------------------------------")
print(type(myfile))
print(type(contents))
print("------------------------------------------")
if "chill" in contents :
    print("YES")
else:
    print("NO")
