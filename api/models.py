# app/utils.py
# from torchvision.io import read_image
from torchvision.models import resnet50, ResNet50_Weights

# img = read_image("image.jpg")

# Initialize model with the best available weights
weights = ResNet50_Weights.DEFAULT
model = resnet50(weights=weights)
model.eval()

# Initialize the inference transforms
preprocess = weights.transforms()


def predict_cellphone(img):
    # image = read_image(img)
    
    batch = preprocess(img).unsqueeze(0)
    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    category_name = weights.meta["categories"][class_id]
    return category_name
    # return {'aa':'avar'}



# print(predict_cellphone("image.jpg"))

