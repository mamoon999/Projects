import numpy as np 
import cv2
# from final_encoding import *

def detect(path):
    facedetect = cv2.CascadeClassifier(r'C:\Users\91967\AppData\Local\Programs\Python\Python312\Facial-Recognition-for-Crime-Detection-master\Advanced Identity Recognition\haarcascade_frontalface_default.xml')
    #cam = cv2.VideoCapture(0)
    cam = cv2.VideoCapture(path)
    sampleNum = 0


    while(True):
        ret,img = cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray,1.3,5)

        for(x,y,w,h) in faces:
            sampleNum+=1
            cv2.imwrite('dataset/'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.waitKey(1)
        cv2.imshow('face',img)
        cv2.waitKey(1)
        if(sampleNum>100):
            break

    cam.release()
    cv2.destroyAllWindows()