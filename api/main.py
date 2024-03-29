# app/main.py
from fastapi import FastAPI, File, UploadFile
from models import predict_cellphone

app = FastAPI()

list_of_image= []



@app.get("/find")
def get_image(index_of_image: int):
    prediction = predict_cellphone(list_of_image[index_of_image])
    temporary_variable = index_of_image
    return {"prediction": prediction,
            "strning":list_of_image[index_of_image]}



@app.post("/predict/")
def predict(file: UploadFile = File(...)):
    # with open(file.phone_image, "wb") as buffer:
    #     buffer.write(file.read())

    list_of_image.append(file)
    prediction = predict_cellphone(file)
    return {"prediction": prediction ,
            "thi": file}
