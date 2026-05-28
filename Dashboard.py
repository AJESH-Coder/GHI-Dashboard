import streamlit as st

st.title("🌍 South Asia Hunger Index Dashboard")
st.divider()
st.write("This is a dashboard used to track Global Hunger Index of 6 South Asian countries from year 2000, 2008," \
" 2016, 2025")

col1, col2, col3 = st.columns(3)
col1.metric("Countries Tracked", "6")
col2.metric("Best in 2025", "Sri Lanka")
col3.metric("Worst in 2025", "Afghanistan")

st.info("Lower GHI score = Less hunger. Score below 10 is low, 10-19 moderate, 20-34 serious, 35+ alarming.")

st.subheader("Why This Matters?")
st.write("Over 1 in 4 people in South Asia face hunger. This dashboard tracks progress and highlights countries needing urgent attention.")

st.markdown("<h1 style='color: #FFFFFF; font-size: 25px;'>The information source for this dashboard came from official Global Hunger Index website.</h1>",
             unsafe_allow_html=True)
st.link_button(label= "Global Hunger Index Website",url="https://www.globalhungerindex.org/ranking.html")