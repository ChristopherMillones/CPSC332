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
        output(table, record)

    def selectRecord(self, FLname):
        self.cursor.execute("""SELECT * FROM artist WHERE FLname= '{name}'""".format(name=FLname))
        record = self.cursor.fetchall()
        output('artist', record)

    def sortASC(self):
        self.cursor.execute("""SELECT * FROM customer ORDER BY customerNumber ASC """)
        record = self.cursor.fetchall()
        print('\n')
        output('customer', record)

    def sortDESC(self):
        self.cursor.execute("""SELECT * FROM customer ORDER BY customerNumber DESC """)
        record = self.cursor.fetchall()
        print('\n')
        output('customer', record)



def action(i):
    db = Art_Gallery("root", "Python1!", "art_gallery")
    if i == "1":
        table_choice = input("\t---Enter Table---\n")
        db.displayTable(table_choice.lower())
    elif i == "2":
        FLname = input("Enter a Name to Search By:\t")
        db.selectRecord(FLname)

    elif i == "3":
        db.sortASC()

    elif i == "4":
        db.sortDESC()


def output(table, record):
    if table == "artist":
        for row in record:
            print("Full Name: ", row[0])
            print("Phone #: ", row[1])
            print("addy: ", row[2])
            print("brith place: ", row[3])
            print("Age: ", row[4])
            print("Style of Art: ", row[5], '\n\n')
    if table == "artshows":
        for row in record:
            print("Contact Number: ", row[0])
            print("Contact: ", row[1])
            print("Location: ", row[2])
            print("Date of Show: ", row[3])
            print("Time of Show: ", row[4], '\n\n')

    if table == "artwork":
        for row in record:
            print("Type of Art: ", row[0])
            print("Date Created: ", row[1])
            print("Date Acquired: ", row[2])
            print("Price of Art: ", row[3])
            print("Location of Art: ", row[4])
            print("Title of Art", row[5], '\n\n')

    if table == "customer":
        for row in record:
            print("Customer's Art Preference: ", row[0])
            print("Customer's Phone #: ", row[1])
            print("Customer's Number in Line: ", row[2], '\n\n')


print("\n\t"
      "---Welcome to Art Gallery database simulation---\n")

choice = input("Please select one of the following commands:"
               "\n(1)Display Records from a Table\n(2)Select Specific Record From Artist table"
               "\n(3)Order Customer Table by Customer Number (ASC)\n(4)Order Customer Table by "
               "Customer Number (DESC)\n(q) Quit\n")

while choice != "q" and choice != "Q":
    action(choice)
    choice = input("Please select one of the following commands:"
                   "\n(1)Display Records from a Table\n(2)Select Specific Record From Artist table"
                   "\n(3)Order Customer Table by Customer Number (ASC)\n(4)Order Customer Table by "
                   "Customer Number (DESC)\n(q) Quit\n")
else:
    print("\n\tThank you and Bye!\n")
