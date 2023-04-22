import pandas as pd
import streamlit as st
import plotly.express as px
from database import *

def read_artist():
    result = view_all_artist_data()
   
    df = pd.DataFrame(result,
                      columns=['artist_id' , 'artist_name', 'PIN','city','street','DOB', 'gallery_id','Age'])
    with st.expander("View Artist"):
        st.dataframe(df)

