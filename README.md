# Hydraulic Accumulator Condition Prediction

A machine learning project that analyses hydraulic system sensor data to predict the condition of a hydraulic accumulator.

## Project Overview

This project uses the Condition Monitoring of Hydraulic Systems dataset to study sensor measurements and predict accumulator conditions using machine learning.

It focuses on analysing pressure, temperature, flow and vibration measurements and presenting the findings through an interactive Streamlit dashboard.

## Project Objectives

- Analyse hydraulic system sensor measurements.
- Perform data cleaning and preprocessing.
- Extract statistical features from sensor readings.
- Compare different machine learning classification models.
- Predict hydraulic accumulator conditions.
- Develop an interactive dashboard to explore the results.

## Sensors Analysed

| Sensor Category | Sensors |
|---|---|
| Pressure | PS1–PS6 |
| Temperature | TS1–TS4 |
| Flow | FS1–FS2 |
| Vibration | VS1 |
| Motor Power | EPS1 |

## Dataset Information

- Total operating cycles: 2,205
- Initial sensor features: 84
- Final selected features: 80
- Target classes: 90, 100, 115 and 130

Dataset source: [UCI Machine Learning Repository – Condition Monitoring of Hydraulic Systems](https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems)

## Machine Learning Models

The following models were compared:

1. Dummy Classifier
2. Logistic Regression
3. Decision Tree
4. Random Forest

The Decision Tree achieved the best validation Macro F1 score and was selected for hyperparameter tuning.

## Final Model Performance

The selected Decision Tree was evaluated on the final chronological test set.

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 28.84% |
| Macro Precision | 20.95% |
| Macro Recall | 28.13% |
| Macro F1 Score | 22.34% |

The final test results indicate limited generalisation to unseen cycles. This highlights the challenges of predicting accumulator conditions from sensor data and the need for further model improvement.

## Streamlit Dashboard

The project includes an interactive dashboard with four sections:

- **Dataset Overview:** Explore dataset information and condition distribution.
- **Sensor Analysis:** Examine sensor behaviour across selected conditions and cycles.
- **Model Performance:** Compare models and review final predictions.
- **About the Project:** View the project methodology and findings.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Plotly
- Streamlit
- Jupyter Notebook

## Project Limitations

- The final model has limited predictive performance.
- Evaluation uses a chronological holdout from the available dataset.
- The dashboard analyses existing data and is not connected to live industrial sensors.
- Further testing and improvement are needed before practical deployment.

## Acknowledgement

Dataset provided by the UCI Machine Learning Repository.

This project was developed for academic and learning purposes.