import cv2
from ultralytics import RTDETR

video_path = 0
cap = cv2.VideoCapture(video_path)

window_width = 640
window_height = 480
cv2.namedWindow(" model Test", cv2.WINDOW_NORMAL)
cv2.resizeWindow(" model Test", window_width, window_height)
model = RTDETR('best.pt')

while cap.isOpened():

    #read a frame from the video
    success, frame = cap.read()

    if success: 
        results = model.predict(frame, conf=0.5)
        annotated_frame = results[0].plot()
        #display the frame
        cv2.imshow(" model Test", annotated_frame)

        #Break the loop if q is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        #Break the loop if the end of the video is reached
        break
    #Release the video capture object and close the display window

cap.release()
cv2.destroyAllWindows()
#print