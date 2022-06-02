
from matplotlib import pyplot as plt
from nbformat import write
import streamlit as st
import pandas as pd
import seaborn as sb
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
    
    

    st.dataframe(df)

   # folium_static(folium.Map(location=[fine['위도'][0],fine['경도'][0]]))

    

#     coffee_df = pd.concat([coffee_df1,coffee_df2,coffee_df3])


#     cafe = ['데이터프레임','인천시','경기도','서울시','브랜드별 수도권 위치','인접한 카페 위치']
#     selected = st.selectbox('선택하세요',cafe)

#     if selected == cafe[0] :
        
#         st.dataframe(coffee_df)
#     elif selected == cafe[1]:
#         cafeBrand1 = ['스타벅스','이디야','뺵다방']
#         select1 = st.selectbox('브랜드를 선택해주세요',cafeBrand1)
#         if select1 == cafeBrand1[0]:
#             df_starbucks1 = coffee_df1[coffee_df1['상호명'].str.contains('스타벅스')]
#             st.dataframe(df_starbucks1)
#             df_starbucks1.index = range(len(df_starbucks1))
#             st.write('인천시 내 스타벅스 점포 수 :', len(df_starbucks1))

#             starbucks_gu1 = df_starbucks1.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
#             starbucks_gu1 = starbucks_gu1.reset_index()
#             starbucks_gu1 = starbucks_gu1.set_index('시군구명')
#             st.dataframe(starbucks_gu1, 300, 350)
        

#             # 위치 파라미터 설정
#             loc = [37.517, 126.733] # 위도(N), 경도(E)
#             data1_size = len(df_starbucks1)

#             # 지도 정의
#             map_starbucks1 = folium.Map(location=loc, zoom_start=12)
    
#             # 포인트 마커 추가

#             for i in range(data1_size):

#                 folium.Marker(list(df_starbucks1.iloc[i][['위도', '경도']]),
#                 popup=df_starbucks1.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='green')).add_to(map_starbucks1)

#             folium_static(map_starbucks1)

#         elif select1 == cafeBrand1[1]:
#             df_ediya1 = coffee_df1[coffee_df1['상호명'].str.contains('이디야')]
#             st.dataframe(df_ediya1)
#             df_ediya1.index = range(len(df_ediya1))
#             st.write('인천시 내 이디야 점포 수 :', len(df_ediya1))

#             ediya_gu1 = df_ediya1.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
#             ediya_gu1 = ediya_gu1.reset_index()
#             ediya_gu1 = ediya_gu1.set_index('시군구명')
#             st.dataframe(ediya_gu1)

#             # 위치 파라미터 설정
#             loc = [37.517, 126.733] # 위도(N), 경도(E)
#             data2_size = len(df_ediya1)

#             # 지도 정의
#             map_ediya1 = folium.Map(location=loc, zoom_start=12)
    
#             # 포인트 마커 추가

#             for i in range(data2_size):

#                 folium.Marker(list(df_ediya1.iloc[i][['위도', '경도']]),
#                 popup=df_ediya1.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='blue')).add_to(map_ediya1)

#             folium_static(map_ediya1)

#         elif select1 == cafeBrand1[2]:    
#             df_paikdabang1 = coffee_df1[coffee_df1['상호명'].str.contains('빽다방')]
#             st.dataframe(df_paikdabang1)
#             df_paikdabang1.index = range(len(df_paikdabang1))
#             st.write('인천시 내 빽다방 점포 수 :', len(df_paikdabang1))

#             paikdabang_gu1 = df_paikdabang1.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
#             paikdabang_gu1 = paikdabang_gu1.reset_index()
#             paikdabang_gu1 = paikdabang_gu1.set_index('시군구명')
#             st.dataframe(paikdabang_gu1)

#             # 위치 파라미터 설정
#             loc = [37.517, 126.733] # 위도(N), 경도(E)
#             data3_size = len(df_paikdabang1)

#             # 지도 정의
#             map_paikdabang1 = folium.Map(location=loc, zoom_start=12)
    
#             # 포인트 마커 추가

#             for i in range(data3_size):

#                 folium.Marker(list(df_paikdabang1.iloc[i][['위도', '경도']]),
#                 popup=df_paikdabang1.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='orange')).add_to(map_paikdabang1)

#             folium_static(map_paikdabang1)   
        

#     elif selected == cafe[2]:
#         cafeBrand2 = ['스타벅스','이디야','뺵다방']
#         select2 = st.selectbox('브랜드를 선택해주세요',cafeBrand2)
#         if select2 == cafeBrand2[0]:
#             df_starbucks2 = coffee_df2[coffee_df2['상호명'].str.contains('스타벅스')]
#             st.dataframe(df_starbucks2)
#             df_starbucks2.index = range(len(df_starbucks2))
#             st.write('경기도 내 스타벅스 점포 수 :', len(df_starbucks2))

#             starbucks_gu2 = df_starbucks2.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
#             starbucks_gu2 = starbucks_gu2.reset_index()
#             starbucks_gu2 = starbucks_gu2.set_index('시군구명')
#             st.dataframe(starbucks_gu2, 300, 350)
        

#             # 위치 파라미터 설정
#             loc = [37.517, 126.733] # 위도(N), 경도(E)
#             data4_size = len(df_starbucks2)

#             # 지도 정의
#             map_starbucks2 = folium.Map(location=loc, zoom_start=12)
    
#             # 포인트 마커 추가

#             for i in range(data4_size):

#                 folium.Marker(list(df_starbucks2.iloc[i][['위도', '경도']]),
#                 popup=df_starbucks2.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='green')).add_to(map_starbucks2)

#             folium_static(map_starbucks2)

#         elif select2 == cafeBrand2[1]:
#             df_ediya2 = coffee_df2[coffee_df2['상호명'].str.contains('이디야')]
#             st.dataframe(df_ediya2)
#             df_ediya2.index = range(len(df_ediya2))
#             st.write('경기도 내 이디야 점포 수 :', len(df_ediya2))

#             ediya_gu2 = df_ediya2.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
#             ediya_gu2 = ediya_gu2.reset_index()
#             ediya_gu2 = ediya_gu2.set_index('시군구명')
#             st.dataframe(ediya_gu2)

#             # 위치 파라미터 설정
#             loc = [37.517, 126.733] # 위도(N), 경도(E)
#             data5_size = len(df_ediya2)

#             # 지도 정의
#             map_ediya2 = folium.Map(location=loc, zoom_start=12)
    
#             # 포인트 마커 추가

#             for i in range(data5_size):

#                 folium.Marker(list(df_ediya2.iloc[i][['위도', '경도']]),
#                 popup=df_ediya2.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='blue')).add_to(map_ediya2)

#             folium_static(map_ediya2)

#         elif select2 == cafeBrand2[2]:    
#             df_paikdabang2 = coffee_df2[coffee_df2['상호명'].str.contains('빽다방')]
#             st.dataframe(df_paikdabang2)
#             df_paikdabang2.index = range(len(df_paikdabang2))
#             st.write('경기도 내 빽다방 점포 수 :', len(df_paikdabang2))

#             paikdabang_gu2 = df_paikdabang2.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
#             paikdabang_gu2 = paikdabang_gu2.reset_index()
#             paikdabang_gu2 = paikdabang_gu2.set_index('시군구명')
#             st.dataframe(paikdabang_gu2)

#             # 위치 파라미터 설정
#             loc = [37.517, 126.733] # 위도(N), 경도(E)
#             data6_size = len(df_paikdabang2)

#             # 지도 정의
#             map_paikdabang2 = folium.Map(location=loc, zoom_start=12)
    
#             # 포인트 마커 추가

#             for i in range(data6_size):

#                 folium.Marker(list(df_paikdabang2.iloc[i][['위도', '경도']]),
#                 popup=df_paikdabang2.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='orange')).add_to(map_paikdabang2)

#             folium_static(map_paikdabang2)
        
#     elif selected == cafe[3]:
#         cafeBrand3 = ['스타벅스','이디야','뺵다방']
#         select3 = st.selectbox('브랜드를 선택해주세요',cafeBrand3)
#         if select3 == cafeBrand3[0]:
#             df_starbucks3 = coffee_df3[coffee_df3['상호명'].str.contains('스타벅스')]
#             st.dataframe(df_starbucks3)
#             df_starbucks3.index = range(len(df_starbucks3))
#             st.write('서울시 내 스타벅스 점포 수 :', len(df_starbucks3))

#             starbucks_gu3 = df_starbucks3.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
#             starbucks_gu3 = starbucks_gu3.reset_index()
#             starbucks_gu3 = starbucks_gu3.set_index('시군구명')
#             st.dataframe(starbucks_gu3, 300, 350)
        

#             # 위치 파라미터 설정
#             loc = [37.517, 126.733] # 위도(N), 경도(E)
#             data7_size = len(df_starbucks3)

#             # 지도 정의
#             map_starbucks3 = folium.Map(location=loc, zoom_start=12)
    
#             # 포인트 마커 추가

#             for i in range(data7_size):

#                 folium.Marker(list(df_starbucks3.iloc[i][['위도', '경도']]),
#                 popup=df_starbucks3.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='green')).add_to(map_starbucks3)

#             folium_static(map_starbucks3)

#         elif select3 == cafeBrand3[1]:
#             df_ediya3 = coffee_df3[coffee_df3['상호명'].str.contains('이디야')]
#             st.dataframe(df_ediya3)
#             df_ediya3.index = range(len(df_ediya3))
#             st.write('서울시 내 이디야 점포 수 :', len(df_ediya3))

#             ediya_gu3 = df_ediya3.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
#             ediya_gu3 = ediya_gu3.reset_index()
#             ediya_gu3 = ediya_gu3.set_index('시군구명')
#             st.dataframe(ediya_gu3)

#             # 위치 파라미터 설정
#             loc = [37.517, 126.733] # 위도(N), 경도(E)
#             data8_size = len(df_ediya3)

#             # 지도 정의
#             map_ediya3 = folium.Map(location=loc, zoom_start=12)
    
#             # 포인트 마커 추가

#             for i in range(data8_size):

#                 folium.Marker(list(df_ediya3.iloc[i][['위도', '경도']]),
#                 popup=df_ediya3.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='blue')).add_to(map_ediya3)

#             folium_static(map_ediya3)

#         elif select3 == cafeBrand3[2]:    
#             df_paikdabang3 = coffee_df3[coffee_df3['상호명'].str.contains('빽다방')]
#             st.dataframe(df_paikdabang3)
#             df_paikdabang3.index = range(len(df_paikdabang3))
#             st.write('서울시 내 빽다방 점포 수 :', len(df_paikdabang3))

#             paikdabang_gu3 = df_paikdabang3.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
#             paikdabang_gu3 = paikdabang_gu3.reset_index()
#             paikdabang_gu3 = paikdabang_gu3.set_index('시군구명')
#             st.dataframe(paikdabang_gu3)

#             # 위치 파라미터 설정
#             loc = [37.517, 126.733] # 위도(N), 경도(E)
#             data9_size = len(df_paikdabang3)

#             # 지도 정의
#             map_paikdabang3 = folium.Map(location=loc, zoom_start=12)
    
#             # 포인트 마커 추가

#             for i in range(data9_size):

#                 folium.Marker(list(df_paikdabang3.iloc[i][['위도', '경도']]),
#                 popup=df_paikdabang3.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='orange')).add_to(map_paikdabang3)

#             folium_static(map_paikdabang3)
        

#     elif selected == cafe[4]:
#         cafeBrand4 = ['인천시','경기도','서울시']
#         select4 = st.selectbox('브랜드를 선택해주세요',cafeBrand4)
#         if select4 == cafeBrand4[0]:
#             loc = [37.545, 126.671]

#             df_starbucks1 = coffee_df1[coffee_df1['상호명'].str.contains('스타벅스')]
#             df_ediya1 = coffee_df1[coffee_df1['상호명'].str.contains('이디야')]
#             df_paikdabang1 = coffee_df1[coffee_df1['상호명'].str.contains('빽다방')]

#             data1_size = len(df_starbucks1)
#             data2_size = len(df_ediya1)
#             data3_size = len(df_paikdabang1)

#             map = folium.Map(location=loc,tiles = 'OpenStreetMap',zoom_start=11)

#             for i in range(data1_size):
            
#                 folium.Marker(list(df_starbucks1.iloc[i][['위도', '경도']]),
#                 popup=df_starbucks1.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='green')).add_to(map)

#             for i in range(data2_size):

#                 folium.Marker(list(df_ediya1.iloc[i][['위도', '경도']]),
#                 popup=df_ediya1.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='blue')).add_to(map)

#             for i in range(data3_size):

#                 folium.Marker(list(df_paikdabang1.iloc[i][['위도', '경도']]),
#                 popup=df_paikdabang1.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='orange')).add_to(map)

#             folium_static(map)

#         elif select4 == cafeBrand4[1]:
#             loc = [37.545, 126.671]

#             df_starbucks2 = coffee_df2[coffee_df2['상호명'].str.contains('스타벅스')]
#             df_ediya2 = coffee_df2[coffee_df2['상호명'].str.contains('이디야')]
#             df_paikdabang2 = coffee_df2[coffee_df2['상호명'].str.contains('빽다방')]

#             data4_size = len(df_starbucks2)
#             data5_size = len(df_ediya2)
#             data6_size = len(df_paikdabang2)

#             map = folium.Map(location=loc,tiles = 'OpenStreetMap',zoom_start=11)

#             for i in range(data4_size):
            
#                 folium.Marker(list(df_starbucks2.iloc[i][['위도', '경도']]),
#                 popup=df_starbucks2.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='green')).add_to(map)

#             for i in range(data5_size):

#                 folium.Marker(list(df_ediya2.iloc[i][['위도', '경도']]),
#                 popup=df_ediya2.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='blue')).add_to(map)

#             for i in range(data6_size):

#                 folium.Marker(list(df_paikdabang2.iloc[i][['위도', '경도']]),
#                 popup=df_paikdabang2.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='orange')).add_to(map)

#             folium_static(map)
#         elif select4 == cafeBrand4[2]:
#             loc = [37.545, 126.671]

#             df_starbucks3 = coffee_df3[coffee_df3['상호명'].str.contains('스타벅스')]
#             df_ediya3 = coffee_df3[coffee_df3['상호명'].str.contains('이디야')]
#             df_paikdabang3 = coffee_df3[coffee_df3['상호명'].str.contains('빽다방')]

#             data7_size = len(df_starbucks3)
#             data8_size = len(df_ediya3)
#             data9_size = len(df_paikdabang3)

#             map = folium.Map(location=loc,tiles = 'OpenStreetMap',zoom_start=11)

#             for i in range(data7_size):
            
#                 folium.Marker(list(df_starbucks3.iloc[i][['위도', '경도']]),
#                 popup=df_starbucks3.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='green')).add_to(map)

#             for i in range(data8_size):

#                 folium.Marker(list(df_ediya3.iloc[i][['위도', '경도']]),
#                 popup=df_ediya3.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='blue')).add_to(map)

#             for i in range(data9_size):

#                 folium.Marker(list(df_paikdabang3.iloc[i][['위도', '경도']]),
#                 popup=df_paikdabang3.iloc[i][['상호명','지점명']],
#                 icon=folium.Icon(color='orange')).add_to(map)

#             folium_static(map)

#     elif selected == cafe[5]:
#         cafeBrand5 = ['인천시','경기도','서울시']
#         select5 = st.selectbox('브랜드를 선택해주세요',cafeBrand5)
#         if select5 == cafeBrand5[0]:
        
        
#             loc = [37.545, 126.671]

#             df_starbucks1 = coffee_df1[coffee_df1['상호명'].str.contains('스타벅스')]
#             df_ediya1 = coffee_df1[coffee_df1['상호명'].str.contains('이디야')]
#             df_paikdabang1 = coffee_df1[coffee_df1['상호명'].str.contains('빽다방')]

#             data1_size = len(df_starbucks1)
#             data2_size = len(df_ediya1)
#             data3_size = len(df_paikdabang1)

#             map = folium.Map(location=loc,
#                     tiles = 'OpenStreetMap', # 'OpenStreetMap', 'Stamen Toner'
#                     zoom_start=15, zoom_control=True,control_scale=True)


#             for i in range(data1_size):
            
#                 folium.Circle(list(df_starbucks1.iloc[i][['위도', '경도']]),
#                             radius = 50,
#                             popup=df_starbucks1. iloc[i][['상호명','지점명']],
#                             color = '#2c9147',fill_color = '#2c9147').add_to(map)

#             for i in range(data2_size):

#                 folium.Circle(list(df_ediya1.iloc[i][['위도', '경도']]),
#                             radius = 50,
#                             popup=df_ediya1.iloc[i][['상호명','지점명']],
#                             color = '#32408c',fill_color = '#32408c').add_to(map)

#             for i in range(data3_size):

#                 folium.Circle(list(df_paikdabang1.iloc[i][['위도', '경도']]),
#                             radius = 50,
#                             popup=df_paikdabang1.iloc[i][['상호명','지점명']],
#                             color = '#FF7F50',fill_color = '#FF7F50').add_to(map)
            
#             folium_static(map)
#         elif select5 == cafeBrand5[1]:
        
#             # 수원역 좌표
#             loc = [37.266, 126.995]

#             df_starbucks2 = coffee_df2[coffee_df2['상호명'].str.contains('스타벅스')]
#             df_ediya2 = coffee_df2[coffee_df2['상호명'].str.contains('이디야')]
#             df_paikdabang2 = coffee_df2[coffee_df2['상호명'].str.contains('빽다방')]

#             data4_size = len(df_starbucks2)
#             data5_size = len(df_ediya2)
#             data6_size = len(df_paikdabang2)

#             map = folium.Map(location=loc,
#                     tiles = 'OpenStreetMap', # 'OpenStreetMap', 'Stamen Toner'
#                     zoom_start=15, zoom_control=True,control_scale=True)


#             for i in range(data4_size):
            
#                 folium.Circle(list(df_starbucks2.iloc[i][['위도', '경도']]),
#                             radius = 50,
#                             popup=df_starbucks2. iloc[i][['상호명','지점명']],
#                             color = '#2c9147',fill_color = '#2c9147').add_to(map)

#             for i in range(data5_size):

#                 folium.Circle(list(df_ediya2.iloc[i][['위도', '경도']]),
#                             radius = 50,
#                             popup=df_ediya2.iloc[i][['상호명','지점명']],
#                             color = '#32408c',fill_color = '#32408c').add_to(map)

#             for i in range(data6_size):

#                 folium.Circle(list(df_paikdabang2.iloc[i][['위도', '경도']]),
#                             radius = 50,
#                             popup=df_paikdabang2.iloc[i][['상호명','지점명']],
#                             color = '#FF7F50',fill_color = '#FF7F50').add_to(map)
            
#             folium_static(map)
#         elif select5 == cafeBrand5[2]:
        
#             # 강남역 좌표
#             loc = [37.497, 127.023]


#             df_starbucks3 = coffee_df3[coffee_df3['상호명'].str.contains('스타벅스')]
#             df_ediya3 = coffee_df3[coffee_df3['상호명'].str.contains('이디야')]
#             df_paikdabang3 = coffee_df3[coffee_df3['상호명'].str.contains('빽다방')]

#             data7_size = len(df_starbucks3)
#             data8_size = len(df_ediya3)
#             data9_size = len(df_paikdabang3)

#             map = folium.Map(location=loc,
#                     tiles = 'OpenStreetMap', # 'OpenStreetMap', 'Stamen Toner'
#                     zoom_start=15, zoom_control=True,control_scale=True)


#             for i in range(data7_size):
            
#                 folium.Circle(list(df_starbucks3.iloc[i][['위도', '경도']]),
#                             radius = 50,
#                             popup=df_starbucks3. iloc[i][['상호명','지점명']],
#                             color = '#2c9147',fill_color = '#2c9147').add_to(map)

#             for i in range(data8_size):

#                 folium.Circle(list(df_ediya3.iloc[i][['위도', '경도']]),
#                             radius = 50,
#                             popup=df_ediya3.iloc[i][['상호명','지점명']],
#                             color = '#32408c',fill_color = '#32408c').add_to(map)

#             for i in range(data9_size):

#                 folium.Circle(list(df_paikdabang3.iloc[i][['위도', '경도']]),
#                             radius = 50,
#                             popup=df_paikdabang3.iloc[i][['상호명','지점명']],
#                             color = '#FF7F50',fill_color = '#FF7F50').add_to(map)
            
#             folium_static(map)
        
    
        

