import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import folium
from PIL import Image

def run_map():
    st.subheader('지역별 미세먼지 시간별 현황')

    df = pd.read_csv('data/fine_dust.csv',encoding ='cp949' )
    dust = pd.read_csv('data/dust1.csv' ,encoding='utf-8')
    data = Image.open('data/데이터.jpg')
    
    df['위도'] = dust['위도']
    df['경도'] = dust['경도']

   
    asd = df['연월일'].unique()
    qaz = df['시간'].unique()
    choice = st.sidebar.selectbox('날짜 선택',asd)
    choice1 = st.sidebar.selectbox('시간 선택',qaz)
    
    st.sidebar.image(data)
    
    user = df.loc[df['연월일'] == choice , ]
    user2 = df.loc[df['시간'] == choice1 ,]
    user3 = pd.merge(user, user2  , how='inner')

    
    
    loc = [37.558163, 126.930479] # 위도(N), 경도(E)
    qwer = len(user3)
    map = folium.Map(location= loc ,tiles = 'OpenStreetMap',zoom_start=11)
    popup= folium.Popup()

    for i in range(qwer):
        # folium.Vega(scatter_chert, height=250,width=350.add_to(popup))
        folium.Marker(list(user3.iloc[i][['위도', '경도']]),
        popup= user3.iloc[i][['미세먼지','초미세먼지']],
        icon=folium.Icon(color='green')).add_to(map)
    
    folium_static(map)


    st.dataframe(user3)
