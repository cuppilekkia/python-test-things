import cv2, time

video=cv2.VideoCapture(0)

if video.isOpened():
  while True:
    _,frame = video.read()
    #gray_frame=frame
    gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame=cv2.flip(gray_frame,1)
    cv2.imshow('frame', gray_frame)

    key=cv2.waitKey(33)
    
    if key==ord('q'):
      break

video.release()
cv2.destroyAllWindows()