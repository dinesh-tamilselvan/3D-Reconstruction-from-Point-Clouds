import numpy as np
import matplotlib.pyplot as plt

xd=np.linspace(-1,1);
yd=np.linspace(0,2*np.pi);
[x,y]=np.meshgrid(xd,yd);
z=x*(np.sin(y)+np.cos(y));

fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
 
# Creating plot
ax.plot_surface(x, y, z)
 
# show plot
plt.show()
#surf(x,y,z)

x = x.reshape(2500,1)
y = y.reshape(2500,1)
z = z.reshape(2500,1)

fig1 = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x, y, z, color = "green")
