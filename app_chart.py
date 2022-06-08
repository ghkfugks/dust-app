import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import plotly.express as px

############### 그래프에서 한국어 인식 ###############
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Linux':
    rc('font', family='NanumGothic')    
else:
    print('Unknown system')


def run_chart():
    df = pd.read_csv('data/fine_dust.csv',encoding ='cp949' )

    
    sns.set_theme(style="whitegrid")

    fig = plotly.bar(df, x='풍속', y='연월일')
    st.plotly_chart(fig)

    fig4 = plt.figure()
    df['유동인구'].hist()
    st.pyplot(fig4)

    fig2 = plt.figure()
    df['미세먼지'].hist()
    st.pyplot(fig2)

    fig3 = plt.figure()
    df['초미세먼지'].hist()
    st.pyplot(fig3)



