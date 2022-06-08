import streamlit as st
from app_data import run_data

from app_home import run_home
from app_map import run_map
from app_ml import run_ml

from streamlit_option_menu import option_menu



def main():
    st.title('서대문구 미세먼지')

    menu = ['Home','Data','MAP','ML']

    with st.sidebar:
    
        choose = option_menu("Menu", menu,
                            icons=['house', 'layout-text-sidebar-reverse','graph-up','map'],
                            menu_icon="app-indicator", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#44475A5"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#BD93F9"},
            "nav-link-selected": {"background-color": "#02ab21"},
        })

    if choose == menu[0] :
        run_home()
    elif choose == menu[1] :
        run_data()
    elif choose == menu[2]:
        run_map()
    elif choose == menu[3]:
        run_ml()




if __name__ == '__main__':
    main()