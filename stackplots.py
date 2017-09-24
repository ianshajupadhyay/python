import matplotlib.pyplot as plt
days=[1,2,4,8,9]
x=[1,2,3,7,0]
x2=[4,5,9,8,4]
x3=[3,4,8,7]
x4=[8,6,9,7]

plt.stackplot(days,x,x2);

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title(" stack plots ")
plt.legend()
plt.show()
