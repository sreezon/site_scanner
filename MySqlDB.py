import mysql.connector

class MySqlDB:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",user="root",password="abcd")
        self.table_name = 'port_history'
        self.database_name = 'scanner'
        db_create_query = "create database IF NOT EXISTS scanner"
        cursor = self.mydb.cursor()
        cursor.execute(db_create_query)
        self.mydb.commit()
        self.mydb.close()
        self.mydb = mysql.connector.connect(host="localhost",user="root",password="abcd", database=self.database_name)
        table_create_query = "create table IF NOT EXISTS port_history(\
        domain varchar(255),\
        open_ports varchar(3900),\
        ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\
        CONSTRAINT pk_history PRIMARY KEY (domain,ts))"

        cursor = self.mydb.cursor()
        cursor.execute(table_create_query)

        self.mydb.commit()
        self.mydb.close()

    def connect(self):
        self.mydb = mysql.connector.connect(host="localhost",user="root",password="abcd",database='scanner')

    def insertQuery(self, query):
        cursor = self.mydb.cursor()
        cursor.execute(query)
        self.mydb.commit()
        
    def executeQuery(self, query):
        cursor = self.mydb.cursor()
        cursor.execute(query)
        return cursor

    def close_connection(self):
        self.mydb.close()
        
    def get_table_name(self):
        return self.table_name
        
