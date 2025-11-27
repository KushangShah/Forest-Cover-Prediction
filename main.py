"""
I don't want to train all the model over and over again so from the notebook.
it is clear that which model is doing best. 
so i will write pipeline code in this notebook. 
which train and test that specifict model from notebook. 
The best performing model from notebook is - random forest clssification. 

use `test.py` for testing the model
"""

# import library
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import joblib
import warnings
warnings.filterwarnings("ignore")

# import data
forest_DF = pd.read_csv("train.csv")
df = forest_DF.copy()

# missing and duplicated values
miss_value = df.isna().sum()
dupli_value = df.duplicated().sum()

# Removing "Id" column
df.drop(columns=['Id'], inplace=True)

# let's bring cover type to front for better analysis
cover_type = df.pop('Cover_Type')
df.insert(0, 'Cover_Type', cover_type)

# split the data into training and test
X = df.drop('Cover_Type', axis=1)
y = df['Cover_Type']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

y_train_zero_indexed = y_train - 1
y_test_zero_indexed = y_test - 1
y_train = y_train - np.min(y_train)
y_test = y_test - np.min(y_test)

# ml model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train_zero_indexed)
y_pred = rf_model.predict(X_test)

# model evaluation
accuracy = accuracy_score(y_test_zero_indexed, y_pred)
precision = precision_score(y_test_zero_indexed, y_pred, average='weighted')
recall = recall_score(y_test_zero_indexed, y_pred, average='weighted')
f1 = f1_score(y_test_zero_indexed, y_pred, average='weighted')
cm = confusion_matrix(y_test_zero_indexed, y_pred)
cr = classification_report(y_test_zero_indexed, y_pred)

# hyperparameter tuning
from sklearn.model_selection import GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10],
    'min_samples_split': [1, 2, 3],
    'min_samples_leaf': [1, 2]
}
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
hyper_rf_model = grid_search.fit(X_train, y_train_zero_indexed)
best_params = hyper_rf_model.best_params_
best_model = hyper_rf_model.best_estimator_

# prediction
y_pred = best_model.predict(X_test)

# model evaluation (CORRECTED)
accuracy = accuracy_score(y_test_zero_indexed, y_pred)
precision = precision_score(y_test_zero_indexed, y_pred, average='weighted')
recall = recall_score(y_test_zero_indexed, y_pred, average='weighted')
f1 = f1_score(y_test_zero_indexed, y_pred, average='weighted')
cm = confusion_matrix(y_test_zero_indexed, y_pred)
cr = classification_report(y_test_zero_indexed, y_pred)

# save the model
joblib.dump(best_model, 'rf_best_model.pkl')


# output
print(f"\n \
    * Importing library... DONE\n \
    * Importing Data... DONE\n \
        - Missing value in dataset: \n{miss_value}\n \
        - Duplicated value in dataset: {dupli_value}\n \
    * Removing unwanted libraries e.g., Id... DONE\n \
    \n\n{'=-='*45}\n\n \
    * Spliting the dataset into training and testing... DONE\n \
        - X_train: {X_train.shape}\n \
        - X_test: {X_test.shape}\n \
        - y_train: {y_train.shape}\n \
        - y_test: {y_test.shape}\n \
    \n\n{'=-='*45}\n\n \
    * Training the RandomForestClassification with n_estimator=100 and random_state=42... DONE\n \
    * Prediction with Model... DONE\n \
    * Model Evaluation...\n \
        - Accuracy: {accuracy}\n \
        - Precision: {precision}\n \
        - Recall: {recall}\n \
        - F1: {f1}\n \
        - Confusion Matrix:\n {cm}\n \
        - Classification Report:\n {cr}\n \
    \n\n{'=-='*45}\n\n \
    * Performing Hyperparameter tuning... DONE\n \
        - Best Parameters: {best_params}\n \
        - Best Model: {best_model}\n \
    \n\n{'=-='*45}\n\n \
    * Prediction with Model... DONE\n \
        - Accuracy: {accuracy}\n \
        - Precision: {precision}\n \
        - Recall: {recall}\n \
        - F1: {f1}\n \
        - Confusion Matrix:\n {cm}\n \
        - Classification Report:\n {cr}\n \
    \n\n{'=-='*45}\n\n \
    * Saving the model... DONE\n \
    \n\n{'=-='*45}\n\n")