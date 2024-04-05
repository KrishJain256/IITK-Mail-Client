import mysql.connector

def estabilish_connection():
    con = mysql.connector.connect(host="localhost", user="root", passwd="krish")
    cursor = con.cursor()
    cursor.execute("create database mailclient")
    con.commit()