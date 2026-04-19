# rerun_demo.py
'''
Example code from Chapter 10 of Coding Essentials for Astronomers.
Ting, Y.-S. (2025). Coding Essentials for Astronomers. The Ohio State University. 
DOI: 10.5281/zenodo.17850426
'''
import streamlit as st
import datetime

st.title("Understanding Reruns")
st.write(f"Script ran at: {datetime.datetime.now().strftime('%H:%M:%S.%f')}")

temperature = st.slider("Temperature (K):", 3000, 10000, 5778)
st.write(f"Selected: {temperature}K")