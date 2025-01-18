# Regression Salary Estimation with ANN

This project is hosted on: https://ann-regression-salary-estimation-a8zvzen5pmq3rqnxtckdja.streamlit.app/



## Project Overview

This project aims to estimate salaries based on various input features using an Artificial Neural Network (ANN).

## Steps

1. **Data Preprocessing**: Encode categorical features and scale numerical features.
2. **Model Training**: Train an ANN model on the preprocessed data.
3. **Prediction**: Use the trained model to predict salaries for new input data.

## Tools and Libraries

- Python
- TensorFlow/Keras
- Pandas
- Scikit-learn
- Streamlit (for web app)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/adityagadekar7/ANN-Regression-Salary-Estimation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ANN-Regression-Salary-Estimation
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Data Preprocessing and Model Training**:
   ```bash
   model_training.ipynb
   ```
2. **Run the Streamlit App**:
   ```bash
   streamlit run app_streamlit_regression.py
   ```

## Conclusion

This project demonstrates the use of an Artificial Neural Network to estimate salaries based on input features. The Streamlit app provides an interactive way to use the regression model for salary estimation.
