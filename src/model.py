#!/usr/bin/env python3

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from src.data import Data
import ast

# Create class Model
class Model:
    def __init__(self):
        #setup
        data = Data()
        #data.read_log()
        with open('src/final_data.txt', 'r') as f:
            a_data = ast.literal_eval(f.read())
        f.close()
        self.df = pd.DataFrame(a_data)

    def data_format(self):
        train_df, test_df = train_test_split(self.df, test_size=0.25) #splits data into test and train
        # new = old[['A', 'C', 'D']].copy()
        self.x_train = train_df[['VotesFor','VotesAgainst']].copy()
        self.y_train = train_df[['Hackers']].copy()
        self.x_test = test_df[['VotesFor','VotesAgainst']].copy()
    # LOGISTIC REGRESSION!!!!
    def log_regression(self):
        self.log_reg = LogisticRegression(solver='lbfgs')
        self.log_reg.fit(self.x_train, self.y_train)
    #now predict!
    def predict(self):
        self.log_reg.predict(self.x_test)
