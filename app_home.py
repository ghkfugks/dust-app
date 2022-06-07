import streamlit as st
from PIL import Image
import pandas as pd

def run_home():
    st.subheader('서대문구의 미세먼지가 위치 시간 유동인구에 따라 변화가 얼마나 있는지 확인.')
    dust = Image.open('data/먼지.jpg')  
    suda = Image.open('data/서대문구.jpg')

    st.image(dust,width=800)
    st.sidebar.image(suda,width=310)
    
    