# Machine Learning API using FastAPI
Developing a Machine Learning API (Application Programming Interface) using FastAPI.

[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![MIT licensed](https://img.shields.io/badge/license-mit-blue?style=for-the-badge&logo=appveyor)](./LICENSE)
![Python](https://img.shields.io/badge/python-3.9-blue.svg)

## Introduction


This project aims to help us to discover how to create an API that might be requested to interact with an ML model. This is an essential solution when we seek to keep a model architecture secret or to make it available to users already having an API. By creating this API, and deploying it, our model can also receive requests using the internet protocol.


## Description

<!-- 
[FastAPI](https://fastapi.tiangolo.com/) # 
-->

There is a minimal API demo with [FastAPI](https://fastapi.tiangolo.com/), which serves as a standard to make sure that everything works correctly. 
In effect, this API, thus allows us to interact with a Machine Learning model, that is to say:
- Pass data through a request;
- Get the data in using the API;
- Apply the necessary processing;
- Submit the processed data to the ML model to make the predictions;
- Process the predictions obtained and return them as the API's response to the input request.

## Project Tasks

Consequently, our tasks will be to;

1.  Build an ML model to predict the [Sepsis](https://www.kaggle.com/datasets/chaunguynnghunh/sepsis?select=README.md)(**Data set here**). This ML shall have a pipeline/function that takes inputs and make accurate predictions.

2.  Build an API using Fast API, to embed the ML model built. Our API will be able to  work correctly, taking inputs multiple inputs and returning all the related predictions



## Seting-up

Installing the required packages to be able to run the evaluation locally.

We are required to have [`Python 3`](https://www.python.org/) on our system (**a Python version lower than 3.10**). This will enable us ton clone the given repo and being at the repo's `root :: repository_name> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

## Action Plan

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.



## Runing FastAPI

- Run the demo apps (being at the repository root):
        
  FastAPI:
    
    - Demo

          uvicorn src.demo_01.api:app --reload 

    <!-- - Salary prediction

          uvicorn src.salary.api:app --reload  -->




## Resources
Here are some ressources you would read to have a good understanding of FastAPI :
- [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
- [Video - Building a Machine Learning API in 15 Minutes ](https://youtu.be/C82lT9cWQiA)
- [FastAPI for Machine Learning: Live coding an ML web application](https://www.youtube.com/watch?v=_BZGtifh_gw)
- [Video - Deploy ML models with FastAPI, Docker, and Heroku ](https://www.youtube.com/watch?v=h5wLuVDr0oc)
- [FastAPI Tutorial Series](https://www.youtube.com/watch?v=tKL6wEqbyNs&list=PLShTCj6cbon9gK9AbDSxZbas1F6b6C_Mx)
- [Http status codes](https://www.linkedin.com/feed/update/urn:li:activity:7017027658400063488?utm_source=share&utm_medium=member_desktop)




## Author

-Isaac Mawuli Fumey
