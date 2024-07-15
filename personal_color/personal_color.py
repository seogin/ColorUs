import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


# 25%
def svm_model():
    data = pd.read_csv("../csv_file/data.csv")
    x = data.drop("label", axis=1)
    x = preprocessing.normalize(x)
    y = data["label"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

    model = svm.SVC(kernel="linear", C=2)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    
    print(accuracy_score(y_test, y_pred))

    return model


# 30.6%
def knn_model():
    data = pd.read_csv("../csv_file/data.csv")
    x = data.drop("label", axis=1)
    x = preprocessing.normalize(x)
    y = data["label"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

    model = KNeighborsClassifier(n_neighbors=27)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    
    print(accuracy_score(y_test, y_pred))

    return model


def main():
    # svm_model()
    knn_model()


if __name__ == "__main__":
    main()