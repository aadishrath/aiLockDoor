import firebase_admin
from firebase_admin import credentials, firestore, storage


def connection(userId, imageFile):
    # Use the application default credentials
    cred = credentials.Certificate("./privKey.json")
    firebase_admin.initialize_app(cred)

    # create connection to firebase storage
    db = firestore.client()
    bucket = storage.bucket('facialrecognitionlock.appspot.com')

    # uploading images to the storage
    imageBlob = bucket.blob(imageFile)
    imageBlob.upload_from_filename(imageFile)

    doc_ref = db.collection(u'AccessList').document(u'owners')
    doc_ref.set({
        u'Id': userId,
        u'Filename': imageFile
    })
