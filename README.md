# AdvanceDBM_Project
1. # Project: Disease Prediction and Analysis Using Big Data and Machine Learning

## Overview
This project leverages Big Data technologies and machine learning techniques to predict diseases based on symptoms and provide analytical insights using visualizations. Built on Hadoop’s HDFS and PySpark, the project demonstrates the integration of distributed data processing with advanced machine learning workflows.

---

## Workflow

### 1. Data Preparation
1. **Dataset Collection**:
   - Data includes attributes like Age, Gender, City, Symptoms, and the corresponding Disease.
2. **Storage**:
   - The dataset is uploaded and stored in HDFS for distributed processing.
3. **Access**:
   - PySpark is used to read and manipulate the dataset directly from HDFS.

### 2. Preprocessing
1. **Handling Missing Values**: Dropped rows with missing data.
2. **Encoding**:
   - Categorical variables like Gender, City, and Disease are encoded using LabelEncoder.
3. **Scaling**:
   - Numerical features such as Age are scaled using StandardScaler.
4. **Dimensionality Reduction**:
   - PCA is applied to reduce the feature space to the top 10 principal components for faster computation.

### 3. Model Training
1. **Model Selection**:
   - A Stochastic Gradient Descent (SGD) classifier is used for its efficiency in large datasets.
2. **Training Process**:
   - The model is trained using the preprocessed dataset.
3. **Evaluation**:
   - Accuracy and classification reports are generated to validate model performance.

### 4. Model Saving
- The trained model is saved for reuse, enabling predictions on new data without retraining.

### 5. Prediction
1. **New Dataset**:
   - A new dataset with symptom attributes is uploaded.
   - The Disease column is removed before prediction.
2. **Loading Model**:
   - The saved model is loaded using joblib.
3. **Prediction**:
   - Diseases for the new dataset are predicted and saved for analysis.

### 6. Analytics and Visual Insights
1. **Objectives**:
   - Derive insights from the predicted results.
2. **Visualizations**:
   - Age group analysis: Disease trends across different age groups.
   - Disease distribution by city: Identify cities with higher cases of specific diseases.
   - Gender-based disease trends: Analyze disease prevalence by gender.
   - Symptom correlation: Heatmaps to show symptom-disease relationships.
   - Other custom visualizations.
3. **Tools**:
   - Matplotlib and Seaborn for plotting visualizations.

### 7. Challenges
1. **Overfitting**:
   - Addressed using regularization and class balancing.
2. **Resource Limitations**:
   - Leveraged Hadoop’s distributed storage and PySpark’s processing capabilities.
3. **Model Training**:
   - Managed large-scale data processing with Spark.

### 8. Conclusion
1. **Achievements**:
   - Developed a scalable, efficient disease prediction system.
   - Created actionable insights through visual analytics.
2. **Future Work**:
   - Incorporate real-time streaming data for predictions.
   - Explore advanced deep learning models for higher accuracy.
   - Enhance visualizations for interactive analysis.

---

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Hadoop Setup**:
   - Ensure HDFS is configured and running.
   - Upload datasets to HDFS:
     ```bash
     hdfs dfs -put <local_path_to_dataset> <hdfs_path>
     ```
4. **Run Preprocessing and Model Training**:
   - Submit the PySpark job:
     ```bash
     spark-submit --master yarn sgdregress.py
     ```
5. **Prediction**:
   - Use the trained model for predictions:
     ```bash
     spark-submit --master yarn predict_disease.py
     ```
6. **Visualization**:
   - Generate visualizations locally:
     ```bash
     python3 analysispic.py
     ```

---



