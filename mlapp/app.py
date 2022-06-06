import streamlit as st
from predict_page import show_predict_page
from explore_page import show_timer_page
from about import show_about_page
page = st.sidebar.selectbox("Tab",('About','Timer','Which topic should I study?',))
if page=='Timer':
    show_timer_page()
elif page=='which topic should I study?':
    show_predict_page()
else:
    show_about_page()