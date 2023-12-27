import streamlit as st

st.title('🎈 Custom font style')

st.header("Step 1 - Importing the font")
st.markdown("We're going to use fonts from the Google API: https://fonts.googleapis.com/css?family=Open+Sans")

st.markdown("""
  <style>
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:400,700,400italic,700bold);
  </style>
  """, unsafe_allow_html=True)

with st.expander("See code"):
  st.code("""
    st.markdown('''
      <style>
        @import url(https://fonts.googleapis.com/css?family=Open+Sans:400,700,400italic,700bold);
      </style>
    ''', unsafe_allow_html=True)
  """)

st.header("Step 2 - Using the font")

st.subheader("Displaying new font in H1 heading")

st.markdown("""
  <h1 style="font-family: 'Open Sans', sans-serif;">
    Open Sans
  </h1>
""", unsafe_allow_html=True)

with st.expander("See code"):
  st.code("""
    st.markdown('''
      <h1 style="font-family: 'Open Sans', sans-serif;">
        Open Sans
      </h1>
    ''', unsafe_allow_html=True)
  """)

st.markdown("""
  For comparison, the following is Streamlit's default font style:
  <h1>
    Open Sans
  </h1>
""", unsafe_allow_html=True)

with st.expander("See code"):
  st.code("""
    st.markdown('''
      <h1>
        Open Sans
      </h1>
    ''')
""")

st.subheader("Displaying new font in normal text")

st.markdown("""
  <div style="font-family: 'Open Sans', sans-serif;">
    The quick brown fox jumped over the lazy cat.
  </div>
""", unsafe_allow_html=True)

with st.expander("See code"):
  st.code("""
    st.markdown'''
      <div style="font-family: 'Open Sans', sans-serif;">
        The quick brown fox jumped over the lazy cat.
      </div>
    ''' unsafe_allow_html=True)
  """)

st.markdown("The quick brown fox jumped over the lazy cat.")

with st.expander("See code"):
  st.code("""
    st.markdown('The quick brown fox jumped over the lazy cat.')
  """)
