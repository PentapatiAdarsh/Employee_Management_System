
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

class Training:
    def train(algo, features):
        
        if algo==1:
            alg=RandomForestClassifier()
        elif algo==2:
            alg=MultinomialNB()
        elif algo==3:
            alg=LinearSVC()
        elif algo==4:
            alg=DecisionTreeClassifier()
        else:
            alg=LogisticRegression()
            
        
        df = pd.read_csv("Employee-Attrition.csv")
        y_train = df['Attrition']
        del df['Attrition']
        
        df2 = pd.read_csv("TestSet.csv")
        y_test = df2['Attrition']
        del df2['Attrition']
        X_test = df2[features]
        
    
        X = df[features]
        #X = df
        y = y_train

        
        clf = alg

        clf.fit(X, y)

    

        predicted = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predicted)*100
        precision = precision_score(y_test, predicted, average="weighted")*100
        recall = recall_score(y_test, predicted, average="weighted")*100
        fscore = f1_score(y_test, predicted, average="weighted")*100

        print("%=",accuracy,precision,recall,fscore)

        return (accuracy,precision,recall,fscore)



if __name__ == "__main__":
    features=featureselection.calc()

    Training.train(1, features)
    Training.train(2, features)
    Training.train(3, features)
    Training.train(4, features)
    Training.train(5, features)

