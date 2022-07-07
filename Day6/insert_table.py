import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vivek",
    database="mydemo"
)
mycursor = conn.cursor()

# mycursor.execute("CREATE DATABASE mydemo")

sql = "INSERT INTO tbl_user (user_id,user_firstname, user_lastname, user_address, user_email,user_password) VALUES (1,'Vivek', 'Sangadiya','hifli, navin Society', 'vivek@gmail.com', 123456);"
sql = "INSERT INTO tbl_user (user_id,user_firstname, user_lastname, user_address, user_email,user_password) VALUES (2,'Sagar', 'Sangadiya','hifli, navin Society', 'vivek@gmail.com', 234567);"
mycursor.execute(sql)
conn.commit()
print(mycursor.rowcount, "row inserted.")