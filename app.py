import streamlit as st
import pandas as pd

st.header("Coro Invoice Processor")
st.subheader("Upload the files to get started with processing")

uploaded_file = st.file_uploader("Upload an Invoice File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

