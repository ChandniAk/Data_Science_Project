import json
import pickle
import numpy as np
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, Sqft, bedrooms):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = bedrooms
    x[1] = Sqft
    if loc_index >= 0:
        x[loc_index] = 1
    xp=  round(__model.predict([x])[0], 2)
    return xp


def get_location_names():
    return __locations

def load_save_artifacts():
    print("loading saved artifacts......start")
    global __locations
    global __data_columns
    global __model
    with open("columns.json", 'r') as f:
       __data_columns = json.load(f)['data_columns']
       __locations = __data_columns[2:]

    with open("pakistan_home_price_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loaded saved-----done")


if __name__ == '__main__':
    load_save_artifacts()
    print(get_location_names())
    print(get_estimated_price("gulshan-e-ravi, lahore, punjab", 2000, 3))

    print(get_location_names())