# Second tutorial in image processing
# Description can be found [here](https://lukakozina6.wixsite.com/cvlab/post/new-changes-new-you) 




import cv2 
import numpy as np
from matplotlib import pyplot as plt

#def click(event, x, y, flags, param):
#	if event == cv2.EVENT_LBUTTONDOWN:
#		strXY = str(x) + ',' + str(y)
#		cv2.putText(img, strXY, (x,y), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,255,0), 2)
#		cv2.imshow('Mount',img)


img = cv2.imread('mount.jpeg')
img2 = np.zeros((1000, 1000, 3), np.uint8)
img3 = cv2.imread("water_balloons.jpg")
img = cv2.resize(img, (1000, 1000))
img3 = cv2.resize(img3, (1000, 1000))

#print( img.shape )
#print( img.size )
#print( img.dtype )

#cv2.rectangle(img,(300,100),(600,300),(0,255,0),3)
#cv2.circle(img,(500,500), 50, (0,0,255), -1)
#cv2.ellipse(img,(300,400),(100,100),0,0,180,255,-1)
#pts = np.array([[30,20],[100,100],[500,400],[800,800]], np.int32)
#cv2.polylines(img, [pts], True, (255, 0, 0), 6)
#cv2.putText (img, 'MASON MOUNT', (10,500), cv2.FONT_HERSHEY_SIMPLEX, 4, (0,255,0), 5, cv2.LINE_AA)

#ball = img[830:980, 225:325]
#img[830:980, 700:800] = ball

#b,g,r = cv2.split(img)
#cv2.imshow("Blue", b)
#cv2.imshow("Green", g)
#cv2.imshow("Red", r)
#img = cv2.merge((b,g,r))


#bitAnd = cv2.bitwise_and(img2, img)
#bitOr = cv2.bitwise_or(img2, img)
#bitXor = cv2.bitwise_xor(img, img2)
#bitNot1 = cv2.bitwise_not(img)
#bitNot2 = cv2.bitwise_not(img2)
#cv2.imshow('bitAnd', bitAnd)
#cv2.imshow('bitOr', bitOr)
#cv2.imshow('bitXor', bitXor)
#cv2.imshow('bitNot1', bitNot1)
#cv2.imshow('bitNot2', bitNot2)

added_img = cv2.add(img,img3);
addW_img = cv2.addWeighted(img, .7, img3, .3, 0);

#cv2.imshow("Mount", img)
#cv2.imshow("Black", img2)
#cv2.imshow("Water Balloons", img3)
#cv2.imshow("Added image", added_img)
cv2.imshow("AddWeighted image", addW_img)
#cv2.setMouseCallback('Mount', click)
#cv2.imwrite('new_img.jpg', addW_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
