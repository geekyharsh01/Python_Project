# app/main.py
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from models import predict_cellphone
from io import BytesIO
import numpy as np

app = FastAPI()

list_of_image = []

async def read_imagefile(file) -> Image.Image:
    contents = await file.read()  # Use await to properly read the file
    image = Image.open(BytesIO(contents))
    return image

@app.get("/find")
async def get_image(index_of_image: int):

    prediction = predict_cellphone(list_of_image[index_of_image])
    return {"prediction": prediction}

@app.post("/detect_cellphone/")
async def detect_cellphone_endpoint(file: UploadFile = File(...)):
    image = await read_imagefile(file)  # Use await since read_imagefile is an async function

    list_of_image.append(image)
    print("appended into the array")
    prediction = predict_cellphone(image)
    return {"prediction": prediction}
