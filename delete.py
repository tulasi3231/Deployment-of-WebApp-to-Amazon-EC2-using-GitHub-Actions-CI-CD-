import pandas as pd
import streamlit as st
from database import *


def delete_artist():
    result = view_all_artist_data()
    df = pd.DataFrame(result,
                      columns=['artist_id' , 'artist_name', 'PIN','city','street','DOB','Age','gallery_id'])
    with st.expander("Current artist details"):
        st.dataframe(df)

    list_of_artists = [i[0] for i in view_only_artist_names()]
    selected_artist = st.selectbox("Artist to Delete", list_of_artists)
    st.warning("Do you want to delete ::{}".format(selected_artist))
    if st.button("Delete ARTIST"):
        delete_artist_data(selected_artist)
        st.success("Artist has been deleted successfully")
    new_result = view_all_artist_data()
    df2 = pd.DataFrame(new_result,
                       columns=['artist_id' , 'artist_name', 'PIN','city','street','DOB','Age','gallery_id'])
    with st.expander("Updated details"):
        st.dataframe(df2)