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


@app.post("/createImage")
async def createImage(name: str = Form(...), idd: str = Form(...), video_file: UploadFile = File(...)):
    # Lưu video vào một tệp tạm thời để xử lý
    video_path = f"temp/{video_file.filename}"

    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(video_file.file, buffer)

    faceDetect(video_path, idd, name)

    # Xóa tệp tạm thời sau khi đã xử lý
    os.remove(video_path)

    file_path = r"dataset/users.xlsx"
    json_data = read_excel_to_json(file_path)

    return JSONResponse(content=json_data)

@app.post("/train")
async def train():
    return Train()


@app.post("/recognize")
async def recognize(
       #filename: str = Form(...),
        #msg: str = Form(...),
        file: UploadFile = File(...)
):
    # Create a temporary directory if it doesn't exist
    os.makedirs('temp', exist_ok=True)

    img_path = f"temp/{file.filename}"

    # Save the image file
    with open(img_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Perform image recognition
    result = recog(img_path)

    # Remove the temporary image file after processing
    os.remove(img_path)

    return result