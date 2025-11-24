import streamlit as st
import requests

st.title("Chain AI Supply Recommendation")

uploaded_file = st.file_uploader("Upload your sales CSV", type="csv")

if uploaded_file:
    st.success("File uploaded successfully!")
    if st.button("Get Recommendation"):
        files = {'file': uploaded_file}
        response = requests.post("http://127.0.0.1:8000/recommend", files=files)
        if response.ok:
            data = response.json()
            st.write(f"Forecast for next period: **{data['forecast']} units**")
            st.write(f"Recommended order: **{data['recommended_order']} units**")
        else:
            st.error("Error from backend: " + response.text)
