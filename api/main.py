# Importing all the important Libraries
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO
import logging

#importing predict_cellphone function from the models.py here 
from models import predict_cellphone

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Initialize FastAPI instance
app = FastAPI()
# Initialize an empty list to store uploaded images
list_of_prediction = []

# Define an async function to read an image file
async def read_imagefile(file) -> Image.Image:
    """
    An asynchronous function to read an image file uploaded through FastAPI.

    Parameters:
    - file: The uploaded image file.

    Returns:
    - Image.Image: The PIL Image object representing the uploaded image.
    """
    try:
        # Read the contents of the uploaded file asynchronously
        contents = await file.read()  

        # Open the image using PIL's Image module from the read contents
        image = Image.open(BytesIO(contents)) 

        # Return the PIL Image object representing the uploaded image
        return image
    except Exception as e:
        # Log any exceptions that occur during image reading
        logger.error(f"Error reading image file: {e}")
        raise


@app.get("/detected_cellphone")
async def get_prediction(index_of_image: int)->dict :
    """
    An endpoint to retrieve the prediction for an image at a specified index, using the list initiated above named list_of_prediction

    Parameters:
    - index_of_image (int): The index of the image prediction to retrieve.

    Returns:
    - dict: A JSON response containing the prediction for the specified image index.
    """
    try:
        # Calculate the length of the prediction list
        length_of_list = len(list_of_prediction)

        # Check if the index is within the range of available predictions
        if index_of_image < length_of_list:
            # If the index is within range, return the prediction for the specified image
            return {"prediction": list_of_prediction[index_of_image]}
        # If the index is out of range, return a message indicating that it is out of range.
        return {"index": "out of range"}
    except Exception as e:
        # Log any exceptions that occur during prediction retrieval
        logger.error(f"Error retrieving prediction: {e}")
        raise



# Define a POST endpoint to detect cellphone in an uploaded image
@app.post("/detect_cellphone/")
async def detect_cellphone_endpoint(file: UploadFile = File(...)) ->dict:
    '''
    Asynchronous function used to detect the cellphone. Here in this function first the image uploaded is read and then used the predict_cellphone function created in the models.py file is used to get whether the image contains the cellphone or not.

    Parameters:
    - file (UploadFile): The uploaded image file.

    Returns:
    - dict: A JSON response containing the prediction result.
    '''


    try:
        # Read the uploaded image asynchronously using read_imagefile function
        image = await read_imagefile(file)  

        # Make a prediction for cellphone detection using predict_cellphone function
        prediction = predict_cellphone(image)

        # Appending the prediction of the input image to the list
        list_of_prediction.append(prediction)
        
        # Return the prediction result as a JSON response
        return {"prediction": prediction}
    except Exception as e:
        # Log any exceptions that occur during cellphone detection
        logger.error(f"Error Reading image file or detecting cellphone: {e}")
        raise
