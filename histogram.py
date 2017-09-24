import matplotlib.pyplot as plt
plotting = [10,90,8,7,89,78,67,65,89,74,45,63,23,2,4,2,5,8,7,89,78,67,65]
bins = [0,10,20,30,40,50,60,70,80,90]
plt.hist(plotting , bins ,histtype= 'bar' , rwidth = 0.8)


plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title(" histo GRAPHS ")
plt.legend()
plt.show()
