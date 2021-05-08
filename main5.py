import streamlit as st

st.title('Streamlit超入門')

st.write('Interactive Widgets')

text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味:',text

condition = st.slider('あなたの調子は？',0,100,50)
'あなたのコンディション：',condition