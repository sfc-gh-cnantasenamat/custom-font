import streamlit as st

st.title('🎈 Custom font style')

st.markdown("""
  <style>
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:400,700,400italic,700bold);
  </style>
  """, unsafe_allow_html=True)

st.markdown("""
  This app is using the Open Sans font style from the Google API: https://fonts.googleapis.com/css?family=Open+Sans
""")
