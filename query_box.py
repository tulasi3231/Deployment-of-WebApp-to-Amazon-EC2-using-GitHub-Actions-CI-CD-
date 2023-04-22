import pandas as pd
import streamlit as st
from database import execute_query,show_tables,view_table,get_attributes



def QueryBox():

   
    tables_list = show_tables()
    table = st.selectbox("Select table to view", tables_list)
    result = view_table(table)
    attributes = get_attributes(table)
    if st.button("view table"):
        df = pd.DataFrame(result, columns=attributes)
        st.dataframe(df)
    query = st.text_input("Query:")# if possible increase breadth 
    st.warning("Changes Made to DataBase via QueryBox will be commited")
    
    if st.button("Execute"):
        data = execute_query(query)
        # print(data)
        if data not in [0,1]:
            df = pd.DataFrame(data[0],columns=data[1])
            st.dataframe(df)
