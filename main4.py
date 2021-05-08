import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit超入門')

st.write('Display Image')

img = Image.open('sample.jpeg')
img = img.rotate(270)
st.image(img, caption='Hiroshi Ohta in PILATUS',use_column_width =True)




