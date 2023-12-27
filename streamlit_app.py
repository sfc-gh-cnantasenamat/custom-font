import streamlit as st

st.title('🎈 Custom font style')

st.header("Step 1 - Import font")
st.markdown("""
  <style>
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:400,700,400italic,700bold);
  </style>
  """, unsafe_allow_html=True)

st.code("""
st.markdown('''
  <style>
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:400,700,400italic,700bold);
  </style>
''', unsafe_allow_html=True)
""")

st.header("Step 2 - Use the font")
st.markdown("""
  The following is using
  <h1 style="font-family: 'Open Sans', sans-serif;">
    Open Sans
  </h1>
  font style from the Google API: https://fonts.googleapis.com/css?family=Open+Sans
""", unsafe_allow_html=True)

st.code("""
<h1 style="font-family: 'Open Sans', sans-serif;">
    Open Sans
</h1>
""")

st.markdown("""
  For comparison, the following is not using
  <h1>
    Open Sans
  </h1>
""", unsafe_allow_html=True)

st.code("""
<h1>
  Open Sans
</h1>
""")
