import streamlit as st

# App Title
st.set_page_config(page_title="Velor Risk Calculator", layout="centered")
st.title("💰 Velor Risk Calculator")

# Currency pairs
major_pairs = ["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "USDCAD", "NZDUSD"]
minor_pairs = ["EURGBP", "EURJPY", "GBPJPY", "CHFJPY", "AUDCAD", "NZDJPY"]
indices = ["XAUUSD", "US30", "NAS100", "SPX500"]

st.subheader("1️⃣ Select Pair Type")
pair_type = st.radio("Choose type:", ["Major", "Minor", "Other"])

# Conditional pair options
if pair_type == "Major":
    pair = st.selectbox("Select Major Pair", major_pairs)
elif pair_type == "Minor":
    pair = st.selectbox("Select Minor Pair", minor_pairs)
else:
    pair = st.selectbox("Select Other", indices)

# Inputs
st.subheader("2️⃣ Trade Settings")
balance = st.number_input("Account Balance ($)", min_value=0.0, step=100.0)
risk_percent = st.number_input("Risk per Trade (%)", min_value=0.0, step=0.1)
stop_loss = st.number_input("Stop Loss (pips)", min_value=0.1, step=0.1)
pip_value = st.number_input("Custom Pip Value ($)", min_value=0.01, value=10.0)

# Risk calculation
if balance > 0 and stop_loss > 0:
    risk_amount = (risk_percent / 100) * balance
    lot_size = risk_amount / (stop_loss * pip_value)
    potential_loss = lot_size * stop_loss * pip_value

    st.subheader("📊 Results")
    st.write(f"**Pair:** {pair}")
    st.write(f"Risk Amount: **${risk_amount:.2f}**")
    st.write(f"Lot Size: **{lot_size:.2f} lots**")
    st.write(f"Potential Loss: **${potential_loss:.2f}**")

    if risk_percent > 5:
        st.warning("⚠️ Risk exceeds 5% — Consider lowering it for better risk management.")