import base64
from http.client import HTTPException
import io 
import numpy as np
import cv2

# Import our FastAPI library 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import matplotlib.pyplot as plt

import tensorflow as tf
import face_recognition

from backend.src.services.deepfake import get_model_info


# This is where the API is coded 
app = FastAPI()

# Origins 
origins = [
    "http://localhost",
    "http://localhost:8000"
]


# Allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost", "http://localhost:8000", 
        "chrome-extension://mdekjfmflkkipcindelknmijdcaijiol"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# The root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# A get request endpoint
@app.get("/model_info")
def show_model_info(): 

    model_path = "./backend/data/models/trained_2conv_1dense_2022_1_8_v1.h5"

    return get_model_info(model_path)


@app.post("/process_frame")
def save_frame(data: dict):

    try: 

        # --- SAVING THE FRAME --- 

        # Getting the base64 image data 
        base64_image = data['image_data'].split(",")[1]

        # Decoding the base64 image data
        image_bytes = base64.b64decode(base64_image)
        image = cv2.imdecode(np.fromstring(image_bytes, dtype=np.uint8), 1)

        # Save the image
        cv2.imwrite('frame.jpg', image)



        # --- PROCESS THE FRAME --- 

        # Process the image
        image = image.astype(np.uint8)

        print('>> Image:', image.shape, image.dtype)




        # --- FACE DETECTION ---

        # Face detection 
        face_locations = face_recognition.face_locations(image)

        if not face_locations:
            print('>> No face detected!')
            return {
                "status": "success",
                "message": 'No face detected!',
                "prediction": None,
                "face_image": base64_image
            }
        else:
            print(f'>> {len(face_locations)} face(s) detected!')
        
        # Crop around the first detected face
        top, right, bottom, left = face_locations[0]
        face_image = image[top:bottom, left:right]

        # Save Face Image as B64 encoding for frontend
        _, buffer = cv2.imencode('.jpg', face_image)
        face_image_b64 = base64.b64encode(buffer).decode('utf-8')

        print('>> Face Image:', face_image.shape, face_image.dtype)





        # --- PREPARE THE IMAGE FOR THE MODEL --- 

        # Resize the image
        face_image = cv2.resize(face_image, (28, 28))

        # Normalize the data and expand the dimensions
        face_image = face_image.astype('float32') / 255.0
        face_image = np.expand_dims(face_image, axis=0)
        
        print('>> Face Image for Model:', face_image.shape, face_image.dtype)



        # --- LOAD THE MODEL --- 

        # Load the model
        deepfake_model = tf.keras.models.load_model(
            './backend/data/models/new_model.h5')

        # --- MAKE THE PREDICTION ---

        prediction = deepfake_model.predict(face_image.reshape(1, 28, 28, 3))
        is_deepfake = prediction[0][0] > 0.5

        print('>> Prediction:', prediction[0][0] > 0.5)

        # Message
        message_deepfake = "This is a deepfake!" 
        message_real = "This is a real image!"
        message = message_deepfake if is_deepfake else message_real

        response = {
            "status": "success",
            "message": message,
            "face_image": face_image_b64,
            "prediction": str(is_deepfake)
        }

        return response
    
    except Exception as e:

        print('>> Error:', e)
        return {
            "status": "error",
            "message": str(e),
            "prediction": None,
            "face_image": None
        }


