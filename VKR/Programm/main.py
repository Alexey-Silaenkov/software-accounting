# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from BD import *
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1389, 895)
        MainWindow.setStyleSheet("background-color: rgb(135, 163, 201);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.all_pages = QtWidgets.QTabWidget(self.centralwidget)
        self.all_pages.setGeometry(QtCore.QRect(0, 40, 1391, 851))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.all_pages.setFont(font)
        self.all_pages.setStyleSheet("")
        self.all_pages.setObjectName("all_pages")
        self.zayavki_view = QtWidgets.QWidget()
        self.zayavki_view.setStyleSheet("")
        self.zayavki_view.setObjectName("zayavki_view")
        self.Zayavki_group = QtWidgets.QGroupBox(self.zayavki_view)
        self.Zayavki_group.setGeometry(QtCore.QRect(0, 380, 1381, 461))
        self.Zayavki_group.setTitle("")
        self.Zayavki_group.setObjectName("Zayavki_group")
        self.number_zayavka_label = QtWidgets.QLabel(self.Zayavki_group)
        self.number_zayavka_label.setGeometry(QtCore.QRect(20, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number_zayavka_label.setFont(font)
        self.number_zayavka_label.setObjectName("number_zayavka_label")
        self.status_zayavka_label = QtWidgets.QLabel(self.Zayavki_group)
        self.status_zayavka_label.setGeometry(QtCore.QRect(70, 140, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.status_zayavka_label.setFont(font)
        self.status_zayavka_label.setObjectName("status_zayavka_label")
        self.name_po_zayavka_label = QtWidgets.QLabel(self.Zayavki_group)
        self.name_po_zayavka_label.setGeometry(QtCore.QRect(370, 140, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_po_zayavka_label.setFont(font)
        self.name_po_zayavka_label.setObjectName("name_po_zayavka_label")
        self.version_po_zayavka_label = QtWidgets.QLabel(self.Zayavki_group)
        self.version_po_zayavka_label.setGeometry(QtCore.QRect(680, 140, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.version_po_zayavka_label.setFont(font)
        self.version_po_zayavka_label.setObjectName("version_po_zayavka_label")
        self.login_zayavka_label = QtWidgets.QLabel(self.Zayavki_group)
        self.login_zayavka_label.setGeometry(QtCore.QRect(980, 140, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.login_zayavka_label.setFont(font)
        self.login_zayavka_label.setObjectName("login_zayavka_label")
        self.status_zayavka_input = QtWidgets.QLineEdit(self.Zayavki_group)
        self.status_zayavka_input.setGeometry(QtCore.QRect(70, 190, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.status_zayavka_input.setFont(font)
        self.status_zayavka_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.status_zayavka_input.setObjectName("status_zayavka_input")
        self.name_po_zayavka_input = QtWidgets.QLineEdit(self.Zayavki_group)
        self.name_po_zayavka_input.setGeometry(QtCore.QRect(370, 190, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_po_zayavka_input.setFont(font)
        self.name_po_zayavka_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.name_po_zayavka_input.setObjectName("name_po_zayavka_input")
        self.version_po_zayavka_input = QtWidgets.QLineEdit(self.Zayavki_group)
        self.version_po_zayavka_input.setGeometry(QtCore.QRect(680, 190, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.version_po_zayavka_input.setFont(font)
        self.version_po_zayavka_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.version_po_zayavka_input.setObjectName("version_po_zayavka_input")
        self.login_zayavka_input = QtWidgets.QLineEdit(self.Zayavki_group)
        self.login_zayavka_input.setGeometry(QtCore.QRect(980, 190, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.login_zayavka_input.setFont(font)
        self.login_zayavka_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.login_zayavka_input.setObjectName("login_zayavka_input")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.Zayavki_group)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.delete_zayavka_button = QtWidgets.QPushButton(self.Zayavki_group)
        self.delete_zayavka_button.setGeometry(QtCore.QRect(70, 300, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.delete_zayavka_button.setFont(font)
        self.delete_zayavka_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_zayavka_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.delete_zayavka_button.setObjectName("delete_zayavka_button")
        self.add_zayavka_button = QtWidgets.QPushButton(self.Zayavki_group)
        self.add_zayavka_button.setGeometry(QtCore.QRect(980, 310, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.add_zayavka_button.setFont(font)
        self.add_zayavka_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_zayavka_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.add_zayavka_button.setObjectName("add_zayavka_button")
        self.edit_zayavka_button = QtWidgets.QPushButton(self.Zayavki_group)
        self.edit_zayavka_button.setGeometry(QtCore.QRect(540, 300, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.edit_zayavka_button.setFont(font)
        self.edit_zayavka_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_zayavka_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.edit_zayavka_button.setObjectName("edit_zayavka_button")
        self.all_pages.addTab(self.zayavki_view, "")
        self.users_view = QtWidgets.QWidget()
        self.users_view.setObjectName("users_view")
        self.users_group = QtWidgets.QGroupBox(self.users_view)
        self.users_group.setGeometry(QtCore.QRect(10, 340, 1371, 461))
        self.users_group.setTitle("")
        self.users_group.setObjectName("users_group")
        self.F_U_users_label = QtWidgets.QLabel(self.users_group)
        self.F_U_users_label.setGeometry(QtCore.QRect(70, 30, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.F_U_users_label.setFont(font)
        self.F_U_users_label.setObjectName("F_U_users_label")
        self.I_U_users_label = QtWidgets.QLabel(self.users_group)
        self.I_U_users_label.setGeometry(QtCore.QRect(370, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.I_U_users_label.setFont(font)
        self.I_U_users_label.setObjectName("I_U_users_label")
        self.O_U_users_label = QtWidgets.QLabel(self.users_group)
        self.O_U_users_label.setGeometry(QtCore.QRect(680, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.O_U_users_label.setFont(font)
        self.O_U_users_label.setObjectName("O_U_users_label")
        self.Email_users_label = QtWidgets.QLabel(self.users_group)
        self.Email_users_label.setGeometry(QtCore.QRect(980, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Email_users_label.setFont(font)
        self.Email_users_label.setObjectName("Email_users_label")
        self.F_U_users_input = QtWidgets.QLineEdit(self.users_group)
        self.F_U_users_input.setGeometry(QtCore.QRect(70, 80, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.F_U_users_input.setFont(font)
        self.F_U_users_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.F_U_users_input.setObjectName("F_U_users_input")
        self.I_U_users_input = QtWidgets.QLineEdit(self.users_group)
        self.I_U_users_input.setGeometry(QtCore.QRect(360, 80, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.I_U_users_input.setFont(font)
        self.I_U_users_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.I_U_users_input.setObjectName("I_U_users_input")
        self.O_U_users_input = QtWidgets.QLineEdit(self.users_group)
        self.O_U_users_input.setGeometry(QtCore.QRect(680, 80, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.O_U_users_input.setFont(font)
        self.O_U_users_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.O_U_users_input.setObjectName("O_U_users_input")
        self.Email_users_input = QtWidgets.QLineEdit(self.users_group)
        self.Email_users_input.setGeometry(QtCore.QRect(970, 80, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Email_users_input.setFont(font)
        self.Email_users_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.Email_users_input.setObjectName("Email_users_input")
        self.delete_users_button = QtWidgets.QPushButton(self.users_group)
        self.delete_users_button.setGeometry(QtCore.QRect(70, 340, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.delete_users_button.setFont(font)
        self.delete_users_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_users_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.delete_users_button.setObjectName("delete_users_button")
        self.add_users_button = QtWidgets.QPushButton(self.users_group)
        self.add_users_button.setGeometry(QtCore.QRect(980, 330, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.add_users_button.setFont(font)
        self.add_users_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_users_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.add_users_button.setObjectName("add_users_button")
        self.edit_users_button = QtWidgets.QPushButton(self.users_group)
        self.edit_users_button.setGeometry(QtCore.QRect(540, 330, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.edit_users_button.setFont(font)
        self.edit_users_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_users_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.edit_users_button.setObjectName("edit_users_button")
        self.login_users_label = QtWidgets.QLabel(self.users_group)
        self.login_users_label.setGeometry(QtCore.QRect(360, 160, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.login_users_label.setFont(font)
        self.login_users_label.setObjectName("login_users_label")
        self.login_users_input = QtWidgets.QLineEdit(self.users_group)
        self.login_users_input.setGeometry(QtCore.QRect(360, 210, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.login_users_input.setFont(font)
        self.login_users_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.login_users_input.setObjectName("login_users_input")
        self.password_users_input = QtWidgets.QLineEdit(self.users_group)
        self.password_users_input.setGeometry(QtCore.QRect(680, 210, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password_users_input.setFont(font)
        self.password_users_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.password_users_input.setObjectName("password_users_input")
        self.password_users_label = QtWidgets.QLabel(self.users_group)
        self.password_users_label.setGeometry(QtCore.QRect(680, 160, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password_users_label.setFont(font)
        self.password_users_label.setObjectName("password_users_label")
        self.I_U_users_label.raise_()
        self.F_U_users_label.raise_()
        self.O_U_users_label.raise_()
        self.Email_users_label.raise_()
        self.F_U_users_input.raise_()
        self.I_U_users_input.raise_()
        self.O_U_users_input.raise_()
        self.Email_users_input.raise_()
        self.delete_users_button.raise_()
        self.add_users_button.raise_()
        self.edit_users_button.raise_()
        self.login_users_label.raise_()
        self.login_users_input.raise_()
        self.password_users_input.raise_()
        self.password_users_label.raise_()
        self.tableWidget = QtWidgets.QTableWidget(self.users_view)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1381, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.all_pages.addTab(self.users_view, "")
        self.po_view = QtWidgets.QWidget()
        self.po_view.setObjectName("po_view")
        self.PO_group = QtWidgets.QGroupBox(self.po_view)
        self.PO_group.setGeometry(QtCore.QRect(10, 370, 1361, 431))
        self.PO_group.setTitle("")
        self.PO_group.setObjectName("PO_group")
        self.name_po_po_label = QtWidgets.QLabel(self.PO_group)
        self.name_po_po_label.setGeometry(QtCore.QRect(370, 140, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_po_po_label.setFont(font)
        self.name_po_po_label.setObjectName("name_po_po_label")
        self.version_po_po_label = QtWidgets.QLabel(self.PO_group)
        self.version_po_po_label.setGeometry(QtCore.QRect(680, 140, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.version_po_po_label.setFont(font)
        self.version_po_po_label.setObjectName("version_po_po_label")
        self.kluch_po_label = QtWidgets.QLabel(self.PO_group)
        self.kluch_po_label.setGeometry(QtCore.QRect(980, 140, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.kluch_po_label.setFont(font)
        self.kluch_po_label.setObjectName("kluch_po_label")
        self.name_po_po_input = QtWidgets.QLineEdit(self.PO_group)
        self.name_po_po_input.setGeometry(QtCore.QRect(370, 190, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_po_po_input.setFont(font)
        self.name_po_po_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.name_po_po_input.setObjectName("name_po_po_input")
        self.version_po_po_input = QtWidgets.QLineEdit(self.PO_group)
        self.version_po_po_input.setGeometry(QtCore.QRect(680, 190, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.version_po_po_input.setFont(font)
        self.version_po_po_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.version_po_po_input.setObjectName("version_po_po_input")
        self.kluch_po_input = QtWidgets.QLineEdit(self.PO_group)
        self.kluch_po_input.setGeometry(QtCore.QRect(980, 190, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.kluch_po_input.setFont(font)
        self.kluch_po_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.kluch_po_input.setObjectName("kluch_po_input")
        self.delete_po_button = QtWidgets.QPushButton(self.PO_group)
        self.delete_po_button.setGeometry(QtCore.QRect(70, 300, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.delete_po_button.setFont(font)
        self.delete_po_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_po_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.delete_po_button.setObjectName("delete_po_button")
        self.add_po_button = QtWidgets.QPushButton(self.PO_group)
        self.add_po_button.setGeometry(QtCore.QRect(980, 310, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.add_po_button.setFont(font)
        self.add_po_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_po_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.add_po_button.setObjectName("add_po_button")
        self.edit_po_button = QtWidgets.QPushButton(self.PO_group)
        self.edit_po_button.setGeometry(QtCore.QRect(540, 300, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.edit_po_button.setFont(font)
        self.edit_po_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_po_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.edit_po_button.setObjectName("edit_po_button")
        self.all_pages.addTab(self.po_view, "")
        self.errors_view = QtWidgets.QWidget()
        self.errors_view.setObjectName("errors_view")
        self.errors_group = QtWidgets.QGroupBox(self.errors_view)
        self.errors_group.setGeometry(QtCore.QRect(10, 190, 1371, 461))
        self.errors_group.setTitle("")
        self.errors_group.setObjectName("errors_group")
        self.name_error_label = QtWidgets.QLabel(self.errors_group)
        self.name_error_label.setGeometry(QtCore.QRect(40, 70, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_error_label.setFont(font)
        self.name_error_label.setObjectName("name_error_label")
        self.about_error__label = QtWidgets.QLabel(self.errors_group)
        self.about_error__label.setGeometry(QtCore.QRect(300, 70, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.about_error__label.setFont(font)
        self.about_error__label.setObjectName("about_error__label")
        self.name_error_input = QtWidgets.QLineEdit(self.errors_group)
        self.name_error_input.setGeometry(QtCore.QRect(40, 110, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_error_input.setFont(font)
        self.name_error_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.name_error_input.setObjectName("name_error_input")
        self.s = QtWidgets.QPushButton(self.errors_group)
        self.s.setGeometry(QtCore.QRect(1080, 320, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.s.setFont(font)
        self.s.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.s.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.s.setObjectName("s")
        self.about_error_input = QtWidgets.QTextEdit(self.errors_group)
        self.about_error_input.setGeometry(QtCore.QRect(300, 110, 751, 301))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.about_error_input.setFont(font)
        self.about_error_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.about_error_input.setObjectName("about_error_input")
        self.all_pages.addTab(self.errors_view, "")
        self.user_prelogin_info_label = QtWidgets.QLabel(self.centralwidget)
        self.user_prelogin_info_label.setGeometry(QtCore.QRect(940, 0, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.user_prelogin_info_label.setFont(font)
        self.user_prelogin_info_label.setObjectName("user_prelogin_info_label")
        self.user_login_info = QtWidgets.QLabel(self.centralwidget)
        self.user_login_info.setGeometry(QtCore.QRect(1140, 0, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.user_login_info.setFont(font)
        self.user_login_info.setObjectName("user_login_info")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.all_pages.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.fill_data_users()







    def fill_data_users(self):
        
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["Номер пользователя", "Фамилия", "Имя", "Очество", "Email", "Логин", "Пароль"])
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.itemSelectionChanged.connect(self.func1)

        bd_get = Bd_get_data()
        polz = bd_get.get_polz_view()
        for p in polz:
            rows = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rows + 1)
            self.tableWidget.setItem(rows, 0, QTableWidgetItem(str(p[0])))
            self.tableWidget.setItem(rows, 1, QTableWidgetItem(p[1]))
            self.tableWidget.setItem(rows, 2, QTableWidgetItem(p[2]))
            self.tableWidget.setItem(rows, 3, QTableWidgetItem(p[3]))
            self.tableWidget.setItem(rows, 4, QTableWidgetItem(p[4]))
            self.tableWidget.setItem(rows, 5, QTableWidgetItem(p[5]))
            self.tableWidget.setItem(rows, 6, QTableWidgetItem(p[6]))

            rows = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rows + 1)
            self.tableWidget.setItem(rows, 0, QTableWidgetItem(str(p[0])))
            self.tableWidget.setItem(rows, 1, QTableWidgetItem(p[1]))
            self.tableWidget.setItem(rows, 2, QTableWidgetItem(p[2]))
            self.tableWidget.setItem(rows, 3, QTableWidgetItem(p[3]))
            self.tableWidget.setItem(rows, 4, QTableWidgetItem(p[4]))
            self.tableWidget.setItem(rows, 5, QTableWidgetItem(p[5]))
            self.tableWidget.setItem(rows, 6, QTableWidgetItem(p[6]))

      
        self.tableWidget.resizeColumnsToContents()

    def func1 (self):
        all_data = self.tableWidget.selectedItems()
        print (all_data[0].text())
        print (all_data[1].text())
        print (all_data[2].text())
        print (all_data[3].text())
        print (all_data[4].text())
        print (all_data[5].text())
        print (all_data[6].text())
         




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.number_zayavka_label.setText(_translate("MainWindow", "Номер заявки"))
        self.status_zayavka_label.setText(_translate("MainWindow", "Статус"))
        self.name_po_zayavka_label.setText(_translate("MainWindow", "Название ПО"))
        self.version_po_zayavka_label.setText(_translate("MainWindow", "Версия ПО"))
        self.login_zayavka_label.setText(_translate("MainWindow", "Логин"))
        self.delete_zayavka_button.setText(_translate("MainWindow", "Удалить"))
        self.add_zayavka_button.setText(_translate("MainWindow", "Добавить"))
        self.edit_zayavka_button.setText(_translate("MainWindow", "Изменить"))
        self.all_pages.setTabText(self.all_pages.indexOf(self.zayavki_view), _translate("MainWindow", "Заявки"))
        self.F_U_users_label.setText(_translate("MainWindow", "Фамилия"))
        self.I_U_users_label.setText(_translate("MainWindow", "Имя"))
        self.O_U_users_label.setText(_translate("MainWindow", "Отчество"))
        self.Email_users_label.setText(_translate("MainWindow", "Email"))
        self.delete_users_button.setText(_translate("MainWindow", "Удалить"))
        self.add_users_button.setText(_translate("MainWindow", "Добавить"))
        self.edit_users_button.setText(_translate("MainWindow", "Изменить"))
        self.login_users_label.setText(_translate("MainWindow", "Логин"))
        self.password_users_label.setText(_translate("MainWindow", "Пароль"))
        self.all_pages.setTabText(self.all_pages.indexOf(self.users_view), _translate("MainWindow", "Пользователи"))
        self.name_po_po_label.setText(_translate("MainWindow", "Название ПО"))
        self.version_po_po_label.setText(_translate("MainWindow", "Версия ПО"))
        self.kluch_po_label.setText(_translate("MainWindow", "Лицензионный ключ"))
        self.delete_po_button.setText(_translate("MainWindow", "Удалить"))
        self.add_po_button.setText(_translate("MainWindow", "Добавить"))
        self.edit_po_button.setText(_translate("MainWindow", "Изменить"))
        self.all_pages.setTabText(self.all_pages.indexOf(self.po_view), _translate("MainWindow", "Программное обеспечение"))
        self.name_error_label.setText(_translate("MainWindow", "Название ошибки"))
        self.about_error__label.setText(_translate("MainWindow", "Описание ошибки"))
        self.s.setText(_translate("MainWindow", "Отправить"))
        self.all_pages.setTabText(self.all_pages.indexOf(self.errors_view), _translate("MainWindow", "Ошибки"))
        self.user_prelogin_info_label.setText(_translate("MainWindow", "Пользователь:"))
        self.user_login_info.setText(_translate("MainWindow", "login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
