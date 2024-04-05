import mysql.connector

def create_new_user(username,password,firstname,lastname,email,rollno):
    con = mysql.connector.connect(host="localhost", user="root", passwd="krish", database="mailclient")
    cursor = con.cursor()
    query = f"Insert into ui_user (username,password,firstname,lastname,email,rollno) values ('{username}','{password}','{firstname}','{lastname}','{email}',{rollno})"
    cursor.execute(query)
    con.commit()

def verify_user(username,password):
    con = mysql.connector.connect(host="localhost", user="root", passwd="krish", database="mailclient")
    cursor = con.cursor()
    query = f"select exists(select * from ui_user where username = '{username}' and password = '{password}')"
    cursor.execute(query)
    if cursor.fetchone() == (1,):
        return 1
    else:
        return 0

def send_mail(sender,receiver,subject,body):
    con = mysql.connector.connect(host="localhost", user="root", passwd="krish", database="mailclient")
    cursor = con.cursor()
    query = "Insert into ui_mail (sender,receiver,subject,body,date_time) values('{}','{}','{}','{}',CURRENT_TIMESTAMP())".format(sender, receiver,
                                                                                                    subject, body)
    cursor.execute(query)
    con.commit()
