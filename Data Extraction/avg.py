import pickle
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm
from numpy import inf
from copy import copy
from scipy.io import savemat

data=[]

no_videos=9.0


for i in range(0,int(no_videos)):
	with open('datav'+str(i)+'.pkl') as f:  
		data.append(pickle.load(f))


data=np.array(data)




#__________Positions______________________
#conversion factor from pixles to mm
#distance between PIP and DIP = 25 mm when hand is fully extended


for i in range(0,int(no_videos)):
	factor=(   25.0/norm((data[i][2][0,2,:])-(data[i][2][0,3,:]))  )
	data[i][2]=data[i][2]*factor


#zero offset, and rotate centers 
theta = np.radians(-90)
c, s = np.cos(theta), np.sin(theta)
R = np.array(((c,-s), (s, c)))


for i in range(0,int(no_videos)):
	zeroOffset=copy(data[i][2][0,0,:])
	for j in range(0,5):                                                                                                                                                                                             
		data[i][2][:,j,:]=data[i][2][:,j,:]-zeroOffset
		data[i][2][:,j,:]=np.matmul(data[i][2][:,j,:],R)




minL=inf
for i in range(0,int(no_videos)):
	if len(data[i][0])<minL:
			minL=len(data[i][0])






plt.figure(1,figsize=(5,4))
ax=plt.axes()
color=['r','b','k','y','c','m','k','r--','b--','g--']
'''
for i in range(0,int(no_videos)):
	ax.plot(data[i][2][0:minL,2,1], data[i][2][0:minL,2,0], 'y' ,linewidth=1)
	ax.plot(data[i][2][0:minL,3,1], data[i][2][0:minL,3,0], 'y' ,linewidth=1)
	ax.plot(data[i][2][0:minL,4,1], data[i][2][0:minL,4,0], 'y' ,linewidth=1)
	pass
'''



avg=[]
for j in range(0,5):
	sum=data[0][2][0:minL,j]
	for i in range(1,int(no_videos)):
		sum+=data[i][2][0:minL,j]
	avg.append(sum/no_videos)


lab=['PIP','DIP','DP']

for i in range(2,5):
	ax.plot(avg[i][:,1], avg[i][:,0], color[i-2] ,label=lab[i-2],linewidth=2)




ax.grid()
ax.set_xlabel('x (mm)')
ax.set_ylabel('y (mm)')
#ax.set_title('Finger\'s Joint Angles')
ax.set_xlim((50,120))
ax.set_ylim((-40,75))
ax.legend()


#-------Angles------------

plt.figure(2,figsize=(5,4))
ax2=plt.axes()

angles=[]
sum_MCP=[]
sum_PIP=[]
sum_DIP=[]

for i in range(0,int(no_videos)):
	data_angles=data[i][1]

	MCP_angles=data_angles[0:minL,1]-data_angles[0:minL,0]
	MCP_angles=MCP_angles[0]-MCP_angles
	PIP_angles=data_angles[0:minL,2]-data_angles[0:minL,1]
	PIP_angles=PIP_angles[0]-PIP_angles
	DIP_angles=data_angles[0:minL,3]-data_angles[0:minL,2]
	DIP_angles=DIP_angles[0]-DIP_angles

	if len(sum_DIP)>0:
		sum_MCP+=MCP_angles
		sum_PIP+=PIP_angles
		sum_DIP+=DIP_angles
	else:
		sum_MCP=copy(MCP_angles)
		sum_PIP=copy(PIP_angles)
		sum_DIP=copy(DIP_angles)


	movementPercentage=100*data[i][0][0:minL]/data[i][0][minL-1]
	#ax2.plot(movementPercentage, MCP_angles, 'y',linewidth=1)
	#ax2.plot(movementPercentage, PIP_angles, 'y',linewidth=1)
	#ax2.plot(movementPercentage, DIP_angles, 'y',linewidth=1)


ax2.plot(movementPercentage, sum_MCP/no_videos , 'r' ,label='MCP',linewidth=2)
ax2.plot(movementPercentage, sum_PIP/no_videos , 'b' ,label='PIP',linewidth=2)
ax2.plot(movementPercentage, sum_DIP/no_videos , 'k' ,label='DIP',linewidth=2)
	



ax2.grid()
ax2.set_xlabel('Grip Cycle (%)')
ax2.set_ylabel('Angles (degrees)')
#ax2.set_title('Finger\'s Joint Angles')
ax2.set_xlim((-5,105))
ax2.set_ylim((-5,70))
ax2.legend()



savemat('IP_DP_Data',{'positions':avg,'movementPercentage':movementPercentage,'MCP':sum_MCP/no_videos,'PIP':sum_PIP/no_videos,'DIP':sum_DIP/no_videos})

plt.show()






