import streamlit as st
import pandas as pd
import numpy as np

st.title("🤖 AI Binary Trading Dashboard")
st.markdown("---")

st.sidebar.header("Settings")
run_bot = st.sidebar.checkbox("Run AI Analysis")
pair = st.sidebar.selectbox("Select Pair", ["EUR/USD", "GBP/USD", "BTC/USD"])

st.write(f"Currently Analyzing: **{pair}**")

if run_bot:
    st.success("AI Bot is running... Signal: CALL (UP) 🟢")
    chart_data = pd.DataFrame(np.random.randn(20, 2) * 5 + 100, columns=['Up', 'Down'])
    st.line_chart(chart_data)
else:
    st.warning("Bot is paused. Check the box on the sidebar to start.")