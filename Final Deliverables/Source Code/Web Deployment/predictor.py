import pickle
import numpy as np
import random
linear_model = pickle.load(open("linear_model.pkl","rb"))
def predict(data):
    crop_features = [x for x in data]
    print(crop_features)
    crop_features[0] = random.randint(0,32)
    crop_features[1] = random.randint(0,645)
    crop_features[2] = int(crop_features[2])
    crop_features[3] = random.randint(0,5)
    crop_features[4] = random.randint(0,123)
    crop_features[5] = float(crop_features[5])
    crop_features = [np.array(crop_features)]
    prediction = linear_model.predict(crop_features)
    return prediction