
import datetime
import pandas as pd
import streamlit as st
from database import *

def update_artist():
    result = view_all_artist_data()
   
    df = pd.DataFrame(result,
                      columns=['artist_id' , 'artist_name', 'PIN','city','street','DOB','Age','gallery_id'])
    with st.expander("Current Artist Details"):
        st.dataframe(df)
    list_of_artists = [i[0] for i in view_only_artist_names()]
    selected_artist = st.selectbox("Artist to Edit", list_of_artists)
    selected_result = get_artist(selected_artist)
   
    if selected_result:
        artist_id=selected_result[0][0]
        artist_name=selected_result[0][1]
        PIN=selected_result[0][2]
        city=selected_result[0][3]
        street=selected_result[0][4]
        DOB=selected_result[0][5]
        Age=selected_result[0][6]
        gallery_id=selected_result[0][7]
        col1, col2 = st.columns(2)
        with col1:
           
            new_artist_name = st.text_input("Artist Name:",artist_name)
            new_PIN = st.text_input("PIN:", PIN)
            new_city=st.text_input("city:", city)
        with col2:
            new_street = st.text_input("Street:", street)
            new_DOB = st.text_input("DOB:", DOB)
            new_Age=st.text_input("Age:",Age)
            new_gallery_id=st.text_input("gallery_id:",gallery_id)
        
        if st.button("Update Artist Details"):
                edit_artist_data(new_artist_name, new_PIN,new_city,new_street,new_DOB,new_Age,new_gallery_id,artist_id)
                st.success("Successfully updated")

    result2 = view_all_artist_data()
    df2 = pd.DataFrame(result2,
                       columns=['artist_id' , 'artist_name', 'PIN','city','street','DOB','Age','gallery_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)





