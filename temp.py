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

        except Error as e:
            print("Error while connecting to MYSQL", e)

    def __del__(self):
        if self.cxn.is_connected():
            self.cursor.close()
            self.cxn.close()

    def displayTable(self, table):
        # SELECTING a TABLE and Displaying Information
        self.cursor.execute("""SELECT * FROM {tab}""".format(tab=table))
        record = self.cursor.fetchall()
        return record

    def selectRecordFromArtist(self, Data):
        self.cursor.execute("""SELECT * FROM artist WHERE FLname= '{data}' OR phone= '{data}' OR address= '{data}' 
           OR birthPlace= '{data}' OR age= '{data'}' OR styleOfArt= '{data}'""".format(data=Data))
        record = self.cursor.fetchall()
        return record

    def selectRecordFromArtShows(self, Data):
        self.cursor.execute("""SELECT * FROM artshows WHERE contactNumber= '{data}' OR contact= '{data}' OR location= '{data}' 
            OR dateShow= '{data}' OR timeShow= '{data'}'""".format(data=Data))
        record = self.cursor.fetchall()
        return record

    def selectRecordFromArtWork(self, Data):
        self.cursor.execute("""SELECT * FROM artwork WHERE typeOfArt= '{data}' OR dateCreated= '{data}' OR dateAcquired= '{data}' 
            OR price= '{data}' OR location= '{data'}' OR title='{data{'""".format(data=Data))
        record = self.cursor.fetchall()
        return record

    def selectRecordFromCustomer(self, Data):
        self.cursor.execute("""SELECT * FROM Customer WHERE artPreference= '{data}' OR phone= '{data}' 
           OR customerNumber= '{data}' """.format(data=Data))
        record = self.cursor.fetchall()
        return record

    def sortASC(self):
        self.cursor.execute("""SELECT * FROM customer ORDER BY customerNumber ASC """)
        record = self.cursor.fetchall()
        return record

    def sortDESC(self):
        self.cursor.execute("""SELECT * FROM customer ORDER BY customerNumber DESC """)
        record = self.cursor.fetchall()
        return record


db = Art_Gallery("root", "Python1!", "art_gallery")