# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'art_gallery.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1012, 640)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 40, 981, 541))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(163, 163, 163);")
        self.main_menu = QWidget()
        self.main_menu.setObjectName(u"main_menu")
        self.printRecords = QPushButton(self.main_menu)
        self.printRecords.setObjectName(u"printRecords")
        self.printRecords.setGeometry(QRect(370, 80, 201, 41))
        self.printRecords.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textBrowser = QTextBrowser(self.main_menu)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(330, 10, 291, 41))
        self.textBrowser.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.selectRecords = QPushButton(self.main_menu)
        self.selectRecords.setObjectName(u"selectRecords")
        self.selectRecords.setGeometry(QRect(370, 160, 201, 51))
        self.selectRecords.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.main_menu)
        self.print_records = QWidget()
        self.print_records.setObjectName(u"print_records")
        self.table_select_1 = QComboBox(self.print_records)
        self.table_select_1.addItem("")
        self.table_select_1.addItem("")
        self.table_select_1.addItem("")
        self.table_select_1.addItem("")
        self.table_select_1.setObjectName(u"table_select_1")
        self.table_select_1.setGeometry(QRect(530, 70, 101, 21))
        self.table_select_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(self.print_records)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 70, 81, 21))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textBrowser_3 = QTextBrowser(self.print_records)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(0, 70, 351, 131))
        self.textBrowser_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ok_bttn_1 = QPushButton(self.print_records)
        self.ok_bttn_1.setObjectName(u"ok_bttn_1")
        self.ok_bttn_1.setGeometry(QRect(650, 70, 81, 21))
        self.ok_bttn_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.table_widget_1 = QTableWidget(self.print_records)
        self.table_widget_1.setObjectName(u"table_widget_1")
        self.table_widget_1.setGeometry(QRect(360, 100, 621, 391))
        self.table_widget_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.print_records)
        self.select_record = QWidget()
        self.select_record.setObjectName(u"select_record")
        self.textBrowser_4 = QTextBrowser(self.select_record)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(10, 10, 361, 121))
        self.textBrowser_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.table_select_2 = QComboBox(self.select_record)
        self.table_select_2.addItem("")
        self.table_select_2.addItem("")
        self.table_select_2.addItem("")
        self.table_select_2.addItem("")
        self.table_select_2.setObjectName(u"table_select_2")
        self.table_select_2.setGeometry(QRect(490, 20, 101, 21))
        self.table_select_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.select_record)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 20, 81, 21))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ok_bttn_2 = QPushButton(self.select_record)
        self.ok_bttn_2.setObjectName(u"ok_bttn_2")
        self.ok_bttn_2.setGeometry(QRect(620, 110, 81, 21))
        self.ok_bttn_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.table_widget_2 = QTableWidget(self.select_record)
        self.table_widget_2.setObjectName(u"table_widget_2")
        self.table_widget_2.setGeometry(QRect(40, 180, 691, 271))
        self.table_widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.select_record)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(400, 110, 191, 21))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit.setMaxLength(20)
        self.stackedWidget.addWidget(self.select_record)
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(300, 0, 401, 41))
        self.home_btn = QPushButton(self.centralwidget)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setGeometry(QRect(30, 0, 71, 31))
        self.home_btn.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1012, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.printRecords.setText(QCoreApplication.translate("MainWindow", u"Print Records from the DB", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00007f;\">Welcome to the Main Menu!</span></p></body></html>", None))
        self.selectRecords.setText(QCoreApplication.translate("MainWindow", u"Select Record", None))
        self.table_select_1.setItemText(0, QCoreApplication.translate("MainWindow", u"Artist", None))
        self.table_select_1.setItemText(1, QCoreApplication.translate("MainWindow", u"Art Shows", None))
        self.table_select_1.setItemText(2, QCoreApplication.translate("MainWindow", u"Art Work", None))
        self.table_select_1.setItemText(3, QCoreApplication.translate("MainWindow", u"Customer", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Select a Table:", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00007f;\">How to use:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00007f;\">Use the Combo Box to select and table then click the &quot;Ok&quot; Button to confirm and display information.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#00007f;\"><br /></p></b"
                        "ody></html>", None))
        self.ok_bttn_1.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00007f;\">How to use:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00007f;\">Select a table then input data to see if it exist within the database or table</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#00007f;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:"
                        "empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#00007f;\"><br /></p></body></html>", None))
        self.table_select_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Artist", None))
        self.table_select_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Art Shows", None))
        self.table_select_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Art Work", None))
        self.table_select_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Customer", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select a Table:", None))
        self.ok_bttn_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"type here....", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; text-decoration: underline; color:#00007f;\">Art Gallery Database Simulation</span></p></body></html>", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
    # retranslateUi

