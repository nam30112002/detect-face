import os
import shutil

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
from face_detect import faceDetect
from recognize import recog
from train import Train
from typing import Dict, Any
import pandas as pd
app = FastAPI()


def read_excel_to_json(file_path: str) -> Dict[str, Any]:
    # Đọc dữ liệu từ file Excel
    df = pd.read_excel(file_path)

    # Chuyển đổi DataFrame thành JSON
    json_data = df.to_dict(orient="records")

    return json_data


import cv2

async def createImage(name: str = Form(...), id: str = Form(...), video_file: UploadFile = Form(...)):

    # Lưu video vào một tệp tạm thời để xử lý
    video_path = f"temp/{video_file.filename}"
    with open(video_path, "wb") as video_buffer:
        shutil.copyfileobj(video_file.file, video_buffer)

    cap = cv2.VideoCapture(video_path)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            # Xử lý frame ở đây với hàm faceDetect
            faceDetect(frame, id, name)
        else:
            break

    cap.release()

    # Xóa tệp tạm thời sau khi đã xử lý
    os.remove(video_path)

    file_path = r"dataset/users.xlsx"
    json_data = read_excel_to_json(file_path)

    return json_data

@app.post("/train")
async def train():
    return Train()


@app.post("/recognize")
async def recognize(img_file: UploadFile = Form(...)):
    # Lưu hình ảnh vào một tệp tạm thời để xử lý
    img_path = f"temp/{img_file.filename}"
    with open(img_path, "wb") as img_buffer:
        shutil.copyfileobj(img_file.file, img_buffer)

    result = recog(img_path)  # Sử dụng hàm recog để nhận dạng hình ảnh

    # Xóa tệp tạm thời sau khi đã xử lý
    os.remove(img_path)

    return result