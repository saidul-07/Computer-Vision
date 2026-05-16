import cv2

# # version check
# print(cv2.__version__)  

# # image reading
# img = cv2.imread("resources/lena.png")
# print(img)
# cv2.imshow("output",img)
# cv2.waitKey(0)

# # Video Reading
# cap= cv2.VideoCapture("resources/elon.mp4")
# while True:
#     success, img = cap.read()
#     if not success:
#         break
#     cv2.imshow("output",img)
    
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break

# Reading from WebCame
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True:
    success, img = cap.read()
    if not success:
        print("Failed to webcam")
        break
    
    cv2.imshow("output",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()