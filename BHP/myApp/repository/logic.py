# Function to predict price
from .data_loader import get_loc_json
from .ml_model import get_ML_model
import numpy as np

columns = get_loc_json()
model = get_ML_model()

def predict_price(location, sqft, bhk, bath):
    try:
        loc_index = columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1

    return model.predict([x])