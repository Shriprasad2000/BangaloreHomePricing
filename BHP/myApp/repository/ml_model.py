from django.shortcuts import render
import pickle
import os

# from local repo
# MODEL_PATH = r"C:\studyAbroad\Project\DS Project1\bangalore_home_prices_model.pickle"


# Load the ML model once
# Define the path to the ML model inside the Django app
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml_models", "bangalore_home_prices_model.pickle")

# Open the file properly in read-binary mode
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)


def get_ML_model():
    return model