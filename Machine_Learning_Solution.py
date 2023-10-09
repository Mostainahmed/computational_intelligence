import pandas as pd
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV


def ml_sol():
    train = pd.read_excel("2023_2_modified.xlsx")
    test = pd.read_excel("2023_1_modified.xlsx")

    y_train = train.Peak
    train.drop(['Peak'], axis=1, inplace=True)
    X_train = train

    y_test = test.Peak
    test.drop(['Peak'], axis=1, inplace=True)
    X_test = test

    # Convert feature names or columns to strings
    X_train.columns = X_train.columns.astype(str)
    X_test.columns = X_test.columns.astype(str)
    common_columns = X_train.columns.intersection(X_test.columns)
    X_train = X_train[common_columns]
    X_test = X_test[common_columns]

    RA = SVR()
    print("SVR model created:", RA)

    cross_val = GridSearchCV(estimator=RA,
                             param_grid={'max_iter': [-1, 100, 500, 750, 1000]},
                             cv=4)
    print("GridSearchCV object created:", cross_val)

    cross_val.fit(X_train, y_train)
    pred = cross_val.predict(X_test)

    print("######5###########5############5########5###")

    print("First 5 prediction {}".format(pred[525:]))
    print("Original first five {}".format(y_test[525:]))
    print("-----1----------1------------1-------1--")
    print(mean_absolute_error(y_test, pred))
    print("-----2-----------2-----------2--------2-")
    print(pd.DataFrame(cross_val.cv_results_))


ml_sol()
