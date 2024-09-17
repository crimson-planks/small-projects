import matplotlib.axes as pla
import matplotlib.pyplot as plt
import numpy as np
def get_scale_from_generator(generator,amount_stacked: int):
    return np.power(generator,np.arange(0,amount_stacked))

intervals=get_scale_from_generator(1+1j,10) #change the 1+1j to change interval

x = np.real(intervals)
y = np.imag(intervals)
labels = [f"{np.real(z)} + {np.imag(z)}i" for z in intervals]

subplot = plt.subplots()
fig = subplot[0]
ax: pla.Axes = subplot[1]

ax.plot(x,y,'o-')
for i, label in enumerate(labels):
    ax.annotate(label, (x[i],y[i]))
ax.set_title('Complex Intervals')

ax.set(xlim=(-20, 20), xticks=np.arange(-20, 20,5),
       ylim=(-20, 20), yticks=np.arange(-20, 20,5)) #change this to change scale

plt.show()