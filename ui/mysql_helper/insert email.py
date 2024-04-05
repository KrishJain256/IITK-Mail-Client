import mysql.connector
con = mysql.connector.connect(host = "localhost",user = "root",passwd = "krish",database="mailclient")
cursor = con.cursor()

while True:
    sender = input("Enter sender : ")
    receiver = input("Enter receiver : ")
    subject = input("Enter subject : ")
    body = input("Enter body : ")


    query = "Insert into ui_mail (sender,receiver,subject,body) values('{}','{}','{}','{}')".format(sender,receiver,subject,body)
    cursor.execute(query)
    con.commit()

    if cursor.rowcount > 0:
        print("Data inserted")
    else:
        print("No Data Found. Some error!")
