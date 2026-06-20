# 🚗 Car Price Prediction App

A Machine Learning web application built using **Python**, **Streamlit**, and **Scikit-Learn** that predicts the estimated price of a car based on its manufacturing year, engine size, and mileage.

## 📌 Features

* Predicts car prices instantly
* User-friendly Streamlit interface
* Machine Learning model using Linear Regression
* Responsive and clean design
* Displays estimated car value in Indian Rupees (₹)

## 🛠️ Technologies Used

* Python
* Pandas
* Streamlit
* Scikit-Learn
* NumPy

## 📂 Project Structure

```
Car-Price-Prediction/
│
├── app.py
├── car_price_prediction.csv
├── README.md
└── requirements.txt
```

## 📊 Dataset

The dataset contains the following features:

| Feature     | Description                        |
| ----------- | ---------------------------------- |
| Year        | Manufacturing year of the car      |
| Engine Size | Engine capacity in CC              |
| Mileage     | Total distance traveled by the car |
| Price       | Car price (Target Variable)        |

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/car-price-prediction.git
```

### 2. Navigate to Project Folder

```bash
cd car-price-prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

## 📋 Requirements

Create a `requirements.txt` file containing:

```text
streamlit
pandas
numpy
scikit-learn
```

## 🎯 How It Works

1. User enters:

   * Car Manufacturing Year
   * Engine Size (CC)
   * Mileage (KM)

2. The trained Linear Regression model processes the inputs.

3. The application predicts and displays the estimated car price.

## 📸 Application Preview

* Modern Streamlit UI
* Interactive input fields
* Instant prediction results
* Currency formatted output

## 🔮 Future Improvements

* Add Car Brand and Model selection
* Improve prediction accuracy using advanced algorithms
* Deploy on Streamlit Cloud
* Add data visualization dashboards
* Export prediction reports to PDF

## 👨‍💻 Author

**Sai Romeo**

Built with Python, Machine Learning, and Streamlit.

## 📄 License

This project is open source and available under the MIT License.
