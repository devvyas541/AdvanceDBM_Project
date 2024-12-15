import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load dataset
file_path = '/Users/devvyas16/Documents/disease_data_2.csv'
data = pd.read_csv(file_path)

# 1. Handle Missing Data
data = data.dropna()  # Drop rows with missing values (can be adjusted based on the dataset)

# 2. Encode Categorical Variables
# Encode 'Gender' and 'City'
encoder = LabelEncoder()
data['Gender'] = encoder.fit_transform(data['Gender'])
data['City'] = encoder.fit_transform(data['City'])

# Encode 'Disease' (Target Variable)
data['Disease'] = encoder.fit_transform(data['Disease'])

# 3. Scale Numerical Features
scaler = StandardScaler()
data['Age'] = scaler.fit_transform(data[['Age']])

# 4. Feature Selection
# Exclude 'ID' and 'Name' as they are not useful for prediction
features = data.drop(columns=['ID', 'Name', 'Disease'])
target = data['Disease']

# 5. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Save Processed Data
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)

print("Preprocessing completed. Processed datasets saved.")
