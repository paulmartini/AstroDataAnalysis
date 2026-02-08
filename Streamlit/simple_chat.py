# simple_chat.py
'''
Example code from Chapter 10 of Coding Essentials for Astronomers.
Ting, Y.-S. (2025). Coding Essentials for Astronomers. The Ohio State University. 
DOI: 10.5281/zenodo.17850426
'''
import streamlit as st

# Initialize
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Handle input
if prompt := st.chat_input("Type here"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Add response
    response = f"Echo: {prompt}"
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
