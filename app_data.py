
import streamlit as st
import pandas as pd

def run_data():
    st.subheader('데이터 확인')

    df = pd.read_csv('data/fine_dust.csv' ,encoding ='cp949' )


    radio_menu = ['데이터프레임','통계치']
    selected = st.radio('선택하세요',radio_menu)

    if selected == radio_menu[0] :
        st.dataframe(df)
    elif selected == radio_menu[1]:
        st.dataframe(df.describe())


    radio_menu1 = ['최대','최소']
    selected1 = st.radio('선택하세요',radio_menu1)

    if selected1 == radio_menu1[0] :
        st.dataframe(df[['미세먼지','초미세먼지']].max())
    elif selected1 == radio_menu1[1] :
        st.dataframe(df[['미세먼지','초미세먼지']].min())
        

