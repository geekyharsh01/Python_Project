# Importing Torchvision Library that will help in importing Resnet model which
#which will be used to predict whether the input image is cellphone or not.
from torchvision.models import resnet50, ResNet50_Weights
import logging


# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Initialize model with the best available weights
weights = ResNet50_Weights.DEFAULT #wieghts available online are used 

#wieghts of pretrained model resnet50 are used here which are available online.
model = resnet50(weights=weights)
model.eval() # switching model to evaluation mode

# Initialize the inference transforms, this will transform the input image according to the model's wieght.
preprocess = weights.transforms()


def predict_cellphone(img):
    '''
    This is the function which takes image as input and provides the category name "cellular telephone" as output.
    This function is going to be used by the detect_cellphone_endpoint in main.py file 
    '''

    try:
        # Applying Preprocessing on the img and then adding batch dimension.
        batch = preprocess(img).unsqueeze(0) 

        # Predicting using the model created above and then squeezing the output given by the model and applying softmax to get probabilities for each label.
        prediction = model(batch).squeeze(0).softmax(0) 

        # Now getting the class_id correspond to the highest probability value, because the image we provide contains the cellular telephone so its id will be stored in the variable class_id
        class_id = prediction.argmax().item()

        # Now getting the category_name on the basis of class_id, weights here contains the information of weight of pretrained model also the categories used while training the model.
        category_name = weights.meta["categories"][class_id]

        # Now returning the category name
        return category_name
    except Exception as e:
        # Log any exceptions that occur during cellphone prediction
        logger.error(f"Error predicting cellphone: {e} , Error in Model predict_cellphone")
        raise




