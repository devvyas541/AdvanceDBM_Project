import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
file_path = '/Users/devvyas16/Downloads/graph/modified_dataset.csv'  # Replace with your actual path
data = pd.read_csv(file_path)

# Ensure necessary columns are present
data['Age_Group'] = pd.cut(data['Age'], bins=[0, 18, 35, 60, 100], labels=["0-18", "19-35", "36-60", "60+"])

# Visualization 1: Heatmap - Disease Distribution by Age Group
plt.figure(figsize=(10, 8))
age_group_disease = data.groupby(["Disease", "Age_Group"]).size().reset_index(name="Count")
heatmap_data = age_group_disease.pivot_table(index="Disease", columns="Age_Group", values="Count", fill_value=0)
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="coolwarm")
plt.title("Disease Distribution by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Disease")
plt.show()

# Visualization 2: Pie Chart - Gender Distribution for Each Disease
gender_disease = data.groupby(["Disease", "Gender"]).size().reset_index(name="Count")
for disease in gender_disease['Disease'].unique():
    disease_data = gender_disease[gender_disease['Disease'] == disease]
    plt.figure(figsize=(6, 6))
    plt.pie(
        disease_data["Count"],
        labels=disease_data["Gender"],
        autopct="%1.1f%%",
        startangle=90,
        colors=sns.color_palette("pastel")[:len(disease_data["Gender"])]
    )
    plt.title(f"Gender Distribution for {disease}")
    plt.show()

# Visualization 3: Bar Chart - Most Common Diseases
disease_count = data["Disease"].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=disease_count.index, y=disease_count.values, palette="viridis")
plt.title("Most Common Diseases")
plt.xlabel("Disease")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Visualization 4: Line Plot - Age Distribution by Disease
age_distribution = data.groupby(["Disease", "Age"])["Age"].count().reset_index(name="Count")
plt.figure(figsize=(12, 6))
sns.lineplot(data=age_distribution, x="Age", y="Count", hue="Disease", marker="o")
plt.title("Age Distribution by Disease")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Visualization 5: Stacked Bar Chart - Disease Distribution by Gender
gender_disease = data.groupby(["Disease", "Gender"]).size().unstack(fill_value=0)
gender_disease.plot(kind="bar", stacked=True, figsize=(12, 6), colormap="coolwarm")
plt.title("Disease Distribution by Gender")
plt.xlabel("Disease")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Visualization 6: Histogram - Age Distribution Across Dataset
plt.figure(figsize=(10, 6))
sns.histplot(data["Age"], bins=20, kde=True, color="blue")
plt.title("Age Distribution Across Dataset")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Visualization 7: Scatter Plot - Age vs. Gender with Disease Color Coding
plt.figure(figsize=(12, 6))
sns.scatterplot(data=data, x="Age", y="Gender", hue="Disease", palette="Set1", s=100)
plt.title("Age vs. Gender with Disease Color Coding")
plt.xlabel("Age")
plt.ylabel("Gender")
plt.show()
