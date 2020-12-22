import cv2

video = cv2.VideoCapture("rtsp://192.168.1.10:554/user=admin&password=admin&channel=1&stream=0.sdp?")
#"rtsp://admin:admin@192.168.1.10:80/user=admin&password=admin&channel=1&stream=0.sdp?"

try:
    while(1):
        ref, frame = video.read()
        cv2.imshow('VIDEO', frame)
        cv2.waitKey(1)
    
except Exception as e:
    print(e)