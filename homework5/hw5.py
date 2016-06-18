import matplotlib.pyplot as pl
import numpy as np


n_nuclei1=[]
n_nuclei2=[]
t=[0]
dt=0.01
n_0a=100
n_0b=0
t_final=10
# global a
a=1
n_nuclei1.append(n_0a)
n_nuclei2.append(n_0b)
i_final=int(t_final/dt)

for i in range(i_final):
	n_t1 =n_nuclei1[i]+((n_nuclei2[i]/a)-n_nuclei1[i]/a)*dt
	n_t2 =n_nuclei2[i]+((n_nuclei1[i]/a)-n_nuclei2[i]/a)*dt
	n_nuclei1.append(n_t1)
	n_nuclei2.append(n_t2)
	t.append(dt*(1+i))

plot1=pl.plot(t,n_nuclei1,'r')
plot2=pl.plot(t,n_nuclei2,'g')
pl.title('Nuclei decay with two types of nuclei')
pl.xlabel('T/(s)')
pl.ylabel('nuclei number N')
pl.plot(t,n_nuclei1,color='red',linewidth=2.5,label='Nuclei A')
pl.plot(t,n_nuclei2,color='blue',linewidth=2.5,label='Nuclei B')
pl.legend(loc='upper right')
pl.show()