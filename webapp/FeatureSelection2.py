import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split



class featureselection:
    def calc():
        df = pd.read_csv("Employee-Attrition.csv")
        
        y = df["Attrition"]  
        del df["Attrition"]
        X=df
        data_top = df.columns
        print(data_top)

                
        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a random forest classifier
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X_train, y_train)

        # Get feature importances
        feature_importances = clf.feature_importances_
        print(feature_importances)

        # Print feature importances
        feat_importances = pd.Series(clf.feature_importances_, index=X.columns)
        
        dic=dict(feat_importances.nlargest(14))
        kys=list(dic.keys())
        vls=list(dic.values())




        return kys

if __name__=="__main__":
    print(featureselection.calc())
