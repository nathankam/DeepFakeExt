# Importing the load model function from tensorflow
from tensorflow.keras.models import load_model
import numpy as np


def get_model_info(model_path): 

    model = load_model(model_path)
   
    layers_info = {}
    for layer in model.layers:
        layers_info[layer.name] = {
            'input_shape': layer.input_shape,
            'output_shape': layer.output_shape,
        }

    return layers_info



def process_frontend_image(frontend_image):

    # A function that takes the input image and make it ready for the model
    # Return an image with face detected / cropped / adapted to the model input shape


    return 

def predict_deepfake(deepfake_model, image): 

    # A function that takes the model and the image and return the prediction
    # Return the prediction of the model on the image

    return 

