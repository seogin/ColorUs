import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm, preprocessing
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

# Path to your data file
data_path = "csv_file/data.csv"


def load_and_preprocess_data(path):
    data = pd.read_csv(path)
    # Handle missing values if any
    data = data.dropna()

    # x = data.drop("label", axis=1)
    x = data.drop(["label"], axis=1)
    y = data["label"]

    # Normalize features
    # x = preprocessing.StandardScaler().fit_transform(x)
    # for col in x:
    #     x[col] = x[col].div(255)

    # print(x)

    return x, y


# 25%
def svm_model():
    x, y = load_and_preprocess_data(data_path)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.1, random_state=42
    )

    model = svm.SVC(kernel="linear", C=2)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    print(accuracy_score(y_test, y_pred))

    return model


# 30.6%
def knn_model():
    x, y = load_and_preprocess_data(data_path)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.1, random_state=42
    )

    model = KNeighborsClassifier(n_neighbors=28)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    print(accuracy_score(y_test, y_pred))

    return model


def random_forest_model(x_train, y_train):
    model = RandomForestClassifier(
        n_estimators=100, min_samples_split=5, min_samples_leaf=1, max_depth=10
    )
    model.fit(x_train, y_train)

    return model


def gradient_boosting_model(x_train, y_train):
    model = GradientBoostingClassifier(
        learning_rate=0.15,
        max_depth=4,
        min_samples_leaf=1,
        min_samples_split=5,
        n_estimators=100,
    )
    model.fit(x_train, y_train)

    return model


def main():
    x, y = load_and_preprocess_data(data_path)
    x_small, x_test, y_small, y_test = train_test_split(
        x, y, test_size=0.1, random_state=42
    )

    svm = svm_model(x_small, y_small)
    rf_model = random_forest_model(x_small, y_small)
    gb_model = gradient_boosting_model(x_small, y_small)

    models = {
        "SVM": svm,
        "Random Forest": rf_model,
        "Gradient Boosting": gb_model,
    }

    for name, model in models.items():
        y_pred = model.predict(x_test)
        print(f"{name} Accuracy: {accuracy_score(y_test, y_pred)}")


if __name__ == "__main__":
    # main()
    svm_model()
    knn_model()
