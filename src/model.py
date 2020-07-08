#!/usr/bin/env python3

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.datasets import make_regression
from src.data import Data
import ast
import pylab as pl

# Create class Model
class Model:
    def __init__(self):
        #setup data class
        data = Data()

        def empty_check(dict):
            if dict:
                return False
            else:
                return True

        with open('final_data.txt', 'r') as f:
            a_data = ast.literal_eval(f.read()) # set text inside to this var which is now a list of our data
            a_data = [d for d in a_data if d]


        f.close()
        self.df = pd.DataFrame(a_data)
        self.df.dropna()
        self.df.isna()
        print(self.df)
        #print(self.df)

    def data_format(self): # formatting
        self.train_df, self.test_df = train_test_split(self.df, test_size=0.25) #splits data into test and train (20% test)
        self.x_train = self.train_df[['VotesFor0','VotesFor1','VotesFor2','VotesFor3','VotesFor4','VotesAgainst0','VotesAgainst1','VotesAgainst2','VotesAgainst3','VotesAgainst4']].copy() # Create a copy of the original df, only using the first two columns
        self.y_train = self.train_df[['Hackers']].copy() # train labels
        self.x_test = self.test_df[['VotesFor0','VotesFor1','VotesFor2','VotesFor3','VotesFor4','VotesAgainst0','VotesAgainst1','VotesAgainst2','VotesAgainst3','VotesAgainst4']].copy() # test data
        self.y_test = self.test_df[['Hackers']].copy()

    # LOGISTIC REGRESSION!!!!

    def temp(self):
        print(self.x_train[:5])
        print(self.y_train[:5])
        print(self.x_test)


    def log_regression(self):
        self.train_df.fillna(0)
        for i in range(5):
            self.train_df['Hackers'].str[i].fillna(0)
            #print(type(self.train_df['Hackers'].str[i]))
        self.log_reg = LogisticRegression(solver='lbfgs') # define logreg model, and set solver var.
        # for i in range(5): # WORKING ______-------_______-----
        #     results = self.log_reg.fit(self.x_train, self.train_df['Hackers'].str[i])
        self.results0 = self.log_reg.fit(self.x_train, self.train_df['Hackers'].str[0])
        self.results1 = self.log_reg.fit(self.x_train, self.train_df['Hackers'].str[1])
        self.results2 = self.log_reg.fit(self.x_train, self.train_df['Hackers'].str[2])
        self.results3 = self.log_reg.fit(self.x_train, self.train_df['Hackers'].str[3])
        self.results4 = self.log_reg.fit(self.x_train, self.train_df['Hackers'].str[4])

    #now predict!
    def predict(self):
        pass
        # self.log_reg.predict(self.x_test) # predict model given test data. # WORKING
        y_pred0 = self.results0.predict(self.x_test)
        y_pred1 = self.results1.predict(self.x_test)
        y_pred2 = self.results2.predict(self.x_test)
        y_pred3 = self.results3.predict(self.x_test)
        y_pred4 = self.results4.predict(self.x_test)

        print(y_pred0)
        print(y_pred1)
        print(y_pred2)
        print(y_pred3)
        print(y_pred4)

        #extract coulmns, set as column0, coulmn1, etc.
        # each column is a list
        # loop through both the list and the prediction array, compare the values, if they are

        #extact columns
        #for i in range len()

        # for value in y_pred0:
        #     if value == 1:
        #         print("test")
