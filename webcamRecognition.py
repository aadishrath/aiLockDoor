import cv2
from saveUserImage import connection
import os
import random
import string


def saveMain():
    try:
        # Loads the XML that contains trained data on +ve and -ve images
        cascPath = "haarcascade_frontalface_alt.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)

        # access the webcam to start reading the input video for faces
        video_capture = cv2.VideoCapture(0)

        # counter is used for keeping camera connection open for 10 secs
        counter = 0
        while True:
            # Capture frame-by-frame of the video
            ret, frame = video_capture.read()

            # converts the frames to grayscale from colored for resource efficiency
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect different size object in the input image. The detected object is returned as a list of rectangles.
            faces = faceCascade.detectMultiScale(
                gray,  # input image
                scaleFactor=1.1,  # specify how much the image size is reduced at each image scale
                minNeighbors=5,  # specify how many neighbors each candidate rectangle should have to retain it
                minSize=(30, 30),  # Minimum possible object size. Objects smaller than that are ignored
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            # the waitKey function pauses for 1000mSec between each frame input from camera for better quality image
            cv2.waitKey(1000)

            # checks to see if the face tuple has any values stored; yes: face read,  no: face not read
            if len(faces) != 0:
                userId = randomStringDigits(8)
                uploadFile = userId + "_user.png"
                cv2.imwrite(filename=uploadFile, img=frame)  # saves the recognized face image locally
                connection(userId, uploadFile)  # sends the saved image to the firebase database
                video_capture.release()  # closes the camera connection
                cv2.destroyAllWindows()  # closes any windows that are opened
                break
            elif counter == 9:  # no face read for 10sec then executes this elif loop
                break
            counter = counter + 1  # increments counter for elif loop

    # catches any exceptions that terminates the code unexpectedly by keyboard input
    except KeyboardInterrupt:
        exit(0)

    # the final block looks for any image files saved locally, deletes them if found
    finally:
        try:
            os.remove(uploadFile)
        except FileNotFoundError:
            exit(0)


# Creates a random alphanumeric string for unique user id
def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
