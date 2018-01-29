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
This script uses hyperopt library for exploration of hyperparameters and sklearn classifiers. Two functions:
 - ```tune(X_train, X_test, y_train, y_test)```, computes and print the best classifier and the related accuracy given the selected input (X_train, X_test) and related labels (y_train, y_test)
 - ```split_and_tune(X, y)```, splits the input data into training and testing
