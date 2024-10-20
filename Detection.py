import cv2

# init classifier
classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Access Web-camera
video_capture = cv2.VideoCapture(0)

def detect_face(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(green_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

# Apply face detection on web-camera's frames
while True:
    result, video_frame = video_capture.read() # read frames from the web-camera

    if result is False:
        break   # stop is the frame is not read successfully

    faces = detect_face(video_frame) # use the function on the video frame

    cv2.imshow("Face Detection", video_frame) # display the frame in the window named Face Detection

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
