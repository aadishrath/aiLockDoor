import face_recognition
import numpy as np


def main(unknownInputImg, savedImg, tolerance=0.6):

    # creates face encodings for comparison
    unknownInputImgEncoding = face_recognition.face_encodings(unknownInputImg, num_jitters=30)
    savedImgEncoding = face_recognition.face_encodings(savedImg, num_jitters=30)

    # saves the list of saved image encodes
    savedEncodingList = []
    for knownEncoding in savedImgEncoding:
        savedEncodingList.append(knownEncoding[0])

    result = []


    # loops over the list of encodings of each input image with 40% match (tolerance of 0.6)
    for unknownEncoding in unknownInputImgEncoding:
        distances = face_recognition.face_distance(savedImgEncoding, unknownEncoding)
        result.append(list(distances <= tolerance))

    return result