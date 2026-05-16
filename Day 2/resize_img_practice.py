import cv2

# # Resizing images
# img = cv2.imread("resources/lambo.png")
# print(img.shape)

# resized_img = cv2.resize(img,(300,200))
# print(resized_img.shape)

# cv2.imshow("Original Image ",img)
# cv2.imshow("resized image ",resized_img)
# cv2.waitKey(0)

# Croping Image
img = cv2.imread("resources/lambo.png")
crop_img= img[0:200,200:500]
cv2.imshow("original ",img)
cv2.imshow("Crop image ",crop_img)
cv2.waitKey(0)