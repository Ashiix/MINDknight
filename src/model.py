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
        #setup data class
        data = Data()
        with open('src/final_data.txt', 'r') as f:
            a_data = ast.literal_eval(f.read()) # set text inside to this var which is now a list of our data
        f.close()
        self.df = pd.DataFrame(a_data)

    def data_format(self): # formatting
        self.train_df, test_df = train_test_split(self.df, test_size=0.20) #splits data into test and train (20% test)
        self.x_train = self.train_df[['VotesFor','VotesAgainst']].copy() # Create a copy of the original df, only using the first two columns
        self.y_train = self.train_df[['Hackers']].copy() # train labels
        self.x_test = test_df[['VotesFor','VotesAgainst']].copy() # test data
    # LOGISTIC REGRESSION!!!!

    def temp(self):
        print(self.x_train[:5])
        print(self.y_train[:5])

    def log_regression(self):
        self.log_reg = LogisticRegression(solver='lbfgs') # define logreg model, and set solver var.
        for i in range(5):
            self.log_reg.fit(self.x_train, self.train_df['Hackers'].str[i])
        self.log_reg.fit(self.x_train, self.y_train) # train model
    #now predict!
    def predict(self):
        self.log_reg.predict(self.x_test) # predict model given test data.
