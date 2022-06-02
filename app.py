import streamlit as st
from app_chart import run_chart
from app_data import run_data

from app_home import run_home
from app_ml import run_ml

from streamlit_option_menu import option_menu
with st.sidebar:
    
        choose = option_menu("Menu", menu,
                            icons=['house', 'graph-up'],
                            menu_icon="app-indicator", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#44475A5"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#BD93F9"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }



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