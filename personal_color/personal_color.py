import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Path to your data file
data_path = "csv_file/data.csv"


def load_and_preprocess_data(path):
    data = pd.read_csv(path)
    # Handle missing values if any
    data = data.dropna()

    x = data.drop(["season"], axis=1)
    y = data["season"]

    return x, y


def random_forest_model(x_train, y_train):
    model = RandomForestClassifier(
        n_estimators=50, min_samples_split=2, min_samples_leaf=1, max_depth=None
    )
    model.fit(x_train, y_train)

    return model


def main():
    x, y = load_and_preprocess_data(data_path)
    model = random_forest_model(x, y)

    with open("personalColor.pickle", "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    main()
