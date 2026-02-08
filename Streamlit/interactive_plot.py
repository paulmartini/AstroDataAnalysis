# interactive_plot.py
'''
Example code from Chapter 10 of Coding Essentials for Astronomers.
Ting, Y.-S. (2025). Coding Essentials for Astronomers. The Ohio State University. 
DOI: 10.5281/zenodo.17850426
'''
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

freq = st.slider("Frequency:", 1, 10, 3)

fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
ax.plot(x, np.sin(freq * x))
st.pyplot(fig)
