from django.shortcuts import render
import json
import os

# from local repo
# LOCATIONS_PATH = os.path.join(os.path.dirname(__file__), 'C:\studyAbroad\Project\DS Project1\columns.json')

# Load location data
# Define the path to the ML model inside the Django app
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCATIONS_PATH = os.path.join(BASE_DIR, "ml_models", "columns.json")

with open(LOCATIONS_PATH, 'r') as f:
    columns = json.load(f)['data_columns']


def get_loc_json():
    return columns