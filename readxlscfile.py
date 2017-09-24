import matplotlib.pyplot as plt
import pandas as pd
B=[10,20,30,40,50,60,70,80,90,100]
df = pd.read_excel('file.xlsx')
plt.hist(df['B'], B ,histtype= 'bar' , rwidth = 0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title("read xl file")
plt.legend()
plt.show()
