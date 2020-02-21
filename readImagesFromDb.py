import cv2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def readMain():
    # Use the application default credentials
    cred = credentials.Certificate("./privKey.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    users_ref = db.collection(u'AccessList')
    docs = users_ref.stream()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
    # # Get user supplied values
    # imagePath = "/Users/adi/Downloads/McMaster/Sem 6/Sr Project/facialRecognition/aiLockDoor/1.png"
    # cascPath = "/Users/adi/Downloads/McMaster/Sem 6/Sr Project/facialRecognition/aiLockDoor/haarcascade_frontalface_default.xml"
    #
    # # Create the haar cascade
    # faceCascade = cv2.CascadeClassifier(cascPath)
    #
    # # Read the image
    # image = cv2.imread(imagePath)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #
    # # Detect faces in the image
    # faces = faceCascade.detectMultiScale(
    #     gray,
    #     scaleFactor=1.1,
    #     minNeighbors=5,
    #     minSize=(30, 30)
    # )
    #
    # print("Found {0} faces!".format(len(faces)))
    #
    # # Draw a rectangle around the faces
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #
    # cv2.imshow("Faces found", image)
    # cv2.waitKey(0)
