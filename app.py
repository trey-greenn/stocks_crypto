import streamlit as st
from multiapp import MultiApp
from apps import crypto, stocks

app = MultiApp()

st.markdown("""
# Multi-Page App 

Dashboard to check your favorite stocks and cryptocurrency

""")

#Add all your application here
app.add_app("Crypto", crypto.app)
app.add_app("Stocks", stocks.app)

app.run()