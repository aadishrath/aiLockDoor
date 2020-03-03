import saveUserImage
import readSavedImage

# will be removing below print statements for raspberry by
print("Enter 1 for saving new occupant")
print("Enter 2 for unlocking door")


def main():
    # functionality result variable
    output = 0

    try:
        userChoice = int(input())
        if userChoice == 1:
            output = saveUserImage.main()
        elif userChoice == 2:
            output = readSavedImage.readMain()
        else:
            print("Wrong input. Exiting")
    except ValueError and KeyboardInterrupt:
        print("Error caught. Exiting")
    return output


main()
