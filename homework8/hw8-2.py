import pylab as pl
import numpy as np
import math

angular_velocity=[0]
angle=[]
t=[0]

dt=float(raw_input('enter dt:'))
angle_0=math.radians(float(raw_input('enter the initial angle:')))
t_final=float(raw_input('enter the end time:'))
l=float(raw_input('enter the length of the string:'))
q=float(raw_input('enter strengh of the damping parameter:'))
force=float(raw_input('enter the amplitude of the driving force:'))
frequency=float(raw_input('enter the angular frequency of the driving force:'))
angle.append(angle_0)
g=9.8

i_final=int(t_final/dt)
for i in range(i_final):
 angular_velocity_1=angular_velocity[i]-9.8*(math.sin(angle[i]))*dt/l
 angular_velocity.append(angular_velocity_1)
 angle_1=angle[i]+angular_velocity[i+1]*dt
 angle.append(angle_1)
 t.append(dt*(1+i))
 
pl.plot(t,angle,'r')
pl.title('the angle of the pendulum depending on time')
pl.xlabel('time t')
pl.ylabel('angle')
pl.show()
