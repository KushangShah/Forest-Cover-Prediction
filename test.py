"""
Let's test the model wgucg we created notebook.ipynb and main.py
"""

# import library
import pandas as pd
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")

# Importing data
forest_DF = pd.read_csv("train.csv")
df = forest_DF.copy()

df.drop(columns=['Id'], inplace=True)

X = df.drop('Cover_Type', axis=1)
y = df['Cover_Type']

# import best model
best_model = joblib.load('rf_best_model.pkl')

# Get 5 random rows of features (X)
random_sample_features = X.sample(n=5, random_state=42)
# Get the corresponding true labels (y) for comparison
random_sample_labels = y.loc[random_sample_features.index]

predictions_zero_indexed = best_model.predict(random_sample_features)

# Convert predictions back to original labels (1-7) for user readability
# In main.py, you used: y_train_zero_indexed = y_train - 1
# So, to reverse it: original_prediction = zero_indexed_prediction + 1
predictions_original = predictions_zero_indexed + 1

# Create a DataFrame for comparison
results_df = pd.DataFrame({
    'True_Cover_Type': random_sample_labels.values,
    'Predicted_Cover_Type': predictions_original
}, index=random_sample_labels.index)

# Compare predictions
correct_predictions = (results_df['True_Cover_Type'] == results_df['Predicted_Cover_Type']).sum()


# output
print(f"\n🔬 Testing with {len(random_sample_features)} random samples:")
print("-" * 50)
print("Random Sample Features (Input to Model):\n")
print(random_sample_features)
print("-" * 50)

# --- 5. Display Results ---
print("\nPrediction Results:")
print("-" * 50)
print(results_df)
print("-" * 50)


print(f"Summary: {correct_predictions} out of {len(results_df)} predictions were correct.\n\n")