# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main-windowKXgOme.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(489, 959)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 281, 51))
        font = QFont()
        font.setFamily(u"Chalkboard")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.RichText)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 70, 261, 31))
        self.lineEdit.setLocale(QLocale(QLocale.Spanish, QLocale.Colombia))
        self.lineEdit.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhNoEditMenu)
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setFrame(True)
        self.lineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 120, 261, 31))
        self.lineEdit_2.setLocale(QLocale(QLocale.Spanish, QLocale.Colombia))
        self.lineEdit_2.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhNoEditMenu)
        self.lineEdit_2.setMaxLength(50)
        self.lineEdit_2.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.goToFinalLocationButton = QPushButton(self.centralwidget)
        self.goToFinalLocationButton.setObjectName(u"goToFinalLocationButton")
        self.goToFinalLocationButton.setGeometry(QRect(300, 70, 171, 81))
        self.goToFinalLocationButton.setAcceptDrops(False)
        self.goToFinalLocationButton.setAutoFillBackground(False)
        self.goToFinalLocationButton.setAutoDefault(True)
        self.goToFinalLocationButton.setFlat(False)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 170, 451, 731))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.gridLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame = QFrame(self.gridLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.gridLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.gridLayoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mapa de EAFIT", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d \u00bfD\u00f3nde est\u00e1s?", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d \u00bfA d\u00f3nde vamos?", None))
        self.goToFinalLocationButton.setText(QCoreApplication.translate("MainWindow", u"Ir", None))
    # retranslateUi

