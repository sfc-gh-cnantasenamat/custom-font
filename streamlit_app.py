import streamlit as st

st.title('🎈 Custom font style')

st.markdown("""
  <style>
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:400,700,400italic,700bold);
  </style>
  """, unsafe_allow_html=True)

st.markdown("""
  This app is using
  <h1 style="text-align: center; font-size:110px; font-family: 'Open Sans', sans-serif; letter-spacing: -0.02em"; font-weight: 700;>
    Open Sans
  </h1>
  font style from the Google API: https://fonts.googleapis.com/css?family=Open+Sans

  For comparison, the following is not using
  <h1>
    Open Sans
  </h1>
""", unsafe_allow_html=True)
