import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
file_path = '/opt/homebrew/Cellar/hadoop/3.4.1/libexec/etc/hadoop/disease_data_2.csv'
data = pd.read_csv(file_path)

# 1. Handle Missing Data
data = data.dropna()

# 2. Encode Categorical Variables
encoder = LabelEncoder()
data['Gender'] = encoder.fit_transform(data['Gender'])
data['City'] = encoder.fit_transform(data['City'])
data['Disease'] = encoder.fit_transform(data['Disease'])

# 3. Scale Numerical Features
scaler = StandardScaler()
data['Age'] = scaler.fit_transform(data[['Age']])

# 4. Feature Selection and Dimensionality Reduction
features = data.drop(columns=['ID', 'Name', 'Disease'])
target = data['Disease']

# Reduce dimensions with PCA
pca = PCA(n_components=10)  # Retain top 10 components
features_reduced = pca.fit_transform(features)

# 5. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(features_reduced, target, test_size=0.2, random_state=42)

# 6. Train a Stochastic Gradient Descent Classifier
sgd = SGDClassifier(max_iter=1000, tol=1e-3, random_state=42)
sgd.fit(X_train, y_train)

# 7. Evaluate the Model
y_pred = sgd.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"SGD Classifier Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

