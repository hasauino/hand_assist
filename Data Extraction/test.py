import cv2



crop1=(719,177)
crop0=(0,650)


lowerBound=(20,50,40)
upperBound=(255,255,255)


def funcCrop(x):
	m=float(crop1[1]-crop0[1])/float(crop1[0]-crop0[0])
	Y=m*(x-crop0[0])+crop0[1]
	return int(Y)


def crop(mask):
	for x in range(0,mask.shape[0]):
		mask[x,0:funcCrop(x)]=0
	return mask



path='v2.mp4' 

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
			if radius>7:
				centers.append(center)
				cv2.circle(img,center,radius,(0,255,0),2)





		cv2.imshow('frame',img)
		if k<819:
			k=cv2.waitKey(1)

		else:
			k=cv2.waitKey(0)

		if k==27:
			break


cap.release()
cv2.destroyAllWindows()



