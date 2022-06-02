import streamlit as st
from app_chart import run_chart
from app_data import run_data

from app_home import run_home
from app_ml import run_ml



def main():
    st.title('서대문구 미세먼지')

    menu = ['Home','Data','Chart','ML']

    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_data()
    elif choice == menu[2]:
        run_chart()
    elif choice == menu[3]:
        run_ml()




if __name__ == '__main__':
    main()