import pylab as pl
import numpy as np
import math

x=[0]
y=[0]
t=[0]
v_x=[]
v_y=[]
v=[]
dt=0.01
v_0=800*1.414
angle=45
t_final=100
v_x0=v_0*math.cos(math.radians(angle))
v_y0=v_0*math.sin(math.radians(angle))
v_x.append(v_x0)
v_y.append(v_y0)
v.append(v_0)
i_final=int(t_final/dt)
for i in range(i_final):
	x_t1  =x[i]+v_x[i]*dt
	y_t1  =y[i]+v_y[i]*dt
	v_xt1 =v_x[i]-(0.00004*v[i]*v_x[i]*(1-(0.0065*y[i])/288)**(2.5))*dt
	v_yt1 =v_y[i]-(0.00004*v[i]*v_y[i]*(1-(0.0065*y[i])/288)**(2.5)+9.8)*dt
	x.append(x_t1)
	y.append(y_t1)
	v_t1  =math.sqrt((v_xt1)**2+(v_yt1)**2)
	v_x.append(v_xt1)
	v_y.append(v_yt1)
	v.append(v_t1)
	t.append(dt*(1+i))


pl.plot(x,y,'r')
pl.title('Trajectory of cannon')
pl.xlabel('X(m)')
pl.ylabel('Y(m)')
pl.show()