#https://www.youtube.com/watch?v=h21wMKGs0qs

import cv2
import os
import numpy as np
import csv

cwd = os.getcwd() # get current working direct
haar_classifier_path = cwd + '\\classifier\\haarcascade_frontalface_default.xml' # Path for CascadeClassifier

# pre process image for trainning
def face_detection(test_img):
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY) #convert img to Gray. Easier for classfier
    face_haar_cascade = cv2.CascadeClassifier(haar_classifier_path) # load model for face detection
    faces = face_haar_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=2) # 5:52
    return faces, gray_img

# label image with given key for taining
def label_traning_data(image_path, user_Key):
    faces = []
    faceID = []

    for path, subdirnames, filenames in os.walk(image_path):
        for filename in filenames:
            if filename.startswith("."):
                print("Skipping system file")
                continue
            id = user_Key
            img_path = os.path.join(path, filename)
            print("loading image: ", img_path, " for id:", id)
            test_img = cv2.imread(img_path)
            if test_img is None:
                print("Image not loaded", img_path)
                continue
            faces_rect, gray_img = face_detection(test_img)
            if len(faces_rect) != 1:
                continue # Only single specifed person should be fed
            (x,y,w,h) = faces_rect[0]
            roi_gray = gray_img[y: y+w, x: x+h]
            faces.append(roi_gray)
            faceID.append(int(id))
    print("All images loaded")
    return faces, faceID

# label image based on folder name for taining
def labels_for_traning_data(directory):
    faces = []
    faceID = []

    for path, subdirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("Skipping system file")
                continue
            id = os.path.basename(path)
            img_path = os.path.join(path, filename)
            print("loading image: ", img_path, "id:", id)
            test_img = cv2.imread(img_path)
            if test_img is None:
                print("Image not loaded", img_path)
                continue
            faces_rect, gray_img = face_detection(test_img)
            if len(faces_rect) != 1:
                continue # Only single person are fed
            (x,y,w,h) = faces_rect[0]
            roi_gray = gray_img[y: y+w, x: x+h]
            faces.append(roi_gray)
            faceID.append(int(id))
    print("All images loaded")
    return faces, faceID

# train classifier
def train_classifier(faces, faceID):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(faceID))
    print("Classifer trained")
    return face_recognizer

# update classifier
def update_classifier(faces, faceID, classifier):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create() # initial classifier
    face_recognizer.read(classifier) # Load classifier
    face_recognizer.update(faces, np.array(faceID)) # Update classifier
    print("Classifer updated")
    return face_recognizer  

# draw rect for face detected
def draw_rect(test_img, face):
    (x,y,w,h) = face
    cv2.rectangle(test_img, (x,y), (x+w,y+h), (200,200,39), thickness=2)

# put name on rect
def put_text(test_img, text, x, y):
    cv2.putText(test_img, text, (x,y), cv2.FONT_HERSHEY_DUPLEX, 1, (200,200,39), 2)

# find if name exsited in given dictionary
def find_exsit(user_name, users):
    for key in sorted(users.keys()) :
        if user_name == users[key]:
            return True
    return False

# read the user file
def read_users_list(file_path):
    users = {}
    with open(file_path) as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile)
        for r in reader:
            if not r or not(r[0]) or not(r[1]):
                continue
            users[int(r[0])] = r[1]
    return users

# wirte to the user file
def update_users_list(file_path, users):
    with open(file_path, mode='w') as csvfile:
        fieldnames = ['key', 'value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key in sorted(users.keys()) :
            writer.writerow({'key': key, 'value': users[key]})
    print("User file updated")
    
            
