import mysql
from mysql.connector import Error


class Art_Gallery:

    def __init__(self, user, password, database):
        try:
            self.cxn = mysql.connector.connect(user=user, password=password, database=database)
            # CONNECTING TO THE DATABASE
            if self.cxn.is_connected():
                db_info = self.cxn.get_server_info()
                self.cursor = self.cxn.cursor(prepared=True)
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
            self.cursor.execute("""SELECT TABLES""")
            self.tables = self.cursor.fetchall()
        except Error as e:
            print("Error while connecting to MYSQL", e)

    def __del__(self):
        if self.cxn.is_connected():
            self.cursor.close()
            self.cxn.close()

    def displayTable(self, table):
        for i in range(len(self.tables)):
            if table == self.tables[i]:
                # SELECTING a TABLE and Displaying Information
                self.cursor.execute("""SELECT * FROM {tab}""".format(tab=table))
                record = self.cursor.fetchall()
            else:
                print("ERROR TABLE NOT FOUND")

    def selectRecordFromArtist(self, Data):
        self.cursor.execute("""SELECT * FROM artist WHERE FLname= '{name}' OR phone= '{data}' OR address= '{data}' 
        OR birthPlace= '{data}' OR age= '{data'}' OR styleOfArt= '{data}'""".format(data=Data))
        record = self.cursor.fetchall()

    def selectRecordFromArtShows(self, Data):
        self.cursor.execute("""SELECT * FROM artshows WHERE contactNumber= '{name}' OR contact= '{data}' OR location= '{data}' 
         OR dateShow= '{data}' OR timeShow= '{data'}'""".format(data=Data))
        record = self.cursor.fetchall()

    def selectRecordFromArtWork(self, Data):
        self.cursor.execute("""SELECT * FROM artwork WHERE typeOfArt= '{name}' OR dateCreated= '{data}' OR dateAcquired= '{data}' 
         OR price= '{data}' OR location= '{data'}' OR title='{data{'""".format(data=Data))
        record = self.cursor.fetchall()

    def selectRecordFromCustomer(self, Data):
        self.cursor.execute("""SELECT * FROM Customer WHERE artPreference= '{name}' OR phone= '{data}' 
        OR customerNumber= '{data}' """.format(data=Data))
        record = self.cursor.fetchall()


    def sortASC(self):
        self.cursor.execute("""SELECT * FROM customer ORDER BY customerNumber ASC """)
        record = self.cursor.fetchall()
        print('\n')

    def sortDESC(self):
        self.cursor.execute("""SELECT * FROM customer ORDER BY customerNumber DESC """)
        record = self.cursor.fetchall()
        print('\n')
