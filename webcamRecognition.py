import cv2


# Loads the XML that contains trained data on +ve and -ve images
cascPath = "haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# access the webcam to start reading the input video for faces
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame of the video
    ret, frame = video_capture.read()

    # converts the frames to grayscale from colored for resource efficiency
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles.
    faces = faceCascade.detectMultiScale(
        gray,                      # input image
        scaleFactor=1.1,           # specify how much the image size is reduced at each image scale
        minNeighbors=5,            # specify how many neighbors each candidate rectangle should have to retain it
        minSize=(30, 30),          # Minimum possible object size. Objects smaller than that are ignored
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # exits out of the program if "q" on keyboard is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
