import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import time

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.background_style = (
            "background-color: #282a36;"
        )
        self.label_style = (
            "font-family: Arial;"
            "padding: 5px;"
            "margin: 5px;"
            "font-size: 60px;"
            "font-weight: bold;"
            "text-align: middle;"
            "color: #50fa7b;"
        )
        self.btn_style = (
            "background-color: #44475a;"
            "border-radius: 15px;"
            "color: #f8f8f2;"
            "padding: 15px;"
            "margin: 10px;"
            "font-family: Arial;"
            "font-size: 40px;"
            "font-weight: bold;"
        )
        self.progress_style = """
QProgressBar{
    border: 2px solid #f8f8f2;
    border-radius: 5px;
    text-align: center;
    color: #ffb86c;
}

QProgressBar::chunk {
    background-color: #8be9fd;
    width: 10px;
    margin: 1px;
}
"""


        self.initUI()
        self.frontUI()


    def initUI(self):
        self.setWindowTitle("FACE LOCKER")
        self.move(300, 200)
        self.resize(400, 600)

        self.setStyleSheet(self.background_style)
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

    ## UI

    def frontUI(self):
        ## make component
        self.frontlabel1 = QLabel('FACE', self)
        self.frontlabel1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frontlabel2 = QLabel('LOCKER', self)
        self.frontlabel2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.frontbtn1 = QPushButton('&UNLOCK', self)
        self.frontbtn1.setChecked(True)
        self.frontbtn1.toggle()
        self.frontbtn2 = QPushButton('&USER', self)
        self.frontbtn2.setChecked(True)
        self.frontbtn2.toggle()
        self.frontbtn3 = QPushButton('&ABOUT', self)
        self.frontbtn3.setChecked(True)
        self.frontbtn3.toggle()

        ## set style
        self.frontlabel1.setStyleSheet(self.label_style)
        self.frontlabel2.setStyleSheet(self.label_style)

        self.frontbtn1.setStyleSheet(self.btn_style)
        self.frontbtn2.setStyleSheet(self.btn_style)
        self.frontbtn3.setStyleSheet(self.btn_style)

        ## layout
        self.frontvbox = QVBoxLayout()
        self.frontvbox.addStretch(2)
        self.frontvbox.addWidget(self.frontlabel1)
        self.frontvbox.addWidget(self.frontlabel2)
        self.frontvbox.addStretch(3)
        self.frontvbox.addWidget(self.frontbtn1)
        self.frontvbox.addWidget(self.frontbtn2)
        self.frontvbox.addWidget(self.frontbtn3)
        self.frontvbox.addStretch(3)

        self.vbox.addLayout(self.frontvbox)

        # event
        self.front_event()

    def unlockUI(self):
        ## make component
        self.unlockprogress1 = QProgressBar(self)
        self.unlockprogress1.setTextVisible(False)
        self.unlockprogress1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.unlockbtn1 = QPushButton('&SCAN', self)
        self.unlockbtn1.setChecked(True)
        self.unlockbtn1.toggle()

        ## set style
        self.unlockprogress1.setStyleSheet(self.progress_style)
        self.unlockbtn1.setStyleSheet(self.btn_style)

        ## layout
        self.unlockvbox = QVBoxLayout()
        self.unlockvbox.addStretch(5)
        self.unlockvbox.addWidget(self.unlockprogress1)
        self.unlockvbox.addStretch(1)
        self.unlockvbox.addWidget(self.unlockbtn1)
        self.unlockvbox.addStretch(1)

        self.vbox.addLayout(self.unlockvbox)

        ## event
        self.unlock_event()


    def userUI(self):
        ## make component
        self.userbtn1 = QPushButton('&ADD USER', self)
        self.userbtn1.setChecked(True)
        self.userbtn1.toggle()
        self.userbtn2 = QPushButton('&REMOVE USER', self)
        self.userbtn2.setChecked(True)
        self.userbtn2.toggle()

        ## set style
        self.userbtn1.setStyleSheet(self.btn_style)
        self.userbtn2.setStyleSheet(self.btn_style)

        ## layout
        self.uservbox = QVBoxLayout()
        self.uservbox.addStretch(4)
        self.uservbox.addWidget(self.userbtn1)
        self.uservbox.addStretch(1)
        self.uservbox.addWidget(self.userbtn2)
        self.uservbox.addStretch(4)


        self.vbox.addLayout(self.uservbox)

        ## event
        self.user_event()

    def addUI(self):
        ## make component
        self.addprogress1 = QProgressBar(self)
        self.addprogress1.setTextVisible(False)
        self.addprogress1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.addbtn1 = QPushButton('&SCAN', self)
        self.addbtn1.setChecked(True)
        self.addbtn1.toggle()

        ## set style
        self.addprogress1.setStyleSheet(self.progress_style)
        self.addbtn1.setStyleSheet(self.btn_style)


        ## layout
        self.addvbox = QVBoxLayout()
        self.addvbox.addStretch(5)
        self.addvbox.addWidget(self.addprogress1)
        self.addvbox.addStretch(1)
        self.addvbox.addWidget(self.addbtn1)
        self.addvbox.addStretch(1)

        self.vbox.addLayout(self.addvbox)

        ## event
        self.add_event()


    def aboutUI(self):
        pass


    ## event listener

    def front_event(self):
        self.frontbtn1.pressed.connect(lambda: self.front_btn_clicked(1))
        self.frontbtn2.pressed.connect(lambda: self.front_btn_clicked(2))
        self.frontbtn3.pressed.connect(lambda: self.front_btn_clicked(3))

    def unlock_event(self):
        self.unlockbtn1.pressed.connect(lambda: self.unlock_btn_clicked())


    def user_event(self):
        self.userbtn1.pressed.connect(lambda: self.user_btn_clicked(1))
        self.userbtn2.pressed.connect(lambda: self.user_btn_clicked(2))

    def add_event(self):
        self.addbtn1.pressed.connect(lambda: self.add_btn_clicked())



    ## delete UI

    def delete_frontUI(self):
        self.frontlabel1.deleteLater()
        self.frontlabel2.deleteLater()

        self.frontbtn1.deleteLater()
        self.frontbtn2.deleteLater()
        self.frontbtn3.deleteLater()

        self.vbox.removeItem(self.frontvbox)

    def delete_userUI(self):
        self.userbtn1.deleteLater()
        self.userbtn2.deleteLater()

        self.vbox.removeItem(self.uservbox)


    ##event

    def front_btn_clicked(self, i):
        self.delete_frontUI()
        if i==1:
            self.unlockUI()
        elif i==2:
            self.userUI()
        else:
            self.aboutUI()

    def unlock_btn_clicked(self):
        self.unlockprogress1.setValue(30)
        # opencv unlock



    def user_btn_clicked(self, i):
        self.delete_userUI()
        if i==1:
            self.addUI()
        else:
            pass

    def add_btn_clicked(self):
        self.addprogress1.setValue(80)
        # opencv add user



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())