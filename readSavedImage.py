import cv2
import os
import numpy as np
import webcamRecognition as wr
import compareImage as ci


def readMain():
    try:
        # calls webcam recognition function to get input
        tempImg, tempFile = wr.main()

        # removes any noise from image taken
        tempImg = cv2.blur(tempImg, (1, 1))

        # reads all saved images
        path = './savedImages'

        # saves the stream image locally with received name
        cv2.imwrite(tempFile, tempImg)

        # read the temporarily saved stream image
        unknownInputImg = cv2.imread(tempFile)

        # move to savedImages directory
        os.chdir(path)

        # loops over the saved images 1 by 1 and compares images to unlock/keep locked
        for file in os.listdir('.'):
            savedImg = cv2.imread(file)
            img = ci.main(unknownInputImg, savedImg)
            img = img[0][0]
            print(img)

            if img:
                print("face found")
                return 1
                break
            else:
                print("face not found")
                return 0
                break
    except FileNotFoundError:
        print("No authorized user exists")
        for deleteFile in os.listdir("."):
            if deleteFile.endswith(".png"):
                os.remove(deleteFile)
        exit(0)
    finally:
        try:
            os.chdir('..')
            os.remove("./" + tempFile)
        except FileNotFoundError:
            return 0
            exit(0)


readMain()
