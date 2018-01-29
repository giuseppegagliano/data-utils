from tpot import TPOTClassifier
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris
import time


def split_and_tune(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=.25, random_state=1)
    tune(X_train, X_test, y_train, y_test)
    
def tune(X_train, X_test, y_train, y_test):
    # Construct and fit TPOT classifier
    start_time = time.time()
    tpot = TPOTClassifier(generations=10, verbosity=2)
    tpot.fit(X_train, y_train)
    end_time = time.time()

    # Results
    print('TPOT classifier finished in %s seconds' % (end_time - start_time)) 
    print('Best pipeline test accuracy: %.3f' % tpot.score(X_test, y_test))

    # Save best pipeline as Python script file
    tpot.export('tpot_pipeline.py')

# Test
D = load_iris()
split_and_tune(D.data, D.target)