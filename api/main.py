# Importing all the important Libraries
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO

#importing predict_cellphone function from the models.py here 
from models import predict_cellphone

# Initialize FastAPI instance
app = FastAPI()
# Initialize an empty list to store uploaded images
list_of_image = []

# Define an async function to read an image file
async def read_imagefile(file) -> Image.Image:
    contents = await file.read()  # Use await to properly read the file asynchrously
    image = Image.open(BytesIO(contents)) # Opening the image using PIL's Image module
    return image



@app.get("/find")
async def get_image(index_of_image: int):

    prediction = predict_cellphone(list_of_image[index_of_image])
    return {"prediction": prediction}


# Define a POST endpoint to detect cellphone in an uploaded image
@app.post("/detect_cellphone/")
async def detect_cellphone_endpoint(file: UploadFile = File(...)):
    '''
    Asynchronous function used to detect the cellphone , here in this function first the image uploaded is read and then used the predict_cellphone function created in the models.py file is used to get whether the image contains the cellphone or not.
    '''


    # Read the uploaded image asynchronously using read_imagefile function
    image = await read_imagefile(file)  # Use await since read_imagefile is an async function

    # Append the image to the list_of_image
    list_of_image.append(image)

    # Make a prediction for cellphone detection using predict_cellphone function
    prediction = predict_cellphone(image)
    
    # Return the prediction result as a JSON response
    return {"prediction": prediction}
