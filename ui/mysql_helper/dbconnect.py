import mysql.connector

def estabilish_connection():
    con = mysql.connector.connect(host="localhost", user="root", passwd="{YOUR_PASSWORD}")
    cursor = con.cursor()
    cursor.execute("create database mailclient")
    con.commit()
