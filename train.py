import cv2
import os
import numpy as np
import PIL.Image as Image

# import PIL as Image

path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")


def getImagesAndLabels(path):
    imagePaths = []
    for f in os.listdir(path):
        if f.endswith('.xls') or f.endswith('.xlsx'):
            continue
        if f.endswith('.mp4'):
            continue
        for l in os.listdir(os.path.join(path, f)):
            imagePaths.append(os.path.join(path, f, l))

    faceSamples = []
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
        img_numpy = np.array(PIL_img, 'uint8')
        id = int(imagePath.split("\\")[1][-1])
        faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id)

    return faceSamples, ids


def Train():
    try:
        faces, ids = getImagesAndLabels(path)
        recognizer.train(faces, np.array(ids))

        # Save the model into trainer/trainer.yml
        recognizer.write('trainer/trainer.yml')
        # Trả về một thông báo thành công hoặc giá trị khác để biết rằng quá trình đã hoàn thành
        return "Model trained successfully"
    except Exception as e:
        # Xử lý lỗi ở đây, ví dụ: in ra thông báo lỗi
        print("An error occurred:", e)
        return "An error occurred during training"
