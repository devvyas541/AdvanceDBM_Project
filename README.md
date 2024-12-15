# 🌟 Disease Prediction and Analytics Project 🚀

Welcome to **Disease Prediction and Analytics**, where **Big Data** meets **Machine Learning** to improve healthcare one prediction at a time. 🩺📊 Buckle up as we dive into how this project helps predict diseases and uncover visual insights—all powered by **Hadoop**, **PySpark**, and advanced ML techniques! ⚡

---

## 🛠️ **Tech Stack**
- **Big Data**: Hadoop & HDFS 🗂️
- **Processing**: PySpark 🔥
- **Machine Learning**: Scikit-learn 🤖
- **Visualization**: Matplotlib & Seaborn 🎨

---

## 🗽️ **Pipeline Overview**

🔹 **Data Source**: Input raw datasets into HDFS.  
🔹 **Preprocessing**: Clean and encode features using PySpark.  
🔹 **ML Training**: Build a predictive model using SGD Classifier.  
🔹 **Prediction**: Use the trained model to predict diseases for unseen datasets.  
🔹 **Analytics**: Generate insightful visualizations to explore trends and patterns.

🌟 **Visual Overview**:  
➡️ **Raw Data** ➡️ **HDFS** ➡️ **PySpark Processing** ➡️ **ML Training** ➡️ **Prediction & Insights** 🚀

---

## ⚙️ **How to Run the Project**

### 💾 Prerequisites:
1. 🔷 Python 3.8+  
2. 🕉️ Required Libraries: 
   ```bash
   pandas==1.5.3
   numpy==1.24.1
   scikit-learn==1.2.2
   matplotlib==3.7.2
   seaborn==0.12.2
   pyspark==3.5.3

   ```
3. 📂 Set up Hadoop & HDFS with PySpark integration.
4. Get Dataset from https://drive.google.com/file/d/1I6EL5rz9W5zuoBp-2d9MjrkxUn2k1yt9/view?usp=drive_link

### 🏁 Steps:
1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-repo/disease-prediction
   cd disease-prediction
   ```

2. **Preprocess the dataset**:
   ```bash
   spark-submit preprocess.py
   ```

3. **Train the ML model**:
   ```bash
   spark-submit train_model.py
   ```

4. **Make predictions on new data**:
   ```bash
   spark-submit predict.py --input new_data.csv --output predictions.csv
   ```

5. **Generate visual insights**:
   ```bash
   python analytics.py
   ```

---

## 🗊 **Analytics & Visual Insights**

🌟 **Discover healthcare trends**:  
1. **Age Group Analysis**: Compare disease frequency among age groups.  
2. **City-wise Trends**: Identify hotspots for common illnesses.  
3. **Gender-based Patterns**: Uncover gender-specific health insights.  

🎉 **Example Outputs**: *(Sample placeholders below)*  
```plaintext
 📈 Age vs Disease
 🔵 City Disease Distribution
 🔶 Gender Analysis Pie Chart
```

---

## 🎯 **Challenges Faced**
- **Overfitting**: Balanced by PCA and feature scaling.  
- **Resource Constraints**: Optimized PySpark execution.  
- **Integration**: Bridged Hadoop and ML workflows seamlessly.  

---

## 🌟 **Key Achievements**
👉 Efficient disease prediction using SGD Classifier.  
👉 Scalable Big Data pipeline with PySpark and HDFS.  
👉 Stunning visual insights to aid healthcare decisions.  

---

## 🚀 **Future Scope**
- **Enhancements**: Incorporate real-time data.  
- **Deep Learning**: Leverage advanced architectures for higher accuracy.  
- **Interactive Dashboards**: Build user-friendly visualization tools.  

---

**Made with ❤️ by Pratham Patel and Dev Vyas
