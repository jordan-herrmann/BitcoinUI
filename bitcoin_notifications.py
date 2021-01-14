# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bitcoin_notifications.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 131)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pullButton = QtWidgets.QPushButton(self.centralwidget)
        self.pullButton.setGeometry(QtCore.QRect(208, 60, 151, 25))
        self.pullButton.setObjectName("pullButton")
        self.labelCrypto = QtWidgets.QLabel(self.centralwidget)
        self.labelCrypto.setGeometry(QtCore.QRect(11, 11, 107, 17))
        self.labelCrypto.setObjectName("labelCrypto")
        self.lineEditCrypto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCrypto.setGeometry(QtCore.QRect(10, 30, 142, 25))
        self.lineEditCrypto.setReadOnly(True)
        self.lineEditCrypto.setObjectName("lineEditCrypto")
        self.labelPrice = QtWidgets.QLabel(self.centralwidget)
        self.labelPrice.setGeometry(QtCore.QRect(160, 10, 132, 17))
        self.labelPrice.setObjectName("labelPrice")
        self.lineEditPrice = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPrice.setGeometry(QtCore.QRect(160, 30, 142, 25))
        self.lineEditPrice.setReadOnly(True)
        self.lineEditPrice.setObjectName("lineEditPrice")
        self.label24H = QtWidgets.QLabel(self.centralwidget)
        self.label24H.setGeometry(QtCore.QRect(310, 10, 81, 17))
        self.label24H.setObjectName("label24H")
        self.lineEdit24H = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit24H.setGeometry(QtCore.QRect(310, 30, 142, 25))
        self.lineEdit24H.setReadOnly(True)
        self.lineEdit24H.setObjectName("lineEdit24H")
        self.label1H = QtWidgets.QLabel(self.centralwidget)
        self.label1H.setGeometry(QtCore.QRect(460, 10, 72, 17))
        self.label1H.setObjectName("label1H")
        self.lineEdit1H = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1H.setGeometry(QtCore.QRect(460, 30, 142, 25))
        self.lineEdit1H.setReadOnly(True)
        self.lineEdit1H.setObjectName("lineEdit1H")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInstructions = QtWidgets.QAction(MainWindow)
        self.actionInstructions.setObjectName("actionInstructions")
        self.menuHelp.addAction(self.actionInstructions)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cryptocurrency Updater"))
        self.pullButton.setText(_translate("MainWindow", "Pull Updates"))
        self.labelCrypto.setText(_translate("MainWindow", "Cryptocurrency"))
        self.labelPrice.setText(_translate("MainWindow", "Current Price (USD)"))
        self.label24H.setText(_translate("MainWindow", "24h Change"))
        self.label1H.setText(_translate("MainWindow", "1h Change"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions"))
