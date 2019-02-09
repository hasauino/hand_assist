import pickle
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm




with open('datav4.pkl') as f:  
	data_time, data_angles, data_centers = pickle.load(f)


data_angles=np.array(data_angles)
t=np.array(data_time)
data_centers=np.array(data_centers)


MCP_angles=data_angles[:,1]-data_angles[:,0]
MCP_angles=MCP_angles[0]-MCP_angles
PIP_angles=data_angles[:,2]-data_angles[:,1]
PIP_angles=PIP_angles[0]-PIP_angles
DIP_angles=data_angles[:,3]-data_angles[:,2]
DIP_angles=DIP_angles[0]-DIP_angles

movementPercentage=100*t/t[-1]

plt.figure(1)
ax=plt.axes()
ax.plot(movementPercentage, MCP_angles, 'r',label='MCP',linewidth=2)
ax.plot(movementPercentage, PIP_angles, 'b',label='PIP',linewidth=2)
ax.plot(movementPercentage, DIP_angles, 'k',label='DIP',linewidth=2)
ax.grid()
ax.set_xlabel('Grip Cycle (%)')
ax.set_ylabel('Angles (degrees)')
#ax.set_title('Finger\'s Joint Angles')
ax.legend()

#__________Positions______________________
#conversion factor from pixles to mm
#distance between PIP and DIP = 25 mm when hand is fully extended


factor=23.0/norm(np.array(data_centers[0,2,:])-np.array(data_centers[0,3,:]))

print data_centers


MCP_position=data_centers[:,1,:]*factor
PIP_position=data_centers[:,2,:]*factor
DIP_position=data_centers[:,3,:]*factor
distal_bone=data_centers[:,4,:]*factor


theta = np.radians(-90)
c, s = np.cos(theta), np.sin(theta)
R = np.array(((c,-s), (s, c)))

MCP_position=np.matmul(MCP_position,R)
PIP_position=np.matmul(PIP_position,R)
DIP_position=np.matmul(DIP_position,R)
distal_bone=np.matmul(distal_bone,R)


plt.figure(2)
ax2=plt.axes()
ax2.plot(PIP_position[:,1], PIP_position[:,0], 'r',label='PIP',linewidth=2)
ax2.plot(DIP_position[:,1], DIP_position[:,0], 'b',label='DIP',linewidth=2)
ax2.plot(distal_bone[:,1], distal_bone[:,0], 'k',label='Distal bone',linewidth=2)

ax2.grid()
ax2.set_xlabel('X (mm)')
ax2.set_ylabel('Y (mm)')
#ax2.set_title('Finger\'s Joint Angles')
ax2.legend()
plt.show()
