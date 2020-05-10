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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 40, 781, 511))
        self.main_menu = QWidget()
        self.main_menu.setObjectName(u"main_menu")
        self.printRecords = QPushButton(self.main_menu)
        self.printRecords.setObjectName(u"printRecords")
        self.printRecords.setGeometry(QRect(280, 90, 201, 41))
        self.textBrowser = QTextBrowser(self.main_menu)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(230, 30, 291, 41))
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
        self.label = QLabel(self.print_records)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 70, 81, 21))
        self.textBrowser_3 = QTextBrowser(self.print_records)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(0, 70, 351, 131))
        self.ok_bttn_1 = QPushButton(self.print_records)
        self.ok_bttn_1.setObjectName(u"ok_bttn_1")
        self.ok_bttn_1.setGeometry(QRect(650, 70, 81, 21))
        self.table_widget_1 = QTableWidget(self.print_records)
        self.table_widget_1.setObjectName(u"table_widget_1")
        self.table_widget_1.setGeometry(QRect(400, 100, 371, 401))
        self.stackedWidget.addWidget(self.print_records)
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(190, 0, 401, 41))
        self.home_btn = QPushButton(self.centralwidget)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setGeometry(QRect(30, 0, 71, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


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
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; text-decoration: underline; color:#00007f;\">Art Gallery Database Simulation</span></p></body></html>", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
    # retranslateUi

