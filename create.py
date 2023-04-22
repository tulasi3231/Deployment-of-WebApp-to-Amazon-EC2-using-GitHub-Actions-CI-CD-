import streamlit as st
from database import *





def create_artist():
    col1, col2 = st.columns(2)
    with col1:
        artist_id = st.text_input(" Artist Id :")
        artist_name = st.text_input("Artist Name:")
        PIN=st.text_input("PIN:")
        
        
    with col2:
        city = st.text_input("City:")
        street = st.text_input("Street:")
        DOB = st.text_input("DOB:")
        age = st.text_input("Age:")
        gallery_id = st.text_input("Gallery ID:")

    if st.button("Add Artist "):
        add_artist_data( artist_id , artist_name, PIN,city,street,DOB, gallery_id,age)
        st.success("Successfully added Artist: {}".format(artist_id))


