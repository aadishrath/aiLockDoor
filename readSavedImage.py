import cv2
import os
import numpy as np
import webcamRecognition as wr
import compareImage as ci
import datetime


def readMain():
    try:
        # calls webcam recognition function to get input
        tempImg, tempFile = wr.main("temp")
        
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
            try:
                img = img[0][0]
                print(img)
            except IndexError:
                img = False

            if img:
                f = open(r"/home/pi/Desktop/test/aiLockDoor/Logs.txt",'a')
                f.write("[%s] Face entry allowed \n" %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                f.close()
                print("Valid User")
                return 1
                break
            else:
                f = open(r"/home/pi/Desktop/test/aiLockDoor/Logs.txt",'a')
                f.write("[%s] Face entry denied \n" %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                f.close()
                print("Not Valid User")
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
