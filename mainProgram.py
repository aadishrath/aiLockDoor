import saveUserImage
import readSavedImage

print("Enter 1 for saving new occupant")
print("Enter 2 for unlocking door")
try:
    userChoice = int(input())
    if userChoice == 1:
        saveUserImage.main()
    elif userChoice == 2:
        readSavedImage.readMain()
    else:
        print("Wrong input. Exiting")
        exit(0)
except ValueError and KeyboardInterrupt:
    print("Error caught. Exiting")
    exit(0)
