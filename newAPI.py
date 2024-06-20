import psycopg2
import cv2
from deepface import DeepFace
def getImagePath(id):
    try:
        # Define your connection parameters
        connection = psycopg2.connect(
            user="postgres",
            password="nam30112002",
            host="192.168.1.10",
            port="5432",
            database="graduation_thesis_ver2"
        )

        cursor = connection.cursor()
        # Query to fetch image_path from student table
        cursor.execute(f'SELECT image_path FROM student WHERE id = {id}')
        # Fetch all results
        image_paths = cursor.fetchall()

        return image_paths[0][0]

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # Closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def checkAttendence(imagePath, listID):
    image = cv2.imread(imagePath)

    # Detect faces in image1
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = detector.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

    # Crop faces from image1 and save them
    face_images = []
    for (x, y, w, h) in faces:
        face = image[y:y + h, x:x + w]
        face_images.append(face)

    results = []
    for id in listID:
        ip = getImagePath(id)
        ss = False
        for i, face in enumerate(face_images):
            result = DeepFace.verify(face, ip, model_name='VGG-Face')
            if result['verified']:
                ss = True
                break
        results.append({'id' : id, 'isAttendance': ss})

    return results

#print(checkAttendence("D:/Data/13.jpg", [13]))

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from typing import Dict, Any
import pandas as pd
from deepface import DeepFace
import cv2
import asyncio

app = FastAPI()


class AttendenceRequest(BaseModel):
    imgPath: str
    ids: List[int]

@app.post("/attendence")
async def attendence(request: AttendenceRequest):
    image1_path = request.imgPath
    ids = request.ids
    results = checkAttendence(image1_path, ids)
    return results
