import os
import datetime

def main(result):
    # reads all saved images

    path = './savedimages'

    # move to savedImages directory
    os.chdir(path)

    # user enters the name to delete from the authorized user list
    #name = input("Enter name to be removed: ")
    name = result

    fileName = name + '.png'

    # As file at filePath is deleted now, so we should check if file exists or not not before deleting them
    if os.path.exists(fileName):
        os.remove(fileName)
        return 1
    else:
        # print("Can not delete the file as it doesn't exists")
        return 0
    print("Updated Logs")

    path = '..'
    os.chdir(path)


