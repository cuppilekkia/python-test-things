import cv2, time, pandas
from datetime import datetime

# Convert to gray, flip image and applies gaussian blur
def convertAndFlip(img):
  gray_frame=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_frame=cv2.flip(gray_frame,1)
  gray_frame=cv2.GaussianBlur(gray_frame, (5,5),0)
  return gray_frame 

# Var for the first frame which is the reference of the background
first_frame=None

# capture cam
video=cv2.VideoCapture(0)

count=0
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start", "End"])

# Proc loop
if video.isOpened():
  while True:

    count+=1
    status=0

    # read the frame
    _,fr = video.read()
    # make a gray frame
    gray_frame=convertAndFlip(fr)
    # save the original color frame
    frame=cv2.flip(fr,1)

    # save the first frame in the var
    # for the first 25 frames to avoid the initial dark frames
    if first_frame is None or count < 25:
      first_frame=gray_frame
      continue

    # calculate the delta frame
    delta_frame=cv2.absdiff(first_frame, gray_frame)
    # calculate the threshold frame and give White
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # dilate the threshold frame
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    # find the contours from the thresh frame
    (cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # for each of the contours
    for cont in cnts:
      # skip if below the given area
      if cv2.contourArea(cont) < 10000:
        continue
      # flag relevant movement
      status=1
      # get the moving area bounding box
      (x,y,w,h) = cv2.boundingRect(cont)
      # draw the rectangle on the original frame
      cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    
    # keep track of the flag changes
    status_list.append(status)

    # keep only the last 2 flags
    status_list=status_list[-2:]

    # if obj is entering the frame append timestamp
    if status_list[-1]==1 and status_list[-2]==0:
      times.append(datetime.now())
    # if obj is exiting the frame append timestamp
    if status_list[-1]==0 and status_list[-2]==1:
      times.append(datetime.now())

    # show video feeds
    cv2.imshow('gray', gray_frame)
    cv2.imshow('delta', delta_frame)
    cv2.imshow('thresh', thresh_frame)
    cv2.imshow('color', frame)

    # catch the 'q' key to stop the loop and exit
    key=cv2.waitKey(33)
    if key==ord('q'):
      # append the last timestamp if missing
      if status==1:
        times.append(datetime.now())
      break

# build the dataframe from the times list
for i in range(0, len(times), 2):
  df=df.append({"Start": times[i], "End": times[i+1]}, ignore_index=True)

# save to csv
df.to_csv("times.csv")

video.release()
cv2.destroyAllWindows()