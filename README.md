# E-Commerce Profit Prediction App

## Project Overview

This project builds a machine learning model to predict **order profit in an e-commerce business** based on key transaction features such as sales, quantity, discount, shipping cost, and order aging.

A **Random Forest regression model** is trained using historical e-commerce order data. The trained model is then deployed using a **Streamlit web application**, allowing users to input order details and instantly predict expected profit.

This project demonstrates the end-to-end workflow of a **data science project**, including data analysis, model training, and deployment through an interactive web interface.

---

## Project Objectives

- Analyze e-commerce order data
- Train a machine learning model to predict profit
- Save the trained model for reuse
- Build an interactive web application for predictions
- Allow users to input order parameters and receive profit predictions

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

---

## Project Structure

```
.
├── E_Commerce_Analysis.ipynb      # Data analysis and model training notebook
├── E-commerce Dataset.csv         # Dataset used for training the model
├── profit_prediction_model.pkl    # Saved trained machine learning model
├── app.py                         # Streamlit web application
└── README.md                      # Project documentation
```

---

## Dataset Features

The model predicts profit using the following input features:

| Feature | Description |
|------|-------------|
| Sales | Total order sales value |
| Quantity | Number of items purchased |
| Discount | Discount applied to the order |
| Shipping Cost | Cost of shipping the order |
| Aging | Number of days the order remained pending |

Target variable:

- **Profit**

---

## Machine Learning Model

The project uses a **Random Forest Regressor** to predict order profit.

Reasons for choosing Random Forest:

- Handles non-linear relationships
- Works well with tabular datasets
- Reduces overfitting compared to single decision trees
- Provides strong predictive performance

The trained model is saved using **Joblib** for later deployment.

---

## Web Application

The project includes a **Streamlit web application** that allows users to interact with the trained model.

Users can:

- Enter order parameters
- Click a prediction button
- View the predicted profit instantly

The application loads the saved model and performs predictions based on user input. :contentReference[oaicite:0]{index=0}

---

## Application Interface

Inputs available in the web app:

- Sales
- Quantity
- Discount
- Shipping Cost
- Aging (days)

After entering the values, clicking **Predict Profit** returns the predicted profit value.

---

## How to Run the Project

### 1. Install Dependencies

```
pip install pandas numpy scikit-learn streamlit joblib
```

---

### 2. Run the Streamlit App

```
streamlit run app.py
```

---

### 3. Open the Application

After running the command, open the provided local URL in your browser (usually):

```
http://localhost:8501
```

---

## Workflow of the Project

1. Load and explore the e-commerce dataset
2. Clean and preprocess the data
3. Train a machine learning regression model
4. Save the trained model using Joblib
5. Build a Streamlit interface for predictions
6. Deploy the model through a web application

---

## Example Use Case

An e-commerce manager can estimate expected profit before processing an order by entering:

- Sales value
- Quantity
- Discount
- Shipping cost
- Order aging

The model predicts the likely profit outcome, helping support **better pricing and discount decisions**.

---

## Possible Improvements

- Add more features such as customer segment or product category
- Improve model performance using hyperparameter tuning
- Deploy the app online using Streamlit Cloud
- Add visual analytics dashboard
- Track prediction history

---

## Conclusion

This project demonstrates a complete **machine learning workflow**, from exploratory data analysis and model training to deployment using an interactive Streamlit application. It highlights how predictive models can support decision-making in e-commerce operations.

