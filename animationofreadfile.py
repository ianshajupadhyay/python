import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation
from matplotlib import style
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(0,0,0)
def animate(i):
    
    B=[10,20,30,40,50,60,70,80,90,100]
    df = pd.read_excel('file.xlsx')
    ax1.plt.hist(df['B'], B ,histtype= 'bar' , rwidth = 0.8)

ani = animation.FuncAnimation(fig , animate ,interval =1000)        


plt.xlabel('x')
plt.ylabel('y')
plt.title("read xl file")
plt.legend()
plt.show()


