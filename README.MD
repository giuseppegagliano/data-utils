# Data Utilities
## Importing
### ```mongo-importer.bat```
Copy & run ```mongo-importer.bat``` in the same folder of CSV datasets you want to import.
> Tip 1: Edit MONGO_HOME as the current MongoDB installation path

> Tip 2: Remove ```--headerline``` parameter if datasets don't have headers

## Cleaning
TODO

## Manipulating
### ```add_noise.py``` (WIP)
Adds random points to data

## Tuning



### ```hyperopt_tuner.py```
This script uses hyperopt library to explore sklearn classifiers and the related hyperparameters. Two functions:
 - ```tune(X_train, X_test, y_train, y_test)```, computes and print the best classifier and the related accuracy given the selected input (X_train, X_test) and related labels (y_train, y_test)
 - ```split_and_tune(X, y)```, splits the input data into training and testing

### ```tpot_tuner.py```
This script uses tpot library to explore hyperparameters space and find the best pipeline of cleaning and classification for the specified dataset. Two functions:
  - ```tune(X_train, X_test, y_train, y_test)```, computes and print the best classifier and the related accuracy given the selected input (X_train, X_test) and related labels (y_train, y_test). At the end it produces ```tpot_pipeline.py``` containing the best pipeline.
  - ```split_and_tune(X, y)```, splits the input data into training and testing
  > Tip: to include xgboost among the classifers, you need to install it, for Windows:
   - download package from website http://www.lfd.uci.edu/~gohlke/pythonlibs/#xgboost
   - put the package in directory C:\
   - open anaconda 3 prompt
   - type cd C:\
   - type pip install C:\xgboost-0.6-cp36-cp36m-win_amd64.whl
   - type conda update scikit-learn
