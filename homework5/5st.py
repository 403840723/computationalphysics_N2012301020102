import pylab as pl
import numpy as np
n_nuclei1=[]
n_nuclei2=[]
t=[0]
dt=float(raw_input('enter dt:'))
n_0a=float(raw_input('enter the initial number of nuclei A:'))
n_0b=float(raw_input('enter the initial number of nuclei B:'))
t_final=float(raw_input('enter the end time:'))
global a
a=float(raw_input('enter the time constant:'))
n_nuclei1.append(n_0a)
n_nuclei2.append(n_0b)
i_final=int(t_final/dt)
for i in range(i_final):
 n_t1=n_nuclei1[i]+((n_nuclei2[i]/a)-n_nuclei1[i]/a)*dt
 n_t2=n_nuclei2[i]+((n_nuclei1[i]/a)-n_nuclei2[i]/a)*dt
 n_nuclei1.append(n_t1)
 n_nuclei2.append(n_t2)
 t.append(dt*(1+i))
plot1=pl.plot(t,n_nuclei1,'r')
plot2=pl.plot(t,n_nuclei2,'g')
pl.title('nuclei decay with two types of nuclei')
pl.xlabel('time t')
pl.ylabel('nuclei number N')
pl.plot(t,n_nuclei1,color='red',linewidth=2.5,linestyle='-',label='nuclei A')
pl.plot(t,n_nuclei2,color='green',linewidth=2.5,linestyle='-',label='nuclei B')
pl.legend(loc='upper left')
pl.show()
