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

import cv2

import face_recognition

def process_frontend_image(frontend_image, target_size=(32, 32)):
    # Load the image
    image = cv2.imread(frontend_image)
    
    # change color from cv to face recog
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # detect faces in the image
    face_locations = face_recognition.face_locations(rgb_image)
    
    # If no face  return None
    if not face_locations:
        return None
    
    # crop  around the first detected face
    top, right, bottom, left = face_locations[0]
    face_image = image[top:bottom, left:right]
    
    # resize the cropped face image to the target size
    resized_face_image = cv2.resize(face_image, target_size)
    
    return resized_face_image



def predict_deepfake(deepfake_model, image):
    
    image = image.astype('float32') / 255.0
    # reshape the image for the input shape of the model
    image = np.expand_dims(image, axis=0)

    prediction = deepfake_model.predict(image)

    return prediction


# Load the trained deepfake model
deepfake_model = load_model('/Users/fionavitali/Downloads/DeepFakeExt/backend/data/models/trained_2conv_1dense_2022_1_8_v1.h5')  # Replace with the path to your model file

# Load the input image
input_image = cv2.imread('image')  # this should be the input image from the youtube

# process the input image
processed_image = process_frontend_image(input_image)

if processed_image is not None:
    # get the prediction
    prediction = predict_deepfake(deepfake_model, processed_image)

    print("Prediction:", prediction)
else:
    print("No face detected in the image.")
