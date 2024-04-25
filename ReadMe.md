# Project Name

## Loading the project from github 

### Get the code

- Open a new project in VSCode
- On the main page click the 'Clone a GitHub Repository' option 
- Copy paste the repository url: *git@github.com:nathankam/DeepFakeExt.git*
- Select a location for the project on your computer

### Set the project on your computer to match the remote repository on GitHub 

- git remote add origin *https://github.com/nathankam/DeepFakeExt*

## Run the project

We need to install the librairies that will be used by our backend. 
- Uvicorn: Running a local server 
- FastAPI: API library
- Pillow: Handling images 
- Numpy: Handling images as array of numbers 
- OpenCV for computer vision 


### Install Libraries

- In terminal 
```pip install uvicorn```
```pip install fastapi```
```pip install matplotlib```
```pip install numpy```
```pip install opencv-python```

- Or 
```pip install requirements.txt```



### Install face_recognition 

The face recognition library uses C++, another programming language to recognize faces. To use it, our machine needs a package called cmake, to download that package we will use homebrew. If you don't have homebrew on your computer you can follow these steps. We also need some tools that xcode provides (xcode should already be installed on you mac)

- Install HomeBrew (Package installer)
```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```

- Check that homebrew is installed correctly 
```brew --version```

- If brew is installed successfully -> Install cmake (needed for the face_recognition library)
```brew install cmake```
```xcode-select --install```

- Check that cmake is installed (you might need to close VSCode and re-open it)
```cmake --version```

- Finally 
```pip install face_recognition```


## Load your model in the data/models folder 

- Copy your *.h5* file in the folder 
- You can put diffferent models there if you want

## Run the Backend Server 

- Open a terminal window 
- Run the following command (copy/paste + enter)

```uvicorn backend.src.server.main:app --reload```

This creates a local host that will enable us to make API calls to our python backend from the frontend (our Chrome Extension). To have a better view at our API endpoints and to check that they work well we can go to *http:localhost:8000/docs*

## Make calls to our API 



