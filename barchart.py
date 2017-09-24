import matplotlib.pyplot as plt
x=[1,2,3]
y=[4,5,90]
x2=[3,45,78]
y2=[8,8,9]
plt.bar(x,y,label= "first data",color="green")

plt.bar(x2,y2,label= "second data", color="red")
plotting = [10,90,8,7,89,78,67,65,89,74,45,63,23,2,4,2,5,8,7,89,78,67,65]
ids = [x for x in range(len(plotting))]
plt.bar(ids , plotting)
plt.legend()


plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title(" BAR GRAPHS ")
plt.legend()
plt.show()

