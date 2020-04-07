import cv2
import os
import random
import string
import sys


def main(result):
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
                minNeighbors=3,  # specify how many neighbors each candidate rectangle should have to retain it
                minSize=(100, 100),  # Minimum possible object size. Objects smaller than that are ignored
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            # the waitKey function pauses for 1000mSec between each frame input from camera for better quality image
            cv2.waitKey(1000)

            # checks to see if the face tuple has any values stored; yes: face read,  no: face not read
            if len(faces) != 0:
                for (x, y, w, h) in faces:
                    r = max(w, h) / 2
                    centerx = x + w / 2
                    centery = y + h / 2
                    nx = int(centerx - r)
                    ny = int(centery - r)
                    nr = int(r * 2)

                    faceimg = frame[ny:ny+nr, nx:nx+nr]
                    lastimg = cv2.resize(faceimg, (64, 64))
                    cv2.imwrite("faceImg.png", lastimg)

                # userId = randomStringDigits(8)
                # fName = input("Enter your first name: ")
                fName = result
                tempFile = fName + ".png"
                faceImg = cv2.imread(r'./faceImg.png')

                # separate the R, G, and B channels
                red_channel = faceImg[:, :, 0]
                green_channel = faceImg[:, :, 1]
                blue_channel = faceImg[:, :, 2]

                # use the following formula to obtain a gray scale image
                gray_image = 0.2989 * red_channel + 0.5870 * green_channel + 0.1140 * blue_channel

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
            os.remove("./faceImg.png")
        except FileNotFoundError and UnboundLocalError:
            exit(0)
    return gray_image, tempFile


# # Creates a random alphanumeric string for unique user id
# def randomStringDigits(stringLength=6):
#     """Generate a random string of letters and digits """
#     lettersAndDigits = string.ascii_letters + string.digits
#     return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
