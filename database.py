# pip install mysql-connector-python
import mysql.connector
import pandas as pd
import streamlit as st
mydb = mysql.connector.connect(
    host="database-2.ckqwsilv80o5.us-east-2.rds.amazonaws.com",
    user="admin",
    database="pes1ug20cs583_artgallery",
    password="niharika123",
    port=3306
)
c = mydb.cursor()
def add_artist_data(artist_id , artist_name, PIN,city,street,DOB,age,gallery_id):
    c.execute('INSERT INTO artist_583(artist_id , artist_name, PIN,city,street,DOB,age,gallery_id) VALUES (%s,'
              '%s,%s,%s,%s,%s,%s,%s)',
              (artist_id , artist_name, PIN,city,street,DOB, gallery_id,age))
    mydb.commit()




def view_all_artist_data():
    c.execute('SELECT * FROM artist_583')
    data = c.fetchall()
    return data

def view_only_artist_names():
    c.execute('SELECT artist_id FROM artist_583 order by artist_id ASC')
    data = c.fetchall()
    return data



def get_artist(artist_id):
    c.execute('SELECT * FROM artist_583 WHERE artist_id="{}"'.format(artist_id))
    data = c.fetchall()
    return data


def edit_artist_data(new_artist_name, new_PIN,new_city,new_street,new_DOB,new_Age,new_gallery_id,artist_id):
    c.execute("UPDATE artist_583 SET artist_name=%s, PIN=%s,city=%s,street=%s,DOB=%s,Age=%s,gallery_id=%s where artist_id=%s",
              (new_artist_name, new_PIN,new_city,new_street,new_DOB,new_Age,new_gallery_id,artist_id))
    mydb.commit()


def delete_artist_data(artist_id):
    c.execute('DELETE FROM artist_583 WHERE artist_id="{}"'.format(artist_id))
    mydb.commit()




def show_tables():
    c.execute('show tables')
    res = c.fetchall()
    tables = [i[0]  for i in res ]
    return tables

def view_table(table):
    c.execute(f'select * from {table}')
    res = c.fetchall()
    return res

def get_attributes(table):
    c.execute(f'select * from {table}')
    res = c.fetchall()
    attributes = c.column_names
    return attributes


def execute_query(query):
    try:
        c.execute(query)
        if query.split()[0].lower() not in ['select','show']:
            mydb.commit()
        data = c.fetchall()
        return [data,c.column_names]
    except BaseException as e:
        if str(e)=='No result set to fetch from.':
            st.success('querry successful')
            return 1
        st.error(e)
        return 0



