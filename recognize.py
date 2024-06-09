import cv2
import numpy as np
import os
import pandas as pd
import PIL.Image as Image

def recog(path):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = 'haarcascade/haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    #iniciate id counter
    id = 0

    # names related to ids: example ==> Marcelo: id=1,  etc
    excel_path = "dataset/users.xlsx"
    df = pd.read_excel(excel_path)
    list = {}

    # Iterate over rows in the DataFrame
    for index, row in df.iterrows():
        list[row['id']] = row['name']

    print("Dictionary of id-name pairs:", list)

    img = cv2.imread(path)

    (height, width) = img.shape[:2]
    minW = width / 5
    minH = height / 5
    #path = input('Enter image path: ')



    PIL_img = Image.open(path).convert('L')  # convert it to grayscale
    img_numpy = np.array(PIL_img, 'uint8')
    faces = faceCascade.detectMultiScale(img_numpy)

    result = set()
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(img_numpy[y:y + h, x:x + w])

        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 100):
            name = list[id]
            confidence = "  {0}%".format(round(100 - confidence))
            result.add((name, id))

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

    cv2.destroyAllWindows()
    print(result)
    return result

#recog("D:/lmao/detect-face/dataset/User20200400/20200400.1.jpg")