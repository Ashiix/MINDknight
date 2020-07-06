#!/usr/bin/env python3

# Import libraries
import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from src.data import Data
import seaborn as sns

# Create class Model
class Model:
    def __init__(self):
        # Create packet dataframe
        data = Data()
        data.read_log()
        #self.train = pd.DataFrame(data.packets)
        #print(self.train.head())

    def log_regression(self):
        pass

    def visualize(self):
        sns.heatmap(self.train.isnull())
