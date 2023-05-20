#Python Program to input data to mysql database
#(c) Sai Shibu
#Import pymysql module library
import pymysql
#Create a connection to MySQL Database 
conn =pymysql.connect(database="rohit",user="rohit",password="pass",host="localhost")
#Create a MySQL Cursor to that executes the SQLs
cur=conn.cursor()
#Create a dictonary containing the fields, name, age and place
data={'topic':'iot_sensor','sensorvalue':10.10}
#Execute the SQL to write data to the database
cur.execute("INSERT INTO rohit(topic, sensorvalue)VALUES(%(topic)s,%(sensorvalue)s);",data)
#Close the cursor
cur.close()
#Commit the data to the database
conn.commit()
#Close the connection to the database
conn.close()

#Open phpMyAdmin and see how the data is stored to the database
