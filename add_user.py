import os
import cv2
import numpy as np
import recognition_functions as fr # import from FaceRecognition_Function.py

cwd = os.getcwd() # get current working direction
### parameter ###
image_desired = 50 # Number of pic desired
cam = cv2.VideoCapture(0) # Initial selected camera
image_path = cwd + '\\new_face\\' # path to store new user's image
classifier_path = cwd + '\\classifier\\classifier.yml' # Path for classifier
users_path = cwd + '\\user_data\\users.csv' # users.csv path
### parameter ###

users = fr.read_users_list(users_path) # read user dictornary

user_name = input("Pleas enter user name: ") # Request user name

# find if user name exsited
while fr.find_exsit(user_name, users) == 1:
    user_name = input("User name exsited, Pleas try again: ") # request new name

# Sort user's dict and find the last users key
new_user_key = sorted(users.keys())[-1] + 1

# Update users dictionary
users[new_user_key] = user_name

###### Take images while one face detected ######
image_saved = 0 # Initial saved image number

while True:
    ret, frame = cam.read() # Take one pic frame as pixal array
    faces_dectected, gray_img = fr.face_detection(frame) # Classify img
    temp = np.copy(frame) # copy frames for bounding box

    for face in faces_dectected: # Draw bounding box
        (x,y,w,h) = face
        roi_gray = gray_img[y:y+h, x:x+h]
        fr.draw_rect(temp, face) # Draw rectengle
        text = str(int(image_saved/image_desired*100)) + '%' + ' completed'
        fr.put_text(temp, text, x, y+h+25) # Top left of the brounding box
    resized_img = cv2.resize(temp, (640,480))
    cv2.imshow("facePOC", resized_img)
    
    if len(faces_dectected) == 1: # If only one face is detected
        cv2.imwrite(image_path + str(image_saved) + ".jpg", frame) # save image
        image_saved = image_saved + 1 # save image counting
       
    if image_saved == image_desired: # Saved image reached desired number
        print("Successful")
        break

    if cv2.waitKey(1) & 0xff == ord('q'): # Quit process
        break

cam.release() # release the usage of camera
cv2.destroyAllWindows()

###### Update classifier ######
faces, faceID = fr.label_traning_data(image_path, new_user_key) # label image for taining
face_recognizer = fr.update_classifier(faces, faceID, classifier_path) # update classifier
face_recognizer.save(classifier_path) # Save classifier

# update users.csv
fr.update_users_list(users_path, users)