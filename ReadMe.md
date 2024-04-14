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

- check that dependencies are installed (fastapi / uvicorn)

## Load your model in the data/models folder 

- Copy your *.h5* file in the folder 
- You can put diffferent models there if you want

## Run the Backend Server 

- Open a terminal window 
- Run the following command (copy/paste + enter)

```uvicorn backend.src.server.main:app --reload```

This creates a local host that will enable us to make API calls to our python backend from the frontend (our Chrome Extension). To have a better view at our API endpoints and to check that they work well we can go to *http:localhost:8000/docs*

## Make calls to our API 



