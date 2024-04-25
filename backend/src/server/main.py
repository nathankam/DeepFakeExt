import base64
from http.client import HTTPException
import io 
import numpy as np
import cv2

# Import our FastAPI library 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import matplotlib.pyplot as plt

from backend.src.services.deepfake import get_model_info


# This is where the API is coded 
app = FastAPI()

# Allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# The root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# A get request endpoint
@app.get("/model_info")
def show_model_info(): 

    model_path = "my-model.h5"

    return get_model_info('my-model.h5')


@app.post("/save_frame")
def save_frame(data: dict):

    print(data.keys())

    # Getting the base64 image data 
    base64_image = data['image'].split(",")[1]

    # Decoding the base64 image data
    image_bytes = base64.b64decode(base64_image)
    image = cv2.imdecode(np.fromstring(image_bytes, dtype=np.uint8), 1)

    # Save the image
    cv2.imwrite('frame.jpg', image)

    return {"status": "success"}
    
