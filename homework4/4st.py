import pylab as pl
import numpy as np
n_population1=[]
n_population2=[]
t=[0]
dt=float(raw_input('enter dt:'))
n_0=float(raw_input('enter the initial population:'))
t_final=float(raw_input('enter the end time:'))
global a
a=float(raw_input('enter the birth rate:'))
n_population1.append(n_0)
n_population2.append(n_0)
i_final=int(t_final/dt)
for i in range(i_final):
 n_t1=n_population1[i]+a*n_population1[i]*dt
 n_population1.append(n_t1)
 t.append(dt*(1+i))
 if n_0<1000:
  n_t2=n_population2[i]+(10*n_population2[i]-3*n_population2[i]*n_population2[i])*dt
  n_population2.append(n_t2)
 if n_0>=1000:
  n_t2=n_population2[i]+(10*n_population2[i]-0.01*n_population2[i]*n_population2[i])*dt
  n_population2.append(n_t2)
print n_population1
plot1=pl.plot(t,n_population1,'r')
plot2=pl.plot(t,n_population2,'g')
pl.title('population growth depending on time')
pl.xlabel('time t')
pl.ylabel('population N')
pl.plot(t,n_population1,color='red',linewidth=2.5,linestyle='-',label='death rate=0')
pl.plot(t,n_population2,color='green',linewidth=2.5,linestyle='-',label='with death rate')
pl.legend(loc='upper left')
pl.show()
