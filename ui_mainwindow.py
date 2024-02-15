# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowvghQKn.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QWidget)
import rc_ico

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(592, 294)
        icon = QIcon()
        icon.addFile(u":/newPrefix/Icons/password.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Container = QFrame(self.centralwidget)
        self.Container.setObjectName(u"Container")
        self.Container.setGeometry(QRect(0, 0, 671, 331))
        self.Container.setStyleSheet(u"QFrame#Container{\n"
"background-color: rgb(28, 40, 51);\n"
"}\n"
"\n"
"QLineEdit {\n"
"border:1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(45, 45, 45, 255), stop:1 rgba(97, 130, 171, 255));\n"
"border-radius:5px;	\n"
"color: rgb(247, 247, 247);\n"
"padding-right:5px;\n"
"padding-left:5px;\n"
"background-color: rgb(27, 38, 49);\n"
"}\n"
"\n"
"QGroupBox{\n"
"color: rgb(255, 255, 255);\n"
"border:1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(45, 45, 45, 255), stop:1 rgba(97, 130, 171, 255));\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"\n"
"border:1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(45, 45, 45, 255), stop:1 rgba(97, 130, 171, 255));\n"
"border-radius:5px;	\n"
"color: rgb(247, 247, 247);\n"
"padding-right:5px;\n"
"padding-left:5px;\n"
"background-color: rgb(27, 38, 49);\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.Container.setFrameShape(QFrame.StyledPanel)
        self.Container.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.Container)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 571, 61))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.HID_lineEdit = QLineEdit(self.groupBox)
        self.HID_lineEdit.setObjectName(u"HID_lineEdit")
        self.HID_lineEdit.setGeometry(QRect(10, 20, 511, 31))
        self.HID_lineEdit.setStyleSheet(u"background-color: rgb(229, 255, 241);\n"
"color: rgb(12, 12, 12);")
        self.HID_lineEdit.setReadOnly(True)
        self.Copy_id_Btn = QPushButton(self.groupBox)
        self.Copy_id_Btn.setObjectName(u"Copy_id_Btn")
        self.Copy_id_Btn.setGeometry(QRect(530, 20, 31, 31))
        self.Copy_id_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(28, 40, 51);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/Icons/files.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Copy_id_Btn.setIcon(icon1)
        self.Copy_id_Btn.setIconSize(QSize(28, 28))
        self.Copy_id_Btn.setFlat(False)
        self.groupBox_2 = QGroupBox(self.Container)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 80, 571, 161))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"")
        self.Name_lineEdit = QLineEdit(self.groupBox_2)
        self.Name_lineEdit.setObjectName(u"Name_lineEdit")
        self.Name_lineEdit.setGeometry(QRect(10, 40, 511, 31))
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 15, 41, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 70, 31, 31))
        self.label_4.setFont(font1)
        self.Key_textEdit = QTextEdit(self.groupBox_2)
        self.Key_textEdit.setObjectName(u"Key_textEdit")
        self.Key_textEdit.setGeometry(QRect(11, 100, 511, 51))
        self.Name_Paste_Btn = QPushButton(self.groupBox_2)
        self.Name_Paste_Btn.setObjectName(u"Name_Paste_Btn")
        self.Name_Paste_Btn.setGeometry(QRect(530, 40, 31, 31))
        self.Name_Paste_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(28, 40, 51);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/Icons/paste.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Name_Paste_Btn.setIcon(icon2)
        self.Name_Paste_Btn.setIconSize(QSize(28, 28))
        self.Name_Paste_Btn.setFlat(False)
        self.Copy_Key_Btn = QPushButton(self.groupBox_2)
        self.Copy_Key_Btn.setObjectName(u"Copy_Key_Btn")
        self.Copy_Key_Btn.setGeometry(QRect(530, 100, 31, 31))
        self.Copy_Key_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(28, 40, 51);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 3px;\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"}")
        self.Copy_Key_Btn.setIcon(icon1)
        self.Copy_Key_Btn.setIconSize(QSize(28, 28))
        self.Copy_Key_Btn.setFlat(False)
        self.Generate_Btn = QPushButton(self.Container)
        self.Generate_Btn.setObjectName(u"Generate_Btn")
        self.Generate_Btn.setGeometry(QRect(10, 250, 201, 31))
        self.Generate_Btn.setFont(font1)
        self.Generate_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(9, 132, 227);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(85, 161, 227);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/Icons/key.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Generate_Btn.setIcon(icon3)
        self.Close_Btn = QPushButton(self.Container)
        self.Close_Btn.setObjectName(u"Close_Btn")
        self.Close_Btn.setGeometry(QRect(390, 250, 191, 31))
        self.Close_Btn.setFont(font1)
        self.Close_Btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(214, 48, 49);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(209, 109, 114);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(223, 160, 5);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Serial Key Generator | https://laroussigsm.net/", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Hardware ID ", None))
        self.Copy_id_Btn.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Registration Information ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Key", None))
        self.Name_Paste_Btn.setText("")
        self.Copy_Key_Btn.setText("")
        self.Generate_Btn.setText(QCoreApplication.translate("MainWindow", u" Generate Activation Code", None))
        self.Close_Btn.setText(QCoreApplication.translate("MainWindow", u" Close", None))
    # retranslateUi

