import streamlit as st
import pandas as pd
import joblib

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="Customer Purchase Prediction",
    page_icon="🛒",
    layout="wide"
)

# ----------------------------------------------------
# LOAD MODEL
# ----------------------------------------------------

MODEL_PATH = "customer_purchase_model.joblib"

model = joblib.load(MODEL_PATH)

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------

st.title("🛒 Customer Purchase Prediction System")

st.markdown("""
This Machine Learning application predicts whether a customer is likely to purchase a product based on demographic and customer information.

The prediction helps marketing teams target the right customers and improve campaign performance.
""")

st.divider()

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

st.sidebar.title("📌 Project Overview")

st.sidebar.markdown("""
### 🎯 Business Objective

Predict customers who are most likely to purchase.

Help businesses improve marketing ROI and increase sales.
""")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 💼 Business Benefits

- 🎯 Target high-potential customers
- 💵 Reduce marketing costs
- 📈 Increase campaign conversions
- ⚡ Improve marketing efficiency
- 📊 Support data-driven decisions
""")

# ----------------------------------------------------
# CUSTOMER INFORMATION
# ----------------------------------------------------

st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=80,
        value=30
    )

    income = st.number_input(
        "Annual Income",
        min_value=1000,
        value=50000
    )

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

with col2:

    spending = st.slider(
        "Spending Score",
        1,
        100,
        50
    )

    country = st.selectbox(
        "Country",
        ["USA","UK","Canada","India"]
    )

    membership = st.selectbox(
        "Membership",
        ["Bronze","Silver","Gold","Platinum"]
    )

st.divider()

# ----------------------------------------------------
# PREDICTION
# ----------------------------------------------------

if st.button("Predict Customer Purchase", use_container_width=True):

    input_df = pd.DataFrame({

        "Age":[age],
        "Income":[income],
        "SpendingScore":[spending],
        "Gender":[gender],
        "Country":[country],
        "Membership":[membership]

    })

    prediction = model.predict(input_df)[0]

    st.subheader("Prediction Result")

    if prediction == 1:

        st.success("✅ Customer is likely to PURCHASE the product.")

    else:

        st.error("❌ Customer is NOT likely to purchase the product.")

    st.divider()

    st.subheader("Customer Summary")

    summary = pd.DataFrame({

        "Feature":[
            "Age",
            "Income",
            "Spending Score",
            "Gender",
            "Country",
            "Membership"
        ],

        "Value":[
            age,
            income,
            spending,
            gender,
            country,
            membership
        ]

    })

    st.table(summary)

    st.divider()

    st.subheader("Business Insight")

    if prediction == 1:

        st.info("""

### Recommendation

This customer has a high purchase probability.

Suggested Actions

- Send promotional offers
- Recommend premium products
- Target through email campaigns
- Provide loyalty rewards

""")

    else:

        st.warning("""

### Recommendation

This customer currently has a low purchase probability.

Suggested Actions

- Offer discounts
- Send personalized campaigns
- Increase engagement before marketing expensive products

""")

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.divider()

st.caption("Built using Python • Scikit-Learn • Streamlit")