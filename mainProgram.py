import webcamRecognition
import readImagesFromDb

print("Enter 1 for saving new occupant")
print("Enter 2 for unlocking door")

userChoice = int(input())
if userChoice == 1:
    webcamRecognition.saveMain()
elif userChoice == 2:
    readImagesFromDb.readMain()
else:
    exit(0)
