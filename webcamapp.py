import cv2
import time


video = cv2.VideoCapture(0)
time.sleep(1)

first_frame=None
while True:

    check,frame=video.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame_gaus=cv2.GaussianBlur(gray_frame,(21,21),0)


    if first_frame  is None:
        first_frame=gray_frame_gaus

    delta_frame=cv2.absdiff(first_frame,gray_frame_gaus)


    thres_frame = cv2.threshold(delta_frame,60,255,cv2.THRESH_BINARY)[1]
    dil_frame  = cv2.dilate(thres_frame,None,iterations=2)
    cv2.imshow("My Video", dil_frame)



    key=cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()





