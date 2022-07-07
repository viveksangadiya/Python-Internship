import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vivek"
)
mycursor = conn.cursor()

# mycursor.execute("CREATE DATABASE mydemo")

# sql = "INSERT INTO tbl_user (user_firstname, user_lastname, user_address, user_email,user_password) VALUES ('Vivek', 'Sangadiya','hifli, navin Society', 'vivek@gmail.com', 123456);"
# mycursor.execute(sql)
# conn.commit()
# print(mycursor.rowcount, "row inserted.")