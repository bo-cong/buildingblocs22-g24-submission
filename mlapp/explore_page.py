import streamlit as st
import time
def show_timer_page():
    def cd(ts):
        with st.empty():
            while ts:
                mins, secs = divmod(ts,60)
                timern='{:02d}:{:02d}'.format(mins,secs)
                st.header(timern)
                time.sleep(1)
                ts-=1
    st.write('Timer')
    time_in_minutes= st.number_input("enter time in minutes")
    time_in_secs=int(time_in_minutes*60)
    if st.button('Start'):
        cd(time_in_secs)