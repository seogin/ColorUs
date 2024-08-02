import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn import svm, preprocessing
from sklearn.metrics import accuracy_score


def load_and_preprocess_data(path):
    data = pd.read_csv(path)
    # Handle missing values if any
    data = data.dropna()

    # x = data.drop(["label"], axis=1)
    # y = data["label"]

    tone_x = data.drop(
        [
            "tone",
            "saturation",
            "brightness",
            "v1",
            # "v2",
            # "v3",
            # "v4",
            "s1",
            # "s2",
            # "s3",
            # "s4",
        ],
        axis=1,
    )

    saturation_x = data.drop(
        [
            "tone",
            "saturation",
            "brightness",
            "v1",
            # "v2",
            # "v3",
            # "v4",
            "b1",
            # "b2",
            # "b3",
            # "b4",
        ],
        axis=1,
    )

    brightness_x = data.drop(
        [
            "tone",
            "saturation",
            "brightness",
            "s1",
            # "s2",
            # "s3",
            # "s4",
            "b1",
            # "b2",
            # "b3",
            # "b4",
        ],
        axis=1,
    )

    tone = data["tone"]
    saturation = data["saturation"]
    brightness = data["brightness"]

    return tone_x, tone, saturation_x, saturation, brightness_x, brightness


def svm_model(x_train, y_train, x_test, y_test, k="linear", c=11):
    model = svm.SVC(kernel=k, C=c)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    print(accuracy_score(y_test, y_pred))

    return model


def knn_model(x_train, y_train, x_test, y_test, n=9):
    model = KNeighborsClassifier(n_neighbors=n)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    print(accuracy_score(y_test, y_pred))

    return model


def lr_model(x_train, y_train, x_test, y_test):
    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)

    # acc = model.score(x_test, y_test)
    # print(acc)

    predictions = model.predict(x_test)
    y = pd.DataFrame(y_test).values
    count = 0

    for x in range(len(predictions)):
        if round(predictions[x]) == y[x][0]:
            count += 1

    print(count / len(predictions))

    return model


def random_model(x_train, y_train, x_test, y_test):
    model = RandomForestClassifier(
        n_estimators=100, min_samples_split=2, min_samples_leaf=1, max_depth=None
    )
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    print(accuracy_score(y_test, y_pred))

    return model


def gradient_model(x_train, y_train, x_test, y_test):
    model = GradientBoostingClassifier(
        max_depth=3,
        min_samples_leaf=2,
        min_samples_split=2,
        n_estimators=50,
    )
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    print(accuracy_score(y_test, y_pred))

    return model


def main():
    data_path = "data.csv"
    tx, ty, sx, sy, bx, by = load_and_preprocess_data(data_path)

    tx_train, tx_test, ty_train, ty_test = train_test_split(
        tx, ty, test_size=0.1, random_state=42
    )

    sx_train, sx_test, sy_train, sy_test = train_test_split(
        sx, sy, test_size=0.1, random_state=42
    )

    bx_train, bx_test, by_train, by_test = train_test_split(
        bx, by, test_size=0.1, random_state=42
    )

    svm_model(tx_train, ty_train, tx_test, ty_test)
    knn_model(tx_train, ty_train, tx_test, ty_test)
    lr_model(tx_train, ty_train, tx_test, ty_test)
    random_model(tx_train, ty_train, tx_test, ty_test)
    gradient_model(tx_train, ty_train, tx_test, ty_test)
    # svm_model(sx_train, sy_train, sx_test, sy_test)
    # knn_model(sx_train, sy_train, sx_test, sy_test)
    # lr_model(sx_train, sy_train, sx_test, sy_test)
    # svm_model(bx_train, by_train, bx_test, by_test)
    # knn_model(bx_train, by_train, bx_test, by_test)
    # lr_model(sx_train, sy_train, sx_test, sy_test)


if __name__ == "__main__":
    main()
