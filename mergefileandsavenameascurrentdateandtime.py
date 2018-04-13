from datetime import datetime
x = datetime.now()
print(x)
files = ["anshaj.txt" , "example.txt" ]

with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in files:
        with open(filename,'r') as f:
            file.write(f.read() + '\n')
