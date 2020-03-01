import os
import cv2
import webcamRecognition as wr
import compareImage as ci


# check to see if directory exists
def checkDir():
    if not os.path.exists('./savedImages'):
        os.mkdir('./savedImages')
    return './savedImages'


def main():
    # create directory if it doesn't exist
    path = checkDir()

    # receives the image and image filename
    img, tempFile = wr.main()

    # removes any noise from image taken
    clean_img = cv2.blur(img, (1, 1))

    # checks if the filename exists, creates new name if it does then save file; else saves the files
    if os.path.exists(tempFile):
        userId = randomStringDigits(8)
        tempFile = userId + ".png"
        cv2.imwrite(path + '/' + tempFile, clean_img)  # saves the gray image locally with newly generated name
    else:
        cv2.imwrite(path + '/' + tempFile, clean_img)  # saves the gray image locally with received name


