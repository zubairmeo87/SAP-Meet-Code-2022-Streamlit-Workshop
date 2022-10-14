import streamlit as st
import os
import numpy as np
import pandas as pd
import urllib.request
from PIL import Image
import glob

def update_params():
    st.experimental_set_query_params(challenge=st.session_state.day)

md_files = sorted([int(x.strip('Slide').strip('.py')) for x in glob.glob1('content',"*.py") ])

# Logo and Navigation
col1, col2, col3 = st.columns((1,4,1))
with col2:
    st.image(Image.open('Logo_Tunup.PNG'))
st.markdown('# Introduction to the Streamlit framework')

days_list = [f'Slide {x}' for x in md_files]

query_params = st.experimental_get_query_params()

if query_params and query_params["challenge"][0] in days_list:
    st.session_state.day = query_params["challenge"][0]

selected_day = st.selectbox('Select the Slide 👇', days_list, key="day", on_change=update_params)




# Display content
for i in days_list:
    if selected_day == i:
        j = i.replace(' ', '')
        exec(open("content/"+str(j)+".py").read())

