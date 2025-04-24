import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectKBest, f_classif
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


class featureselection:
    def calc():
        df = pd.read_csv("Employee-Attrition.csv")
        
        y = df["Attrition"]  
        del df["Attrition"]
        X = df
        data_top = df.columns
        print(data_top)

        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train an Extra Trees classifier
        clf = ExtraTreesClassifier(n_estimators=100, random_state=42)
        clf.fit(X_train, y_train)

        # Get feature importances
        feature_importances = clf.feature_importances_
        print(feature_importances)

        # Print feature importances
        print("Feature Importances:")
        for i, importance in enumerate(feature_importances):
            print(f"Feature {i+1}: {importance}")

        feat_importances = pd.Series(feature_importances, index=X.columns)

        dic = dict(feat_importances.nlargest(10))
        kys = list(dic.keys())
        vls = list(dic.values())

        import random
        colors = ['#{:06x}'.format(random.randint(0, 0xFFFFFF)) for _ in range(len(kys))]

        plt.figure(figsize=(16, 6))
        plt.bar(kys, vls, color=colors)
        for i in range(len(kys)):
            plt.text(i, vls[i], kys[i], ha='center', va='bottom')
        plt.savefig('D:\\Django\\EMS\\webapp\\static\\assets\\images\\graph.png')
        plt.clf()

        print(kys, vls)

        d = dict(feat_importances.nlargest(10))
        l = [ll for ll in d]
        print(l)

        # Plot feature importances
        plt.figure(figsize=(10, 6))
        plt.bar(range(len(feature_importances)), feature_importances, color='skyblue')
        plt.xlabel('Feature Index')
        plt.ylabel('Feature Importance')
        plt.title('Feature Importances')
        plt.xticks(range(len(feature_importances)), range(1, len(feature_importances) + 1))
        plt.grid(True)
        plt.savefig('D:\\Django\\EMS\\webapp\\static\\assets\\images\\graph2.png')
        plt.clf()

        return kys


if __name__ == "__main__":
    print(featureselection.calc())
