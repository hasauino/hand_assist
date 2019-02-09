'''
This script is used to track the markers and export data as pkl file

needs to be run for each video. videos have to be named as follows: v0.mp4 v1.mp4 v2.mp4 ... m11.mp4 and so on
exported pkl file will carry the same name of the video: datav0.pkl   datav1.pkl  datav2.pkl ...  datav11.pkl 

manually you need to change: 1-rgb lower and upper bounds
                             2-crop values
                             3-video name
                             4-radius of markers (not allways, only when the markes appear too small in the video in case if camera was far from the hand). Line 74
'''

import numpy as np
import cv2
import imutils
import os
from numpy.linalg import norm
from sklearn.neighbors import NearestNeighbors
import numpy as np
from copy import copy
from math import atan2,pi
import pickle

# used to crop the red part of the device.
crop1=(719,177)
crop0=(0,650)


# markers rgb values range
lowerBound=(20,50,30)
upperBound=(255,255,255)

def funcCrop(x):
	m=float(crop1[1]-crop0[1])/float(crop1[0]-crop0[0])
	Y=m*(x-crop0[0])+crop0[1]
	return int(Y)


def crop(mask):
	for x in range(0,mask.shape[0]):
		mask[x,0:funcCrop(x)]=0
	return mask


# change this for each video
path='v11.mp4'

cap = cv2.VideoCapture(path)


data_centers=[]
data_angles=[]
data_time=[]
no_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

for k in range(0,int(no_frames)):
	print k
	centers=[]
	time = 0.001*cap.get(cv2.CAP_PROP_POS_MSEC)
	ret, img = cap.read()
	
	if ret:
		mask = cv2.inRange(img, lowerBound, upperBound)
		crop(mask)

		im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


		for cnt in contours:
			(x,y),radius = cv2.minEnclosingCircle(cnt)

			center = (int(x),int(y))
			radius = int(radius)
            # radius of markers
			if radius>7:
				centers.append(center)
				cv2.circle(img,center,radius,(0,255,0),2)



		_centers=sorted(centers,key=lambda f: float(f[0]))
		centers=_centers[1:]

		nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(centers)
		distances, indices = nbrs.kneighbors(centers)
		arr=copy(centers)


		for i in indices:
			img = cv2.line(img,  (centers[i[0]][0],centers[i[0]][1]  ), (centers[i[1]][0],centers[i[1]][1]  )   ,(255,0,0),5)



		j=0
		sortedCenters=[]
		angles=[]
		for i in range(0,len(centers)):
			sortedCenters.append(centers[j])
			cv2.putText(img,str(i+1),(centers[j][0],centers[j][1]), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
			prev_j=j
			j=indices[j][1]
			delY=(centers[j][1]-centers[prev_j][1])*-1
			delX=centers[j][0]-centers[prev_j][0]
			angles.append(	 180*atan2(delY,delX)/pi	)


		sortedCenters=[(_centers[0])]+sortedCenters
		delY=(sortedCenters[1][1]-sortedCenters[0][1])*-1
		delX=centers[1][0]-centers[0][0]
		angles=[	 180*atan2(delY,delX)/pi	]+angles


		img = cv2.line(img,  (sortedCenters[0][0],sortedCenters[0][1]  ), (sortedCenters[1][0],sortedCenters[1][1]  )   ,(255,0,0),5)
		cv2.putText(img,'0',(sortedCenters[0][0],sortedCenters[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)




		cv2.imshow('frame',img)
		k=cv2.waitKey(1)
		if k==27:
			break

		if len(data_centers)==0:
			data_centers=[sortedCenters]
			data_angles=angles
			data_time=time

		else:
			data_centers=np.vstack((data_centers,[sortedCenters]))
			data_angles=np.vstack((data_angles,angles))
			data_time=np.vstack((data_time,time))


with open('data'+path[0:-4]+'.pkl', 'w') as f:
    pickle.dump([data_time, data_angles, data_centers], f)
cap.release()
cv2.destroyAllWindows()



