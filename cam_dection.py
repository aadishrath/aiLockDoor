import cv2
import os
import numpy as np
import recognition_functions as fr

cwd = os.getcwd() # get current working direct
### parameter ###
classifier_path = cwd + '\\classifier\\classifier.yml' # clasifier path
users_path = cwd + '\\user_data\\users.csv' # users.csv path
### parameter ###

users = fr.read_users_list(users_path) # Assign Name

face_recognizer = cv2.face.LBPHFaceRecognizer_create() # Creat classifier
face_recognizer.read(classifier_path) # Load classifier

captured_image = cv2.VideoCapture(0) # Open Camera

while True:
    ret, test_img = captured_image.read() # Capture Frame

    faces_dectected, gray_img = fr.face_detection(test_img) # Classify img

    for face in faces_dectected: # Draw bounding box
        (x,y,w,h) = face
        roi_gray = gray_img[y:y+h, x:x+h]
        label, confidence = face_recognizer.predict(roi_gray) # return Name & Confidence
        print("confidence:", int(confidence))
        print("label:", label)
        fr.draw_rect(test_img, face) # Draw rectengle
        predicted_name = users[label]
        if(confidence == 0): # higher number lower likely, 0 means exact match
            continue
        text = predicted_name + ' ' + str(100 - int(confidence)) + '%'
        fr.put_text(test_img, text, x, y+h+25) # Top left of the brounding box
    resized_img = cv2.resize(test_img, (640,480))
    cv2.imshow("facePOC", resized_img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

captured_image.release()
cv2.destroyAllWindows()