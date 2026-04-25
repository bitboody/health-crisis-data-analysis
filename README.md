# health-crisis-data-analysis


##  Overview

This project focuses on analyzing a Chronic Kidney Disease (CKD) dataset and preparing it for machine learning.
The main objective is to clean the data, handle missing values, and extract meaningful insights.

---

##  Project Goal
* Handle missing and inconsistent data
* Clean and preprocess the dataset
* Analyze relationships between medical features
* Prepare data for machine learning models

---

##  Data set

The dataset contains medical information about patients such as:

* Age
* Blood Pressure
* Hemoglobin
* Blood Glucose
* Sodium & Potassium
* And more clinical features

Target variable:

* `classification` → CKD (1) or Not CKD (0)

---

##  Data Cleaning

* Replaced `"?"` with `NaN`
* Removed extra spaces in text values
* Renamed columns for consistency
* Converted columns to correct data types

---

##  Handling Missing Values

* Numerical features → filled using **median**
* Categorical features → filled using **mode**

---

##  Data Preprocessing

* Converted categorical values to numeric using Label Encoding
* Standardized and cleaned feature values

---

##  Data Visualization

The following visualizations were created:

* CKD vs Non-CKD distribution
* Age distribution
* Age vs Blood Pressure scatter plot
* Correlation heatmap

---

##  Key Insights

* CKD patients tend to have **higher blood pressure**
* Lower hemoglobin levels are associated with CKD
* Several features required cleaning due to missing or inconsistent values
* Data preprocessing significantly improved dataset quality

##  How to Run

```bash
git clone <https://github.com/bitboody/health-crisis-data-analysis>
cd health-crisis-data-analysis
python --version  # Python 3.8+
python main.py
```

---

##   Output

<img width="1243" height="1068" alt="Screenshot 2026-04-25 173947" src="https://github.com/user-attachments/assets/fa78dbe7-a157-43d1-8b70-9f54b2ed9e12" />





_____
<img width="791" height="677" alt="Screenshot 2026-04-25 173934" src="https://github.com/user-attachments/assets/86fbd3d7-8c89-4f2a-98c1-3b840f53eb55" />



---

##  Future Improvements

* Apply advanced machine learning models
* Improve prediction accuracy
* Build a web dashboard for visualization

---

## Team 6 Members
* Ahmed Ezzat
* Abdelrahman Ahmed
* Dana Fattal
* Omer Ahmed
* Peter Gerges
  


