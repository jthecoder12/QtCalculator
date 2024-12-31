import sys

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QLineEdit, QPushButton, QStatusBar, QWidget, QApplication, QMainWindow)

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.error: bool = False

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(205, 500)
        MainWindow.setFixedSize(self.size())
        self.centralwidget: QWidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.result: QLineEdit = QLineEdit(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(0, 0, 201, 61))
        self.result.setStyleSheet(u"font-size:30px;")
        self.result.setReadOnly(True)
        self.oneButton: QPushButton = QPushButton(self.centralwidget)
        self.oneButton.setObjectName(u"oneButton")
        self.oneButton.setGeometry(QRect(10, 70, 51, 51))
        self.oneButton.setStyleSheet(u"font-size:40px;")
        self.oneButton.clicked.connect(self.oneClicked)
        self.twoButton: QPushButton = QPushButton(self.centralwidget)
        self.twoButton.setObjectName(u"twoButton")
        self.twoButton.setGeometry(QRect(80, 70, 51, 51))
        self.twoButton.setStyleSheet(u"font-size:40px;")
        self.twoButton.clicked.connect(self.twoClicked)
        self.threeButton: QPushButton = QPushButton(self.centralwidget)
        self.threeButton.setObjectName(u"threeButton")
        self.threeButton.setGeometry(QRect(150, 70, 51, 51))
        self.threeButton.setStyleSheet(u"font-size:40px;")
        self.threeButton.clicked.connect(self.threeClicked)
        self.fourButton: QPushButton = QPushButton(self.centralwidget)
        self.fourButton.setObjectName(u"fourButton")
        self.fourButton.setGeometry(QRect(10, 130, 51, 51))
        self.fourButton.setStyleSheet(u"font-size:40px;")
        self.fourButton.clicked.connect(self.fourClicked)
        self.fiveButton: QPushButton = QPushButton(self.centralwidget)
        self.fiveButton.setObjectName(u"fiveButton")
        self.fiveButton.setGeometry(QRect(80, 130, 51, 51))
        self.fiveButton.setStyleSheet(u"font-size:40px;")
        self.fiveButton.clicked.connect(self.fiveClicked)
        self.sixButton: QPushButton = QPushButton(self.centralwidget)
        self.sixButton.setObjectName(u"sixButton")
        self.sixButton.setGeometry(QRect(150, 130, 51, 51))
        self.sixButton.setStyleSheet(u"font-size:40px;")
        self.sixButton.clicked.connect(self.sixClicked)
        self.sevenButton: QPushButton = QPushButton(self.centralwidget)
        self.sevenButton.setObjectName(u"sevenButton")
        self.sevenButton.setGeometry(QRect(10, 190, 51, 51))
        self.sevenButton.setStyleSheet(u"font-size:40px;")
        self.sevenButton.clicked.connect(self.sevenClicked)
        self.eightButton: QPushButton = QPushButton(self.centralwidget)
        self.eightButton.setObjectName(u"eightButton")
        self.eightButton.setGeometry(QRect(80, 190, 51, 51))
        self.eightButton.setStyleSheet(u"font-size:40px;")
        self.eightButton.clicked.connect(self.eightClicked)
        self.nineButton: QPushButton = QPushButton(self.centralwidget)
        self.nineButton.setObjectName(u"nineButton")
        self.nineButton.setGeometry(QRect(150, 190, 51, 51))
        self.nineButton.setStyleSheet(u"font-size:40px;")
        self.nineButton.clicked.connect(self.nineClicked)
        self.zeroButton: QPushButton = QPushButton(self.centralwidget)
        self.zeroButton.setObjectName(u"zeroButton")
        self.zeroButton.setGeometry(QRect(10, 250, 191, 51))
        self.zeroButton.setStyleSheet(u"font-size:40px;")
        self.zeroButton.clicked.connect(self.zeroClicked)
        self.plusButton: QPushButton = QPushButton(self.centralwidget)
        self.plusButton.setObjectName(u"plusButton")
        self.plusButton.setGeometry(QRect(10, 310, 51, 51))
        self.plusButton.setStyleSheet(u"font-size:40px;")
        self.plusButton.clicked.connect(self.plusClicked)
        self.minusButton: QPushButton = QPushButton(self.centralwidget)
        self.minusButton.setObjectName(u"minusButton")
        self.minusButton.setGeometry(QRect(80, 310, 51, 51))
        self.minusButton.setStyleSheet(u"font-size:40px;")
        self.minusButton.clicked.connect(self.minusClicked)
        self.asteriskButton: QPushButton = QPushButton(self.centralwidget)
        self.asteriskButton.setObjectName(u"asteriskButton")
        self.asteriskButton.setGeometry(QRect(150, 310, 51, 51))
        self.asteriskButton.setStyleSheet(u"font-size:40px;")
        self.asteriskButton.clicked.connect(self.asteriskClicked)
        self.slashButton: QPushButton = QPushButton(self.centralwidget)
        self.slashButton.setObjectName(u"slashButton")
        self.slashButton.setGeometry(QRect(10, 370, 51, 51))
        self.slashButton.setStyleSheet(u"font-size:40px;")
        self.slashButton.clicked.connect(self.slashClicked)
        self.percentButton: QPushButton = QPushButton(self.centralwidget)
        self.percentButton.setObjectName(u"percentButton")
        self.percentButton.setGeometry(QRect(80, 370, 51, 51))
        self.percentButton.setStyleSheet(u"font-size:40px;")
        self.percentButton.clicked.connect(self.percentClicked)
        self.equalButton: QPushButton = QPushButton(self.centralwidget)
        self.equalButton.setObjectName(u"equalButton")
        self.equalButton.setGeometry(QRect(150, 370, 51, 51))
        self.equalButton.setStyleSheet(u"font-size:40px;")
        self.equalButton.clicked.connect(self.equalClicked)
        self.deleteButton: QPushButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(10, 430, 191, 51))
        self.deleteButton.setStyleSheet(u"font-size:40px;")
        self.deleteButton.clicked.connect(self.deleteClicked)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar: QPushButton = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.result.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.oneButton.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.twoButton.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.threeButton.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.fourButton.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.fiveButton.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.sixButton.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.sevenButton.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.eightButton.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.nineButton.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.zeroButton.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.plusButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.minusButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.asteriskButton.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.slashButton.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.percentButton.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.equalButton.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

    def oneClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()+"1")

    def twoClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()+"2")

    def threeClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()+"3")

    def fourClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()+"4")

    def fiveClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()+"5")

    def sixClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()+"6")

    def sevenClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()+"7")

    def eightClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()+"8")

    def nineClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()+"9")

    def zeroClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()+"0")

    def plusClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text() + "+")

    def minusClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text() + "-")

    def asteriskClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()+"*")

    def slashClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()+"/")

    def percentClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()+"%")

    def equalClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        try:
            self.result.setText(str(eval(self.result.text())))
        except(SyntaxError, ZeroDivisionError):
            self.error = True
            self.result.setText("Error")

    def deleteClicked(self):
        if self.error:
            self.result.setText("")
            self.error = False

        self.result.setText(self.result.text()[:-1])


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    window: Ui_MainWindow = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())
