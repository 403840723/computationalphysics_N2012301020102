import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0.0,20.0,201)
def f(x): return (1-np.exp(-x))*10
v=[]
t=[]
a=9.8;b=1
dt=0.1
v.append(0.0)
t.append(0)
end_time=15

for i in range(int(end_time/dt)):
    tmp=v[-1]+dt*(a-b*v[-1])
    v.append(tmp)
    t.append(dt*(i+1))
    print (t[-1],v[-1])


line1,=plt.plot(t,v,'ro')
line2,=plt.plot(x,f(x),'b--',linewidth=3)
plt.xlabel("T/(s)")
plt.ylabel("V/(m/s)")
plt.legend((line1,line2),('Numerical','Analytical'))
plt.title("The time-dependenct Velocity of A Falling Ball with Friction")
plt.show()