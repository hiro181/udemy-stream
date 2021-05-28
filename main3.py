import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit超入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.546,139.507],
    columns=['lat','lon']
    )

st.map(df)
st.table(df.style.highlight_max(axis=0))


