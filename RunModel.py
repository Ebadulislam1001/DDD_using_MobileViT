import cv2
from ultralytics import RTDETR
import time
import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

video_path = 0
cap = cv2.VideoCapture(video_path)

window_width = 640
window_height = 480
cv2.namedWindow(" model Test", cv2.WINDOW_NORMAL)
cv2.resizeWindow(" model Test", window_width, window_height)
model = RTDETR("best.pt")

sleep_counter = 0
while cap.isOpened():
    # read a frame from the video
    []
    success, frame = cap.read()
    prev_class = 0.0
    try:
        if success:
            results = model.predict(frame, conf=0.5)
            annotated_frame = results[0].plot()
            # display the frame
            cv2.imshow(" model Test", annotated_frame)
            class_label = results[0][0].boxes.cls
            conf_label = results[0][0].boxes.conf
            print("class label :", class_label)
            print("conf_label  :", conf_label)
            if class_label == 1.0 and conf_label > 0.5:
                sleep_counter += 1
                if(sleep_counter >= 10):
                    file_path = "loud_alarm.mp3"
                    play_music(file_path)
                    time.sleep(4)
            else:
                sleep_counter = 0
            prev_class = class_label

            # Break the loop if q is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                print("User pressed 'q'. Exiting loop.")
                break
        # Break the loop if the end of the video is reached
        else:
            print("End of video reached. Exiting loop.")
            break
    except:
        print("Error in processing frame.")
    # Release the video capture object and close the display window

cap.release()
cv2.destroyAllWindows()