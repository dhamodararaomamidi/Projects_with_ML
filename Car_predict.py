import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

h1 {
    text-align:center;
    color:#1f77b4;
}

.stButton>button {
    width:100%;
    background-color:#1f77b4;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover {
    background-color:#0d5aa7;
}

.prediction-box{
    background-color:#d4edda;
    padding:20px;
    border-radius:10px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🚗 SAI's CAR PRICE PREDICTOR")
st.markdown(
    "<h4 style='text-align:center;'>Predict your car resale value instantly</h4>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- LOAD DATA ----------------
data = pd.read_csv("car_price_prediction.csv")
df = pd.DataFrame(data)

# ---------------- MODEL ----------------
x = df[["Year", "Engine Size", "Mileage"]]
y = df["Price"]

model = LinearRegression()
model.fit(x, y)

# ---------------- INPUTS ----------------
st.subheader("Enter Car Details")

col1, col2 = st.columns(2)

with col1:
    year = st.number_input(
        "📅 Manufacturing Year",
        min_value=1950,
        max_value=2026,
        value=2022
    )

with col2:
    engine = st.number_input(
        "⚙️ Engine Size (CC)",
        min_value=800,
        max_value=10000,
        value=2400
    )

mileage = st.number_input(
    "🛣️ Mileage (KM)",
    min_value=1000,
    max_value=300000,
    value=150000
)

st.divider()

# ---------------- PREDICTION ----------------
if st.button("🚀 Predict Price"):

    with st.spinner("Calculating car price..."):

        new_data = [[year, engine, mileage]]
        result = model.predict(new_data)

        price = int(result[0])

    st.success("Prediction Completed!")

    st.metric(
        label="💰 Estimated Car Price",
        value=f"₹ {price:,.0f}"
    )

    st.balloons()

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Made with ❤️ using Streamlit & Machine Learning")