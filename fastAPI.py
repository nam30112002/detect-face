from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
from face_detect import faceDetect
from recognize import recog
app = FastAPI()

@app.post("/train")
async def train(name: str = Form(...), id: str = Form(...), video_path: str = Form(...)):

    faceDetect(video_path, id, name)
    file_path = r"dataset/users.xlsx"
    return FileResponse(file_path, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

@app.post("recognize")
async def recognize(img_path: str = Form(...)):
    result = recog(img_path)
    return result