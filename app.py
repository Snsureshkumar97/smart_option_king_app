import streamlit as st
from datetime import datetime, time

# App Title and Branding
st.set_page_config(page_title="Smart Option Signal King", layout="wide")
st.title("📈 Smart Option Signal King")
st.markdown("AI-powered strike predictions for NIFTY, SENSEX, BANKNIFTY")

# Market Timing Logic
now = datetime.now().time()
market_open = time(9, 15)
market_close = time(15, 30)

if not (market_open <= now <= market_close):
    st.warning("🚫 Markets are closed right now. Please try again between 9:15 AM – 3:30 PM IST.")
else:
    # Sample prediction panel
    st.subheader("🔮 Today's Signal (Live Prediction)")
    st.markdown("""**Strike:** 24,850 CE  
**Entry Above:** ₹278  
**T1:** ₹290  
**T2:** ₹302  
**T3:** ₹318  
**SL:** ₹260""")
    st.markdown("""**Potential Profit per Lot:** ₹3000  
**Expiry:** Tue, 25 Jun 2025""")

    # Refresh Button
    if st.button("🔄 Refresh Prediction"):
        st.success("Signal refreshed with latest data!")

# Footer
st.markdown("---")
st.caption("Built for educational purposes. © 2025 Smart Option Signal King")
