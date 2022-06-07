
import imp
from locale import atoi
from secrets import choice
from sqlite3 import Timestamp
from matplotlib import pyplot as plt
from nbformat import write
import streamlit as st
import pandas as pd
import seaborn as sb
import numpy as np
import json
import glob
import folium
from streamlit_folium import folium_static
from msilib.schema import Icon
import folium

def run_map():
    st.subheader('지역별 미세먼지 시간별 현황')

    df = pd.read_csv('data/fine_dust.csv',encoding ='cp949' )
    dust = pd.read_csv('data/dust1.csv' ,encoding='utf-8')
    
    df['위도'] = dust['위도']
    df['경도'] = dust['경도']

   
    asd = df['연월일'].unique()
    qaz = df['시간'].unique()
    choice = st.sidebar.selectbox('날짜 선택',asd)
    choice1 = st.sidebar.selectbox('시간 선택',qaz)
    
    user = df.loc[df['연월일'] == choice , ]
    user2 = df.loc[df['시간'] == choice1 ,]
    user3 = pd.merge(user, user2  , how='inner')

    
    
    loc = [37.558163, 126.930479] # 위도(N), 경도(E)
    qwer = len(user3)
    map = folium.Map(location= loc ,tiles = 'OpenStreetMap',zoom_start=11)


    for i in range(qwer):
        folium.Marker(list(user3.iloc[i][['위도', '경도']]),
        popup= user3.iloc[i][['미세먼지','초미세먼지']],
        icon=folium.Icon(color='green')).add_to(map)
    
    folium_static(map)


    st.dataframe(user3)
