import streamlit as st
import mysql.connector

from create import *
from database import *
from delete import *
from read import *
from update import *
from query_box import *



def main():

    st.title("CC")
    st.title("ART GALLERY MANAGEMENT SYSTEM")
    menu = ["Artist"]
    options = ["Insert", "View", "Update", "Delete"]
    options_1=["View"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Artist":
        choice1 = st.sidebar.selectbox("Options", options)
        if choice1 == "Insert":
            st.subheader("Enter Artist Details:")
            create_artist()
        elif choice1 == "View":
            st.subheader("View Artist")
            read_artist()

        elif choice1 == "Update":
            st.subheader("Update Artist")
            update_artist()

        elif choice1 == "Delete":
            st.subheader("Delete Artist")
            delete_artist()

        else:
            st.subheader("About Artist")    




if __name__ == '__main__':
    main()
