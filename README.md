# Deploying a Machine Learning Model on Heroku with FastAPI

This is the final project for the third module of
[Machine Learning DevOps Engineer Nanodegree](https://www.udacity.com/course/machine-learning-dev-ops-engineer-nanodegree--nd0821)
on [Udacity](https://www.udacity.com/).

The objective of this project is to train a model and deploy it with a FastAPI hosted on Heroku.

Link for the repository: https://github.com/mfurquimdev/nd0821-c3-starter-code  \
Link for heroku app: https://mfurquim-ml-fastapi.herokuapp.com


## Getting started

At the root of the project, there's the [environment.yml](environment.yml) necessary for setting up the
`ml_model_fastapi` environment using conda. To execute the project, install and activate the environment,
download the dvc files and run the [main.py](main.py) script:

```bash
conda env create -f environment.yml
conda activate ml_model_fastapi
dvc pull
./main.py
```

The `main.py` script will start a [uvicorn](https://www.uvicorn.org/) with the server on port 5000.
To make a GET request, execute the following curl command.
The response will be a dictionary with the greeting `"Hello World!"`.

```bash
curl --request GET --url http://localhost:5000
{"greeting":"Hello World!"}
```

To make a POST request, either execute the [infer_curl_request.sh](infer_curl_request.sh) or the
[infer_request.py](infer_request.py) script. The response will be a dictionary with the inferred salary.

```bash
./infer_request.py
{"salary":"<=50K"}
```

## Unit tests

To run the unit tests, execute the following command inside the `ml_model_fastapi` conda environment.

```bash
PYTHONPATH=${PWD}:${PYTHONPATH} pytest -s -vv --failed-first tests
```

The necessary fixtures are defined at [tests/conftest.py](tests/conftest.py), such as retrieving the train and test
data, the model artifacts (trained model, encoder, and label binarizer), and the census data.

There's a couple of tests for the root endpoint. One to test the success and other to test the failure case which is
triggered by a boolean `fail` query parameter.

There are four test cases for the machine learning functions: `TestTrainModel`, `TestInference`,
`TestComputeModelMetrics`, and `TestData`.

Finally, there are eight tests for the `/infer` endpoint. One that make sure that GET requests are not allowed.
Two tests that complains if there's no data in the body. Three tests that guarantee the age (continuous feature)
receives a value within its allowed range (non empty, non negative and less than 150). One test to guarantee the
education (categorical feature) receives an expected value defined at [src/infer/enum.py](src/infer/enum.py). And the
last test is a success case.

## API

The code for the API is defined inside the [src](src) directory and it is following the MVC architecture pattern.

### Root

```txt
src/root/
└── view.py
```

For the `/` (root) endpoint, there's only one `view.py` script which defines the greeting returned by the endpoint.


### Infer

```txt
src/infer/
├── controller.py
├── enum.py
├── model.py
└── view.py
```

A more complete structure is defined for the `/infer` endpoint.
There's only one POST route defined in the `view.py` and two models (Input and Output) defined in the `model.py`.
The `controller.py` has a few more functions to help with creating the pandas DataFrame from the input data in the
request, running the inference, and converting the inference output to the expected request response.
Lastly, the `enum.py` defines all the possible values for the categorical features.


## Required files

The required image files described on the [rubric](https://review.udacity.com/#!/rubrics/4875/view) are located at
[imgs](imgs):


```txt
imgs/
├── continuous_deloyment.png
├── continuous_integration.png
├── example.png
├── live_get.png
└── live_post.png
```

The [model_card.md](model_card.md) is on the root directory.
The trained model along with its other artifacts (encoder and label_binarizer) are located at [model](model):

```txt
model_card.md
model/
├── encoder.pkl
├── label_binarizer.pkl
└── model.pkl
```

The dataset with its profiling are located at [data](data):

```txt
data/
├── census.csv
└── census.html
```
