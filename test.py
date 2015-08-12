from PySide import QtCore, QtGui
from mainwindow import Ui_TestMainWindow

import sys

class TestWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(TestWindow, self).__init__(parent)
        self._ui = Ui_TestMainWindow()
        self._ui.setupUi(self)

        self._ui.button.pressed.connect(self._btnPressed)

    def _btnPressed(self):
        QtGui.QMessageBox.information(self, 'Hello World!', 'Hello World!', QtGui.QMessageBox.Ok)
        self._ui.statusbar.showMessage("You pressed the button!")

def RunTest():
    app = QtGui.QApplication(sys.argv)

    wnd = TestWindow()
    wnd.show()

    app.exec_()

if __name__ == "__main__":
    RunTest()
