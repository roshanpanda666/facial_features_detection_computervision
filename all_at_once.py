import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml")

#step 2 detecting 
def detect(gray,frame):
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    eye=eye_cascade.detectMultiScale(gray,1.5,7)
    smile=smile_cascade.detectMultiScale(gray,1.9,56)
    #step 3 drawing the rectangle
    for(x,y,w,h)in faces:
        rectangle= cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),1)

        if rectangle.any()==True:
                
            cv2.putText(rectangle,"Face detected",(400,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)

    for(x,y,w,h)in eye:
        rectangle2= cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),1)

        if rectangle2.any()==True:
            cv2.putText(rectangle2,"eye detected",(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)

    for(x,y,w,h)in smile:
        rectangle= cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),1)

        if rectangle.any()==True:
            cv2.putText(rectangle,"Smiling",(450,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
    
    return frame

#take input from camera

video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()