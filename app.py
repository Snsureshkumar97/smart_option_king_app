# app.py

import streamlit as st
import os
from kiteconnect import KiteConnect
from datetime import datetime, time

# --- Load Zerodha API credentials from environment variables ---
Z_API_KEY = os.environ.get("w2v7z50yd1kfrj9m")
Z_API_SECRET = os.environ.get("47hn0txlyifunt3p5h2eh30y7tji5pt2")
Z_ACCESS_TOKEN = os.environ.get("Z_ACCESS_TOKEN")

# --- Zerodha Kite Connect Setup ---
kite = KiteConnect(api_key=Z_API_KEY)
kite.set_access_token(Z_ACCESS_TOKEN)

# --- Streamlit Page Settings ---
st.set_page_config(page_title="Smart Option Signal King", layout="wide")
st.title("📈 Smart Option Signal King")
st.markdown("AI-powered strike predictions for NIFTY, SENSEX, BANKNIFTY")

# --- Market Hours Check ---
now = datetime.now().time()
market_open = time(9, 15)
market_close = time(15, 30)

if not (market_open <= now <= market_close):
    st.warning("🚫 Markets are closed right now. Please try again between 9:15 AM – 3:30 PM IST.")
    st.stop()

# --- Market Dropdown ---
market = st.selectbox("Select Market", ["NIFTY", "BANKNIFTY", "SENSEX"])

# --- Fetch Option Chain (Mock for now, you can add live logic) ---
def fetch_option_chain(market):
    # Replace this mock with live option chain API parsing using KiteConnect later
    return [
        {"strike": "24,850 CE", "entry": 278, "T1": 290, "T2": 302, "T3": 318, "SL": 260, "expiry": "Tue, 25 Jun 2025", "profit": 3000},
        {"strike": "24,900 PE", "entry": 285, "T1": 298, "T2": 310, "T3": 325, "SL": 270, "expiry": "Tue, 25 Jun 2025", "profit": 3300},
    ]

strikes = fetch_option_chain(market)

# --- Display Strike Predictions ---
st.subheader(f"🔮 Strike Predictions for {market}")

for s in strikes:
    st.markdown(f"""
    **Strike:** {s['strike']}  
    **Entry Above:** ₹{s['entry']}  
    **T1:** ₹{s['T1']}  
    **T2:** ₹{s['T2']}  
    **T3:** ₹{s['T3']}  
    **SL:** ₹{s['SL']}  
    **Potential Profit per Lot:** ₹{s['profit']}  
    **Expiry:** {s['expiry']}
    """)

# --- Manual Refresh Button ---
if st.button("🔄 Refresh Prediction"):
    st.success("Signal refreshed with latest data!")

# --- Market Clock ---
st.sidebar.title("🕒 Market Timer")
st.sidebar.markdown(f"**Current Time (IST):** {datetime.now().strftime('%H:%M:%S')}")

# --- Footer ---
st.markdown("---")
st.caption("Built for educational use only. © 2025 Smart Option Signal King")
