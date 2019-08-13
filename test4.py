import cv2

img = cv2.imread('1.jpg',1)
face_engine = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
faces = face_engine.detectMultiScale(img,scaleFactor=1.2,minNeighbors=20)
for(x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,x+y),(255,0,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()