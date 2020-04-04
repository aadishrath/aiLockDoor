import os
import cv2
import webcamRecognition as wr
#import compareImage as ci


# check to see if directory exists
def checkDir():
    if not os.path.exists('./savedImages'):
        os.mkdir('./savedImages')
    return './savedImages'


def main(result):
    try:
        # create directory if it doesn't exist
        path = checkDir()

        # receives the image and image filename
        img, tempFile = wr.main(result)

        # removes any noise from image taken
        clean_img = cv2.blur(img, (1, 1))

        # checks if the filename exists, notifies name exists and exits the program; else saves the files
        if os.path.exists(path+'/'+tempFile):
            # print("Name already exists")
            return 0
        else:
            cv2.imwrite(path + '/' + tempFile, clean_img)  # saves the gray image locally with received name
            # print("Created successfully")
        return 1
    except Exception:
        return 0
