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


@app.post("/create")
async def createImage(name: str = Form(...), id: str = Form(...), video_path: str = Form(...)):

    faceDetect(video_path, id, name)
    file_path = r"dataset/users.xlsx"
    json_data = read_excel_to_json(file_path)

    return json_data

@app.post("/train")
async def train():
    return Train()


@app.post("/recognize")
async def recognize(img_path: str = Form(...)):
    result = recog(img_path)
    return result