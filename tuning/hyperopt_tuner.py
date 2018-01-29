# HYPERPARAMETER & CLASSIFIER MODEL TUNING

from __future__ import print_function
from sklearn import datasets
from sklearn.model_selection import train_test_split
from hyperopt import tpe
import hpsklearn
import sys
from sklearn import preprocessing
from sklearn import utils

# https://github.com/hyperopt/hyperopt-sklearn

def split_and_tune(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=.25, random_state=1)
    tune(X_train, X_test, y_train, y_test)
    
def tune(X_train, X_test, y_train, y_test):
    estimator = hpsklearn.HyperoptEstimator(
        preprocessing=hpsklearn.components.any_preprocessing('pp'),
        classifier=hpsklearn.components.any_classifier('clf'),
        algo=tpe.suggest,
        trial_timeout=300,  # seconds
        max_evals=10,
        seed=1
    )

    print('\n====Demo classification on Iris dataset====', file=sys.stderr)
    iterator = estimator.fit_iter(X_train, y_train)
    next(iterator)
    n_trial = 0
    while len(estimator.trials.trials) < estimator.max_evals:
        iterator.send(1)  # -- try one more model
        n_trial += 1
        print('Trial', n_trial, 'loss:', estimator.trials.losses()[-1], file=sys.stderr)
        #hpsklearn.scatter_error_vs_time(estimator)
        #hpsklearn.demo_support.bar_classifier_choice(estimator)
    estimator.retrain_best_model_on_full_data(X_train, y_train)
    print('Test accuracy:', estimator.score(X_test, y_test), file=sys.stderr)
    print('Best model:',estimator.best_model(), file=sys.stderr)
    print('====End of demo====', file=sys.stderr)

# Test
D = datasets.load_iris()
split_and_tune(D.data, D.target)