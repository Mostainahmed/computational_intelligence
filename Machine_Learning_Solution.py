import pandas as pd
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV


def ml_sol():
    train = pd.read_excel("2023_2_modified.xlsx")
    test = pd.read_excel("2023_2_modified.xlsx")

    print(train.Peak[0])

    y_train = train.Peak
    train.drop(['Peak'], axis=1, inplace=True)
    X_train = train

    y_test = test.Class
    test.drop(['Peak'], axis=1, inplace=True)
    X_test = test

    RA = SVR()
    cross_val = GridSearchCV(estimator=RA,
                             param_grid={'max_iter': [-1, 100, 500, 750, 1000]},
                             cv=4)
    cross_val.fit(X_train, y_train)
    pred = cross_val.predict(X_test)

    print("First 5 prediction {}".format(pred[525:]))
    print("Original first five {}".format(y_test[525:]))

    print(mean_absolute_error(y_test, pred))
    print("------------------------------------")
    print(pd.DataFrame(cross_val.cv_results_))
