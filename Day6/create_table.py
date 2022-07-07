from dataclasses import dataclass
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vivek",
    database="mydemo"
)
mycursor = conn.cursor()

mycursor.execute("CREATE TABLE tbl_user(user_id varchar(255),user_firstname varchar(255),user_lastname varchar(255),user_address varchar(255),user_email varchar(255),user_password varchar(255))")