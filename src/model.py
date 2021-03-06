#!/usr/bin/env python3

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from src.data import Data
import ast
import pylab as pl


class Model:
    def __init__(self):
        data = Data()

        def empty_check(dict):
            if dict:
                return False
            else:
                return True

        with open('final_data.txt', 'r+') as f:
            # set text inside to this var which is now a list of our data
            a_data = ast.literal_eval(f.read())
            a_data = [d for d in a_data if d]

        self.df = pd.DataFrame(a_data)
        self.df.dropna()
        self.df.isna()

    def data_format(self):
        self.train_df, self.test_df = train_test_split(self.df, test_size=0.25)
        self.x_train = self.train_df[['VotesFor0', 'VotesFor1', 'VotesFor2', 'VotesFor3', 'VotesFor4', 'VotesAgainst0', 'VotesAgainst1',
                                      'VotesAgainst2', 'VotesAgainst3', 'VotesAgainst4']].copy()
        self.y_train = self.train_df[['Hackers']].copy()
        self.x_test = self.test_df[['VotesFor0', 'VotesFor1', 'VotesFor2', 'VotesFor3', 'VotesFor4',
                                    'VotesAgainst0', 'VotesAgainst1', 'VotesAgainst2', 'VotesAgainst3', 'VotesAgainst4']].copy()
        self.y_test = self.test_df[['Hackers']].copy()

    def log_regression(self):
        self.train_df.fillna(0)
        for i in range(5):
            self.train_df['Hackers'].str[i].fillna(0)
        self.log_reg = LogisticRegression(solver='lbfgs')
        self.results0 = self.log_reg.fit(
            self.x_train, self.train_df['Hackers'].str[0])
        self.results1 = self.log_reg.fit(
            self.x_train, self.train_df['Hackers'].str[1])
        self.results2 = self.log_reg.fit(
            self.x_train, self.train_df['Hackers'].str[2])
        self.results3 = self.log_reg.fit(
            self.x_train, self.train_df['Hackers'].str[3])
        self.results4 = self.log_reg.fit(
            self.x_train, self.train_df['Hackers'].str[4])

    def analysis(self):
        pass
        y_pred0 = self.results0.predict(self.x_test)
        y_pred1 = self.results1.predict(self.x_test)
        y_pred2 = self.results2.predict(self.x_test)
        y_pred3 = self.results3.predict(self.x_test)
        y_pred4 = self.results4.predict(self.x_test)

        y_true0 = []
        y_true1 = []
        y_true2 = []
        y_true3 = []
        y_true4 = []

        # Extract list from hackers columns
        for i in range(len(self.y_test)):
            val = self.y_test.iloc[i]["Hackers"]
            y_true0.append(val[0])
            y_true1.append(val[1])
            y_true2.append(val[2])
            y_true3.append(val[3])
            y_true4.append(val[4])

        # Preprocess arrays to lists
        y_pred0 = y_pred0.tolist()
        y_pred1 = y_pred1.tolist()
        y_pred2 = y_pred2.tolist()
        y_pred3 = y_pred3.tolist()
        y_pred4 = y_pred4.tolist()

        # Accuracy
        acc0 = accuracy_score(y_true0, y_pred0)
        acc1 = accuracy_score(y_true1, y_pred1)
        acc2 = accuracy_score(y_true2, y_pred2)
        acc3 = accuracy_score(y_true3, y_pred3)
        acc4 = accuracy_score(y_true4, y_pred4)
        # Average accuracy
        avg_acc = (acc0 + acc1 + acc2 + acc3 + acc4) / 5

        # Precision
        prec0 = precision_score(y_true0, y_pred0)
        prec1 = precision_score(y_true1, y_pred1)
        prec2 = precision_score(y_true2, y_pred2)
        prec3 = precision_score(y_true3, y_pred3)
        prec4 = precision_score(y_true4, y_pred4)
        # Average precision
        avg_prec = (prec0 + prec1 + prec2 + prec3 + prec4) / 5

        # Recall
        rec0 = recall_score(y_true0, y_pred0)
        rec1 = recall_score(y_true1, y_pred1)
        rec2 = recall_score(y_true2, y_pred2)
        rec3 = recall_score(y_true3, y_pred3)
        rec4 = recall_score(y_true4, y_pred4)

        # Average recall
        avg_rec = (rec0 + rec1 + rec2 + rec3 + rec4) / 5

        # F1 score
        # Combine true lists and prediction lists into two lists

        f1_true = []
        f1_pred = []

        for i in range(len(self.y_test)):
            val = self.y_test.iloc[i]["Hackers"]
            f1_true.append(val[0])
            f1_true.append(val[1])
            f1_true.append(val[2])
            f1_true.append(val[3])
            f1_true.append(val[4])

        for i in y_pred0:
            f1_pred.append(i)
        for i in y_pred1:
            f1_pred.append(i)
        for i in y_pred2:
            f1_pred.append(i)
        for i in y_pred3:
            f1_pred.append(i)
        for i in y_pred4:
            f1_pred.append(i)

        f1 = f1_score(f1_true, f1_pred, average='binary')

        print("\nModel Analytics:")
        print("Accuracy (avg.): ", round(avg_acc, 4))
        print("Precision (avg.): ", round(avg_prec, 4))
        print("Recall (avg.): ", round(avg_rec, 4))
        print("F1 Score: ", f1)
