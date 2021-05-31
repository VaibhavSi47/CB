import cv2

cap = cv2.VideoCapture(0)
cascade_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here

    frame = cv2.cvtColor(frame, 0)
    detections = cascade_classifier.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)
    if len(detections) > 0:
        (x, y, w, h) = detections[0]
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # for (x,y,w,h) in detections:
    # 	frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Display the resulting frame
    cv2.imshow('ti', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
