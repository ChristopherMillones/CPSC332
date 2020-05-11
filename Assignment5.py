import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide2 import QtCore, QtGui, QtWidgets
from art_gallery import Ui_MainWindow
import mysql
from mysql.connector import Error
import math

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

    def getColumnHeaders(self, table):
        self.cursor.execute("""SHOW COLUMNS FROM {tab}""".format(tab=table))
        record = self.cursor.fetchall()
        return record



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.PrintRecords()
        self.ok_btn_1()
        self.home_btn()
        self.setWindowTitle("Art Gallery DB Simulation")

        try:
            self.cxn = mysql.connector.connect(user = "root", password = "Python1!", database = "art_gallery")
            # CONNECTING TO THE DATABASE
            if self.cxn.is_connected():
                db_info = self.cxn.get_server_info()
                self.cursor = self.cxn.cursor(prepared=True)
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print(record)

        except Error as e:
            print("Error while connecting to MYSQL", e)



    def getColumnHeaders(self, table):
        self.cursor.execute("""SHOW COLUMNS FROM {tab}""".format(tab=table))
        record = self.cursor.fetchall()
        return record

    def displayTable(self, table):
        # SELECTING a TABLE and Displaying Information
        self.cursor.execute("""SELECT * FROM {tab}""".format(tab=table))
        record = self.cursor.fetchall()
        return record

    def PrintRecords(self):
        self.ui.printRecords.clicked.connect(self.menu1)

    def menu1(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def home(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def ok_btn_1(self):
        self.ui.ok_bttn_1.clicked.connect(self.test)

    def home_btn(self):
        self.ui.home_btn.clicked.connect(self.home)


    def test(self):
        rows = self.getColumnHeaders(self.ui.table_select_1.currentText().replace(" ","").lower())
        data = self.displayTable(self.ui.table_select_1.currentText().replace(" ","").lower())

        self.col = []


        for row in rows:
            self.col.append(row[0])

        self.ui.table_widget_1.setColumnCount(len(self.col))
        self.ui.table_widget_1.setRowCount(len(data))
        self.ui.table_widget_1.setHorizontalHeaderLabels(self.col)
        self.insertDataIntoTable(self.ui.table_select_1.currentText().replace(" ","").lower(),data)

    def insertDataIntoTable(self,table,data):

        if table == "artist":
                for x,row in zip(range(len(data)), data):
                    self.ui.table_widget_1.setItem(x, 0, QTableWidgetItem(row[0]))
                    self.ui.table_widget_1.setItem(x, 1, QTableWidgetItem(str(row[1])))
                    self.ui.table_widget_1.setItem(x, 2, QTableWidgetItem(row[2]))
                    self.ui.table_widget_1.setItem(x, 3, QTableWidgetItem(row[3]))
                    self.ui.table_widget_1.setItem(x, 4, QTableWidgetItem(str(row[4])))
                    self.ui.table_widget_1.setItem(x, 5, QTableWidgetItem(row[5]))






if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

