import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cross_validation import train_test_split


def dataPreprocess(dataset,int(test_size=0.8),int(random_state=0),feature_scaling=False):
    if ".csv" not in dataset:
        return("CSV format not applied to dataset, Try again")
    dataset = pd.read_csv(dataset)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, len(dataset.columns)-1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size, random_state)
    if feature_scaling==True:
        sc_X = StandardScaler()
        X_train = sc_X.fit_transform(X_train)
        X_test = sc_X.transform(X_test)
        sc_y = StandardScaler()
        y_train = sc_y.fit_transform(y_train)
    return X_train,y_train,X_test,y_test
