# Currently in Progress
> A machine learning project for predicting economic recessions using macroeconomic indicators: **GS10**, **DGS2**, and **DGS3MO**.

Recession Predictor is a machine learning project built for a Machine Learning course. The primary objective is to compare the performance of different machine learning models in forecasting economic recessions based on key yield curve indicators.

---

## 📌 Project Summary

Economic recessions have a wide-ranging impact on markets, businesses, and individuals. Anticipating a recession early can inform better policy and investment decisions. This project explores how yield curve-based macroeconomic indicators can be used to train machine learning models for binary classification — determining whether the economy is in a recession or not.

---

## 📉 Economic Indicators Used

- **GS10** – 10-Year Treasury Constant Maturity Rate  
- **DGS2** – 2-Year Treasury Constant Maturity Rate  
- **DGS3MO** – 3-Month Treasury Bill Rate  

These indicators are known for their role in predicting yield curve inversions, which often precede recessions.

---

## 🔧 Problem Type

- **Task:** Binary Classification  
- **Target Variable:** Recession (1 = Recession, 0 = No Recession)  
- **Source:** NBER-labeled recession periods & FRED economic data  

---

## 🧪 Algorithms Compared
### Classical ML
- Logistic Regression  
- Balanced Random Forest  
- XGBoost  
- Easy Ensemble Classifier 
### Deep ML 
- Multiple LSTM configurations (deep learning)

---
## 📊 Evaluation Metrics
 ### Metrics for Classical ML
- **AUC-PR (Area Under Precision-Recall Curve)** – Measures performance on imbalanced datasets by focusing on positive class precision and recall  
- **ROC-AUC (Area Under ROC Curve)** – Measures the model's ability to discriminate between classes across all thresholds


 ### Metrics for Deep ML


- **Accuracy** – Proportion of total correct predictions  
- **Balanced Accuracy** – Average recall per class, useful for imbalanced datasets  
- **Precision** – Proportion of positive identifications that were actually correct  
- **Recall** – Proportion of actual positives that were correctly identified  
- **F1 Score** – Harmonic mean of precision and recall, balancing both metrics  
- **Weighted Average** – Weighted average of precision, recall, and F1 score to account for class imbalance  
- **AUC-PR (Area Under Precision-Recall Curve)** – Measures performance on imbalanced datasets by focusing on positive class precision and recall  
- **ROC-AUC (Area Under ROC Curve)** – Measures the model's ability to discriminate between classes across all thresholds



---


