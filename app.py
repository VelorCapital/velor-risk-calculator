import streamlit as st

# Title
st.title("Velor Risk Calculator")

# Inputs
balance = st.number_input("Account Balance ($)", min_value=0.0, step=100.0)
risk_percent = st.number_input("Risk per Trade (%)", min_value=0.0, step=0.1)
stop_loss_pips = st.number_input("Stop Loss (Pips)", min_value=0.1, step=0.1)
pip_value = st.number_input("Custom Pip Value ($)", min_value=0.01, value=10.0)

# Calculate risk
if balance > 0 and stop_loss_pips > 0:
    risk_amount = (risk_percent / 100) * balance
    lot_size = risk_amount / (stop_loss_pips * pip_value)
    potential_loss = lot_size * stop_loss_pips * pip_value

    st.markdown("### Results")
    st.write(f"Risk Amount: ${risk_amount:.2f}")
    st.write(f"Lot Size: {lot_size:.2f}")
    st.write(f"Potential Loss: ${potential_loss:.2f}")

    if risk_percent > 5:
        st.error("⚠️ Warning: Risking more than 5% of your account is very risky!")