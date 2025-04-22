
import sys
import os
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB

from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from .FeatureSelection2 import featureselection

class Prediction:
    def get(features, test_file):
        
        alg=RandomForestClassifier()
            
        
        df = pd.read_csv("Employee-Attrition.csv")
        y_train = df['Attrition']
        del df['Attrition']
        X = df[features]
        y = y_train

        clf = alg
        clf.fit(X, y)


        df2 = pd.read_csv(test_file)
        empid=df2['EmpID']
        del df2['EmpID']
    
        X_test = df2[features]
        

        predicted = clf.predict(X_test)
        return list(empid), list(predicted)



if __name__ == "__main__":
    features=featureselection.calc()
    test_file='EmpDetails.csv'

    res=Prediction.get(features, test_file)
    print(res)

    
