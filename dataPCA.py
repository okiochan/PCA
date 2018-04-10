import matplotlib.pyplot as plt
import numpy as np
import scipy.misc
import math
from sklearn import datasets

class IrisData:
    def GetData(self):
        iris = datasets.load_iris()
        X = iris.data
        y = iris.target
        return X,y

class RandomData:
    def GetData(self):
        l = 50
        real = 2
        X = np.random.randn(l,real)
        a = np.random.randn(real)
        y = np.zeros(l)
        for i in range(l):
            y[i] = a.dot(X[i,:])
        # fake parameters
        Xp = np.concatenate((X,2*X,3*X),axis=1)
        return Xp, y

class DataBuilder:
    def Build(self, name):
        if name == "iris":
            x, y = IrisData().GetData()
            return x, y
        elif name == "random":
            x, y = RandomData().GetData()
            return x, y
        else:
            assert("Unknown data")