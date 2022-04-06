import numpy as np
import pandas as pd
from IPython.display import display
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import accuracy_score

ncaaRead = pd.read_csv(r"/Users/kennyburzynski/Desktop/Python/cbb (1).csv")
NCAA = pd.DataFrame(ncaaRead)
display(NCAA)
print(type(NCAA))
print(NCAA.dtypes)

class MultivariateLinearRegression:
    def __init__(self):
        self.__weights = None

    def fit(self, x, y):
        x = np.concatenate( (x, np.expand_dims(np.ones(x.shape[0]), axis= 0).T), axis = 1)
        self.__weights = np.dot(np.dot(np.linalg.inv(np.dot(x.T,x)),x.T),y)
    def predict(self, x):
        x = np.concatenate((x, np.expand_dims(np.ones(x.shape[0]), axis= 0).T), axis=1)
        return np.dot(x, self.__weights)

class MatrixRegressor:
    def __init__(self):
        self.linearModels = None

    def fit(self, x, y):
        linearModels = [0] * y.shape[1]
        for targets in range(y.shape[1]):
            linearModels[targets] = MultivariateLinearRegression()
            linearModels[targets].fit(x,y[:,targets])
            self.linearModels = linearModels

    def predict(self, x):
        predictions = []
        for models in self.linearModels:
            predictions.append(models.predict(x))
        return np.array(predictions).T

    def score(self, x, y):
        predictions = np.round(self.predict(x), decimals= 0)
        #predictions = to_categorical(predictions)
        #print(y.tolist())
        return accuracy_score(y, predictions)

print(MatrixRegressor)