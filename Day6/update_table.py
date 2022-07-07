import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vivek",
    database="mydemo"
)
mycursor = conn.cursor()
sql = "UPDATE tbl_user SET user_firstname = 'Aarohi' WHERE user_id  = 1"
mycursor.execute(sql)
conn.commit()
print(mycursor.rowcount, "row updated")