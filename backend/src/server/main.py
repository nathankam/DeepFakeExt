from backend.src.services.deepfake import get_model_info

# Import our FastAPI library 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


