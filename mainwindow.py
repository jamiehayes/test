# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Aug 12 01:07:36 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_TestMainWindow(object):
    def setupUi(self, TestMainWindow):
        TestMainWindow.setObjectName("TestMainWindow")
        TestMainWindow.resize(369, 265)
        self.centralwidget = QtGui.QWidget(TestMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtGui.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(140, 100, 75, 23))
        self.button.setObjectName("button")
        self.button2 = QtGui.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(40, 190, 75, 23))
        self.button2.setObjectName("button2")
        TestMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TestMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 369, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        TestMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(TestMainWindow)
        self.statusbar.setObjectName("statusbar")
        TestMainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(TestMainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(TestMainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), TestMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(TestMainWindow)

    def retranslateUi(self, TestMainWindow):
        TestMainWindow.setWindowTitle(QtGui.QApplication.translate("TestMainWindow", "PySide Test Window", None, QtGui.QApplication.UnicodeUTF8))
        self.button.setText(QtGui.QApplication.translate("TestMainWindow", "Press Me!", None, QtGui.QApplication.UnicodeUTF8))
        self.button2.setText(QtGui.QApplication.translate("TestMainWindow", "DoesNothing", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("TestMainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("TestMainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))

