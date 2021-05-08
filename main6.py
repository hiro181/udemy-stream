import streamlit as st

st.title('Streamlit超入門')

st.sidebar.write('Interactive Widgets')

text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味:',text

condition = st.sidebar.slider('あなたの調子は？',0,100,50)
'あなたのコンディション：',condition