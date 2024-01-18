


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
from BD import *
import tkinter.messagebox as mb
from allwidjets import *
from modules import *





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
        self.number_zayavka_label = QtWidgets.QLabel("Номер заявки", self.Zayavki_group)
        self.number_zayavka_label.setGeometry(QtCore.QRect(20, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number_zayavka_label.setFont(font)
        self.number_zayavka_label.setObjectName("number_zayavka_label")
        self.status_zayavka_label = QtWidgets.QLabel("Статус", self.Zayavki_group)
        self.status_zayavka_label.setGeometry(QtCore.QRect(70, 140, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.status_zayavka_label.setFont(font)
        self.status_zayavka_label.setObjectName("status_zayavka_label")
        self.name_po_zayavka_label = QtWidgets.QLabel("Название ПО", self.Zayavki_group)
        self.name_po_zayavka_label.setGeometry(QtCore.QRect(370, 140, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_po_zayavka_label.setFont(font)
        self.name_po_zayavka_label.setObjectName("name_po_zayavka_label")
        self.version_po_zayavka_label = QtWidgets.QLabel("Версия ПО", self.Zayavki_group)
        self.version_po_zayavka_label.setGeometry(QtCore.QRect(680, 140, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.version_po_zayavka_label.setFont(font)
        self.version_po_zayavka_label.setObjectName("version_po_zayavka_label")
        self.login_zayavka_label = QtWidgets.QLabel("Логин", self.Zayavki_group)
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
        self.delete_zayavka_button = QtWidgets.QPushButton("Удалить", self.Zayavki_group)
        self.delete_zayavka_button.setGeometry(QtCore.QRect(70, 300, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.delete_zayavka_button.setFont(font)
        self.delete_zayavka_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_zayavka_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.delete_zayavka_button.setObjectName("delete_zayavka_button")
        self.add_zayavka_button = QtWidgets.QPushButton("Добавить", self.Zayavki_group)
        self.add_zayavka_button.setGeometry(QtCore.QRect(980, 310, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.add_zayavka_button.setFont(font)
        self.add_zayavka_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_zayavka_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.add_zayavka_button.setObjectName("add_zayavka_button")
        self.edit_zayavka_button = QtWidgets.QPushButton("Изменить", self.Zayavki_group)
        self.edit_zayavka_button.setGeometry(QtCore.QRect(540, 300, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.edit_zayavka_button.setFont(font)
        self.edit_zayavka_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_zayavka_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.edit_zayavka_button.setObjectName("edit_zayavka_button")
        self.zayavki_data_from_bd = QtWidgets.QTableWidget(self.zayavki_view)
        self.zayavki_data_from_bd.setGeometry(QtCore.QRect(10, 10, 1371, 351))
        self.zayavki_data_from_bd.setObjectName("zayavki_data_from_bd")
        self.zayavki_data_from_bd.setColumnCount(0)
        self.zayavki_data_from_bd.setRowCount(0)
        self.all_pages.addTab(self.zayavki_view, "Заявки")
        self.users_view = QtWidgets.QWidget()
        self.users_view.setObjectName("users_view")
        self.users_group = QtWidgets.QGroupBox(self.users_view)
        self.users_group.setGeometry(QtCore.QRect(10, 340, 1371, 461))
        self.users_group.setTitle("")
        self.users_group.setObjectName("users_group")
        self.F_U_users_label = QtWidgets.QLabel("Фамилия", self.users_group)
        self.F_U_users_label.setGeometry(QtCore.QRect(70, 30, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.F_U_users_label.setFont(font)
        self.F_U_users_label.setObjectName("F_U_users_label")
        self.I_U_users_label = QtWidgets.QLabel("Имя", self.users_group)
        self.I_U_users_label.setGeometry(QtCore.QRect(370, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.I_U_users_label.setFont(font)
        self.I_U_users_label.setObjectName("I_U_users_label")
        self.O_U_users_label = QtWidgets.QLabel("Отчество", self.users_group)
        self.O_U_users_label.setGeometry(QtCore.QRect(680, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.O_U_users_label.setFont(font)
        self.O_U_users_label.setObjectName("O_U_users_label")
        self.Email_users_label = QtWidgets.QLabel("Email", self.users_group)
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
        self.Email_users_input.setGeometry(QtCore.QRect(970, 80, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Email_users_input.setFont(font)
        self.Email_users_input.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.Email_users_input.setObjectName("Email_users_input")
        self.delete_users_button = QtWidgets.QPushButton("Удалить", self.users_group)
        self.delete_users_button.setGeometry(QtCore.QRect(70, 340, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.delete_users_button.setFont(font)
        self.delete_users_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_users_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.delete_users_button.setObjectName("delete_users_button")
        self.add_users_button = QtWidgets.QPushButton("Добавить", self.users_group)
        self.add_users_button.setGeometry(QtCore.QRect(980, 330, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.add_users_button.setFont(font)
        self.add_users_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_users_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.add_users_button.setObjectName("add_users_button")
        self.edit_users_button = QtWidgets.QPushButton("Изменить", self.users_group)
        self.edit_users_button.setGeometry(QtCore.QRect(540, 330, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.edit_users_button.setFont(font)
        self.edit_users_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_users_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.edit_users_button.setObjectName("edit_users_button")
        self.login_users_label = QtWidgets.QLabel("Логин", self.users_group)
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
        self.password_users_label = QtWidgets.QLabel( "Пароль", self.users_group)
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
        self.users_data_from_bd = QtWidgets.QTableWidget(self.users_view)
        self.users_data_from_bd.setGeometry(QtCore.QRect(0, 0, 1381, 331))
        self.users_data_from_bd.setObjectName("users_data_from_bd")
        self.users_data_from_bd.setColumnCount(0)
        self.users_data_from_bd.setRowCount(0)
        self.all_pages.addTab(self.users_view, "Пользователи")
        self.po_view = QtWidgets.QWidget()
        self.po_view.setObjectName("po_view")
        self.PO_group = QtWidgets.QGroupBox(self.po_view)
        self.PO_group.setGeometry(QtCore.QRect(10, 370, 1361, 431))
        self.PO_group.setTitle("")
        self.PO_group.setObjectName("PO_group")
        self.name_po_po_label = QtWidgets.QLabel("Название ПО", self.PO_group)
        self.name_po_po_label.setGeometry(QtCore.QRect(370, 140, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_po_po_label.setFont(font)
        self.name_po_po_label.setObjectName("name_po_po_label")
        self.version_po_po_label = QtWidgets.QLabel("Версия ПО", self.PO_group)
        self.version_po_po_label.setGeometry(QtCore.QRect(680, 140, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.version_po_po_label.setFont(font)
        self.version_po_po_label.setObjectName("version_po_po_label")
        self.kluch_po_label = QtWidgets.QLabel("Лицензионный ключ", self.PO_group)
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
        self.delete_po_button = QtWidgets.QPushButton("Удалить", self.PO_group)
        self.delete_po_button.setGeometry(QtCore.QRect(70, 300, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.delete_po_button.setFont(font)
        self.delete_po_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_po_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.delete_po_button.setObjectName("delete_po_button")
        self.add_po_button = QtWidgets.QPushButton("Добавить", self.PO_group)
        self.add_po_button.setGeometry(QtCore.QRect(980, 310, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.add_po_button.setFont(font)
        self.add_po_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_po_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.add_po_button.setObjectName("add_po_button")
        self.edit_po_button = QtWidgets.QPushButton("Изменить", self.PO_group)
        self.edit_po_button.setGeometry(QtCore.QRect(540, 300, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.edit_po_button.setFont(font)
        self.edit_po_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_po_button.setStyleSheet("background-color: rgb(181, 206, 245);")
        self.edit_po_button.setObjectName("edit_po_button")
        self.po_data_from_bd = QtWidgets.QTableWidget(self.po_view)
        self.po_data_from_bd.setGeometry(QtCore.QRect(0, 10, 1381, 341))
        self.po_data_from_bd.setObjectName("po_data_from_bd")
        self.po_data_from_bd.setColumnCount(0)
        self.po_data_from_bd.setRowCount(0)
        self.all_pages.addTab(self.po_view, "Программное обеспечение")
        self.errors_view = QtWidgets.QWidget()
        self.errors_view.setObjectName("errors_view")
        self.errors_group = QtWidgets.QGroupBox(self.errors_view)
        self.errors_group.setGeometry(QtCore.QRect(10, 190, 1371, 461))
        self.errors_group.setTitle("")
        self.errors_group.setObjectName("errors_group")
        self.name_error_label = QtWidgets.QLabel("Название ошибки", self.errors_group)
        self.name_error_label.setGeometry(QtCore.QRect(40, 70, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_error_label.setFont(font)
        self.name_error_label.setObjectName("name_error_label")
        self.about_error__label = QtWidgets.QLabel("Описание ошибки", self.errors_group)
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
        self.s = QtWidgets.QPushButton("Отправить", self.errors_group)
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
        self.all_pages.addTab(self.errors_view, "Ошибки")
        self.user_prelogin_info_label = QtWidgets.QLabel("Пользователь:", self.centralwidget)
        self.user_prelogin_info_label.setGeometry(QtCore.QRect(890, 0, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.user_prelogin_info_label.setFont(font)
        self.user_prelogin_info_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.user_prelogin_info_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_prelogin_info_label.setObjectName("user_prelogin_info_label")
        self.user_login_info = QtWidgets.QLabel("login", self.centralwidget)
        self.user_login_info.setGeometry(QtCore.QRect(1140, 0, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.user_login_info.setFont(font)
        self.user_login_info.setObjectName("user_login_info")
        
        self.all_pages.setCurrentIndex(0)
        

        self.fill_data_users()
        self.fill_data_zayavki()
        self.fill_data_po()

        self.set_buttons_click()

        self.edit_login = ""

        self.delete_po_button.hide()
        self.delete_users_button.hide()

        



    def set_name(self, my_login, role, dostup):
        self.user_login_info.setText(my_login)
        self.user_prelogin_info_label.setText(f"{role}:")
        self.dostup = dostup
        
    

# Установка действий на кнопки 
    def set_buttons_click(self):

        self.add_users_button.clicked.connect(self.register_user)
        self.edit_users_button.clicked.connect(self.edit_user)
        self.add_po_button.clicked.connect(self.add_po)
        self.s.clicked.connect(self.send_error)
        

    

# Регистрация нового пользователя
    def register_user(self):

        f_user = self.F_U_users_input.text()
        i_user = self.I_U_users_input.text()
        o_user = self.O_U_users_input.text()
        email_user = self.Email_users_input.text()
        login_user = self.login_users_input.text()
        password_user = self.password_users_input.text()

        auth = Autorization()

        if not f_user or not i_user or not email_user or not login_user or not password_user:
            mb.showerror("Ошибка", "Не все данные заполнены!")
            return
        if auth.check_login(login_user):
            mb.showerror("Ошибка", "Такой логин уже существует!")
            return

        get_data = Bd_get_data()
        dolj_id = get_data.get_iddolj(self.user_login_info.text())

        if dolj_id == 1:
            dolj_user = "Преподаватель"
        else:
            dolj_user = "Студент"

        
        registr = Registration()
        registr.registration(f_user, i_user, o_user, email_user, login_user, password_user, dolj_user)

        mb.showinfo("Информация", "Пользователь добавлен")
        
        # self.users_data_from_bd.clear()
        # self.fill_data_users()

# Изменение данных пользователя
    def edit_user(self):

        
        f_user = self.F_U_users_input.text()
        i_user = self.I_U_users_input.text()
        o_user = self.O_U_users_input.text()
        email_user = self.Email_users_input.text()
        login_user = self.login_users_input.text()

        auth = Autorization()


        if not f_user or not i_user or not email_user or not login_user:
            mb.showerror("Ошибка", "Не все данные заполнены!")
            return
        if auth.check_login(login_user):
            
            if self.edit_login != login_user:
                mb.showerror("Ошибка", "Такой логин уже существует!")
                return

        id_user = int(auth.get_id(self.edit_login))


        get_data = Bd_get_data()
        dolj_id = get_data.get_iddolj(self.my_login)

        bd_edit = Bd_edit()
        bd_edit.edit_polz(id_user, f_user, i_user, o_user, email_user, login_user)

        mb.showinfo("Информация", "Пользователь изменен")









# Заполнение таблицы пользователей
    def fill_data_users(self):
        
        self.users_data_from_bd.setColumnCount(7)
        self.users_data_from_bd.setHorizontalHeaderLabels(["Номер пользователя", "Фамилия", "Имя", "Очество", "Email", "Логин", "Пароль"])
        
        self.users_data_from_bd.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.users_data_from_bd.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.users_data_from_bd.setSelectionMode(QAbstractItemView.SingleSelection)
        self.users_data_from_bd.itemSelectionChanged.connect(self.users_data_from_bd_click)

        bd_get = Bd_get_data()
        polz = bd_get.get_polz_view()
        for p in polz:
            rows = self.users_data_from_bd.rowCount()
            self.users_data_from_bd.setRowCount(rows + 1)
            self.users_data_from_bd.setItem(rows, 0, QTableWidgetItem(str(p[0])))
            self.users_data_from_bd.setItem(rows, 1, QTableWidgetItem(p[1]))
            self.users_data_from_bd.setItem(rows, 2, QTableWidgetItem(p[2]))
            self.users_data_from_bd.setItem(rows, 3, QTableWidgetItem(p[3]))
            self.users_data_from_bd.setItem(rows, 4, QTableWidgetItem(p[4]))
            self.users_data_from_bd.setItem(rows, 5, QTableWidgetItem(p[5]))
            self.users_data_from_bd.setItem(rows, 6, QTableWidgetItem("********"))


            rows = self.users_data_from_bd.rowCount()
            

      
        self.users_data_from_bd.resizeColumnsToContents()

# Получение данных при клике
    def users_data_from_bd_click(self):
        all_data = self.users_data_from_bd.selectedItems()
        
        self.F_U_users_input.setText(all_data[1].text())
        self.I_U_users_input.setText(all_data[2].text())
        self.O_U_users_input.setText(all_data[3].text())
        self.Email_users_input.setText(all_data[4].text())
        self.login_users_input.setText(all_data[5].text())

        self.edit_login = self.login_users_input.text()


        



# Заполнение таблицы заявок
    def fill_data_zayavki(self):
        
        self.zayavki_data_from_bd.setColumnCount(6)
        self.zayavki_data_from_bd.setHorizontalHeaderLabels(["Номер заявки", "Название ПО", "Версия ПО", "Статус", "ФИО", "Логин"])
        
        self.zayavki_data_from_bd.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.zayavki_data_from_bd.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.zayavki_data_from_bd.setSelectionMode(QAbstractItemView.SingleSelection)
        self.zayavki_data_from_bd.itemSelectionChanged.connect(self.zayavki_data_from_bd_click)

        bd_get = Bd_get_data()
        polz = bd_get.get_zayavki_view()
        for p in polz:
            rows = self.users_data_from_bd.rowCount()
            self.zayavki_data_from_bd.setRowCount(rows + 1)
            self.zayavki_data_from_bd.setItem(rows, 0, QTableWidgetItem(str(p[0])))
            self.zayavki_data_from_bd.setItem(rows, 1, QTableWidgetItem(p[1]))
            self.zayavki_data_from_bd.setItem(rows, 2, QTableWidgetItem(p[2]))
            self.zayavki_data_from_bd.setItem(rows, 3, QTableWidgetItem(p[3]))
            self.zayavki_data_from_bd.setItem(rows, 4, QTableWidgetItem(p[4]))
            self.zayavki_data_from_bd.setItem(rows, 5, QTableWidgetItem("ФИО"))
            self.zayavki_data_from_bd.setItem(rows, 6, QTableWidgetItem(p[6]))

            rows = self.zayavki_data_from_bd.rowCount()
            

      
        self.zayavki_data_from_bd.resizeColumnsToContents()


# Получение данных при клике
    def zayavki_data_from_bd_click(self):
        all_data = self.users_data_from_bd.selectedItems()
        
        self.status_zayavka_input.setText(all_data[1].text())
        self.name_po_zayavka_input.setText(all_data[2].text())
        self.version_po_zayavka_input.setText(all_data[3].text())
        self.login_zayavka_input.setText(all_data[4].text())
        

        self.edit_login = self.login_users_input.text()


# Добавление заявок
    def add_zayavki(self):

        status = self.status_zayavka_input.text()
        name_po = self.name_po_zayavka_input.text()
        vers_po = self.version_po_zayavka_input.text()
        login_zayavki = self.login_zayavka_input.text()
       
        
        registr = Registration()
        registr.registration(f_user, i_user, o_user, email_user, login_user, password_user, dolj_user)

        mb.showinfo("Информация", "Пользователь добавлен")



# Заполнение таблицы заявок
    def fill_data_po(self):
        
        self.po_data_from_bd.setColumnCount(4)
        self.po_data_from_bd.setHorizontalHeaderLabels(["Номер ПО", "Название ПО", "Версия ПО", "Количество"])
        
        self.po_data_from_bd.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.po_data_from_bd.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.po_data_from_bd.setSelectionMode(QAbstractItemView.SingleSelection)
        self.po_data_from_bd.itemSelectionChanged.connect(self.po_data_from_bd_click)

        bd_get = Bd_get_data()
        po = bd_get.get_po_view()
        for p in po:
            rows = self.po_data_from_bd.rowCount()
            self.po_data_from_bd.setRowCount(rows + 1)
            self.po_data_from_bd.setItem(rows, 0, QTableWidgetItem(str(p[0])))
            self.po_data_from_bd.setItem(rows, 1, QTableWidgetItem(p[1]))
            self.po_data_from_bd.setItem(rows, 2, QTableWidgetItem(p[3]))
            self.po_data_from_bd.setItem(rows, 3, QTableWidgetItem(str(p[2])))

            rows = self.po_data_from_bd.rowCount()
            

      
        self.po_data_from_bd.resizeColumnsToContents()


# Получение данных при клике
    def po_data_from_bd_click(self):
        all_data = self.po_data_from_bd.selectedItems()
        
        self.name_po_po_input.setText(all_data[1].text())
        self.version_po_po_input.setText(all_data[2].text())
        
        




# Добавление ПО
    def add_po(self):

        name_po = self.name_po_po_input.text()
        vers_po = self.version_po_po_input.text()
        kluch_po = self.kluch_po_input.text()

        if not name_po or not vers_po:
            mb.showerror("Ошибка", "Не все данные заполнены!")
            return

        add_po = Bd_add()
        add_po.add_po(name_po, 0, vers_po)

        mb.showinfo("Информация", "ПО добавлено")


# Отправка сообщений об ошибках
    def send_error(self):
        
        name_error =  self.name_error_input.text()
        opisanie = self.about_error_input.toPlainText()

        bd_get = Bd_get_data()
        fio = bd_get.get_fio(self.user_login_info.text())
        f = fio[0].replace("'","").replace(",","")
        i = fio[1].replace("'","").replace(",","")
        o = fio[2].replace("'","").replace(",","")
        fio = f"{f} {i} {o}"

        send_mail = Send_email()
        send_mail.send("ychet.po", "swfi ciqc lani rhvm" ,"ychet.po@gmail.com", send_mail.errorHtml(fio, opisanie))
        mb.showinfo("Info", "Сообщение об ошибке отправлено")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())