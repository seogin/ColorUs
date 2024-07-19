import pandas as pd
from sklearn.model_selection import (
    train_test_split,
    RandomizedSearchCV,
    StratifiedKFold,
)
from sklearn import svm, preprocessing
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.decomposition import PCA
from scipy.stats import uniform

# Path to your data file
data_path = "./csv_file/data_hist.csv"


def load_and_preprocess_data(path):
    data = pd.read_csv(path)
    # Handle missing values if any
    data = data.dropna()

    x = data.drop("label", axis=1)
    y = data["label"]

    # Normalize features
    x = preprocessing.StandardScaler().fit_transform(x)

    return x, y


def svm_random_search(x_train, y_train, cv):
    svc = svm.SVC()
    parameters = {
        "kernel": ["linear", "rbf"],
        "C": uniform(0.1, 10),
        "gamma": ["scale", "auto"],
    }
    model = RandomizedSearchCV(
        svc,
        parameters,
        n_iter=10,
        cv=cv,
        scoring="accuracy",
        n_jobs=-1,
        random_state=42,
    )
    model.fit(x_train, y_train)
    return model


def random_forest_random_search(x_train, y_train, cv):
    rf = RandomForestClassifier()
    parameters = {
        "n_estimators": [50, 100],
        "max_depth": [None, 10, 20],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2],
    }
    model = RandomizedSearchCV(
        rf, parameters, n_iter=10, cv=cv, scoring="accuracy", n_jobs=-1, random_state=42
    )
    model.fit(x_train, y_train)
    return model


def gradient_boosting_random_search(x_train, y_train, cv):
    gb = GradientBoostingClassifier()
    parameters = {
        "n_estimators": [50, 100],
        "learning_rate": uniform(0.01, 0.2),
        "max_depth": [3, 4],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2],
    }
    model = RandomizedSearchCV(
        gb, parameters, n_iter=10, cv=cv, scoring="accuracy", n_jobs=-1, random_state=42
    )
    model.fit(x_train, y_train)
    return model


def main():
    x, y = load_and_preprocess_data(data_path)

    # Use only 50% of the dataset for initial hyperparameter tuning
    x_small, x_test, y_small, y_test = train_test_split(
        x, y, test_size=0.1, random_state=42
    )

    # Use fewer cross-validation splits
    cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

    svm_model = svm_random_search(x_small, y_small, cv)
    rf_model = random_forest_random_search(x_small, y_small, cv)
    gb_model = gradient_boosting_random_search(x_small, y_small, cv)

    models = {
        "SVM": svm_model,
        "Random Forest": rf_model,
        "Gradient Boosting": gb_model,
    }

    for name, model in models.items():
        y_pred = model.predict(x_test)
        print(f"{name} Best Parameters: {model.best_params_}")
        print(f"{name} Accuracy: {accuracy_score(y_test, y_pred)}")


if __name__ == "__main__":
    main()
