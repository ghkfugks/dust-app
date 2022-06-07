import streamlit as st
from PIL import Image

def run_ml():
    st.subheader('미세먼지 예측 현황')

    dust = Image.open('data/dust.jpg')
    dust1 = Image.open('data/dust1.jpg') 


    
    st.image(dust, caption = '< 일간 미세먼지 예측>')

    
    st.image( dust1 , caption = '< 시간당 미세먼지 예측>')


