from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisUI(object):
    cpath =""
    def setupUi(self, JarvisUI):
        JarvisUI.setObjectName("JarvisUI")
        JarvisUI.resize(1819, 926)
        self.centralwidget = QtWidgets.QWidget(JarvisUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-80, -50, 1999, 1000))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(162, 0, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\bg2.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1340, 860, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 136, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1220, 860, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1200, 50, 181, 51))
        self.textBrowser.setStyleSheet("background:transparent;\n"
        "border-radius:skyblue;\n"
        "color : white;\n"
        "font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1400, 50, 181, 51))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
        "border-radius:skyblue;\n"
        "color : white;\n"
        "font-size:20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-80, 144, 1999, 612))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\gif.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 30, 710, 70))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\lines1.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1160, 10, 191, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\frame10.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1350, 10, 191, 91))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(rf"{self.cpath}\UI\frame10.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1210, 20, 91, 31))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("color: rgb(93, 234, 255);\n"
        "font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1390, 20, 91, 31))
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setStyleSheet("color: rgb(93, 234, 255);\n"
        "font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.textBrowser.raise_()
        self.label_7.raise_()
        self.textBrowser_2.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        JarvisUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(JarvisUI)
        QtCore.QMetaObject.connectSlotsByName(JarvisUI)

    def retranslateUi(self, JarvisUI):
        _translate = QtCore.QCoreApplication.translate
        JarvisUI.setWindowTitle(_translate("JarvisUI", "MainWindow"))
        self.pushButton_3.setText(_translate("JarvisUI", "EXIT"))
        self.pushButton_4.setText(_translate("JarvisUI", "RUN"))
        self.label_8.setText(_translate("JarvisUI", "    DATE"))
        self.label_9.setText(_translate("JarvisUI", "      TIME"))
        
    
    def __init__(self, path):
        self.cpath = path


if __name__ == "__main__":
    import sys
    import os
    
    current_path = os.getcwd()
    app = QtWidgets.QApplication(sys.argv)
    JarvisUI = QtWidgets.QMainWindow()
    ui = Ui_JarvisUI(path=current_path)
    ui.setupUi(JarvisUI)
    JarvisUI.show()
    sys.exit(app.exec_())
