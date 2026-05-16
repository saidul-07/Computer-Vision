import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)
img[:]=255,0,0

# Create Line
# cv2.line(img,(0,0),(300,400),(0,255,0),5)

# Rectangle
# cv2.rectangle(img,(100,50),(300,400),(0,0,255),7)

# Circle
# cv2.circle(img,(300,400),50,(0,255,0),7)

# Put Texts
cv2.putText(img,"Sayedul",(200,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
cv2.imshow("Line",img)
cv2.waitKey(0)