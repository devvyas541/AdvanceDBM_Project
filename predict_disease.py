# Save the trained model and PCA object
joblib.dump(sgd, 'sgd_model.pkl')
joblib.dump(pca, 'pca_object.pkl')
print("Model and PCA object saved.")

# Step 2: Predict Diseases for New Dataset
# Load the trained model and PCA object
sgd_model = joblib.load('sgd_model.pkl')
pca_model = joblib.load('pca_object.pkl')

# Load new dataset
new_file_path = '/Users/devvyas16/Documents/new_dataset.csv'
new_data = pd.read_csv(new_file_path)

# Drop the Disease column if present
if 'Disease' in new_data.columns:
    new_data = new_data.drop(columns=['Disease'])

# Encode categorical variables in the new dataset
new_data['Gender'] = encoder.transform(new_data['Gender'])
new_data['City'] = encoder.transform(new_data['City'])

# Scale numerical features
new_data['Age'] = scaler.transform(new_data[['Age']])

# Apply PCA for dimensionality reduction
new_features_reduced = pca_model.transform(new_data)

# Predict diseases
predicted_diseases = sgd_model.predict(new_features_reduced)

# Add predictions to the dataset
new_data['Predicted_Disease'] = predicted_diseases

# Save the predictions to a new file
new_data.to_csv('/Users/devvyas16/Documents/new_dataset_with_predictions.csv', index=False)
print("Predictions saved to new_dataset_with_predictions.csv")