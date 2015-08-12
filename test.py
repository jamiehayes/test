from PySide import QtCore, QtGui

import sys

class TestWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(TestWindow, self).__init__(parent)
        self.setWindowTitle(u"Hello World")

        layout = QtGui.QVBoxLayout()
        layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.setLayout(layout)

        btn = QtGui.QPushButton('Press Me', self)
        btn.pressed.connect(self._btnPressed)

    def _btnPressed(self):
        QtGui.QMessageBox.information(self, 'Hello World!', 'Hello World!', QtGui.QMessageBox.Ok)

def RunTest():
    app = QtGui.QApplication(sys.argv)

    wnd = TestWindow()
    wnd.show()

    app.exec_()

if __name__ == "__main__":
    RunTest()
