import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import img_processing.find_face
import database.db
import time

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # db class
        self.ddbb = database.db.Db()
        self.pdb = database.db.Passdb()

        self.vbox_status = None

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
        self.small_label_style = (
            "font-family: Arial;"
            "padding: 5px;"
            "margin: 5px;"
            "font-size: 15px;"
            "font-weight: bold;"
            "text-align: middle;"
            "color: #ffb86c;"
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
        self.table_style = (
            "background-color: #f8f8f2;"
            "color: #44475a;"
            "font-family: Arial;"
            "font-size: 20px;"
            "font-weight: bold;"
        )

        self.home_button_style = (
            "background-color: #ff79c6;"
            "border-radius: 15px;"
            "color: #f8f8f2;"
            "padding: 11px;"
            "margin: 10px;"
            "font-family: Arial;"
            "font-size: 20px;"
            "font-weight: bold;"
        )

        self.initUI()
        self.home_button_UI()
        self.frontUI()


    def initUI(self):
        self.setWindowTitle("FACE LOCKER")
        self.move(300, 200)
        self.resize(400, 600)

        self.setStyleSheet(self.background_style)
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)


    def home_button_UI(self):
        ## make component
        self.home_btn1 = QPushButton('&HOME', self)
        self.home_btn1.setChecked(True)
        self.home_btn1.toggle()

        ## set style
        self.home_btn1.setStyleSheet(self.home_button_style)
        self.home_btn1.setFixedWidth(100)

        ## layout
        self.home_btn_vbox = QVBoxLayout()
        self.home_btn_vbox.addWidget(self.home_btn1)

        ## event
        self.home_button_event()


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

        self.vbox.addLayout(self.home_btn_vbox)
        self.vbox.addStretch(10)
        self.vbox.addLayout(self.frontvbox)
        self.vbox.addStretch(10)

        self.vbox_status = self.frontvbox

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

        self.vbox.addLayout(self.home_btn_vbox)
        self.vbox.addStretch(10)
        self.vbox.addLayout(self.unlockvbox)
        self.vbox.addStretch(10)

        self.vbox_status = self.unlockvbox

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

        self.vbox.addLayout(self.home_btn_vbox)
        self.vbox.addStretch(10)
        self.vbox.addLayout(self.uservbox)
        self.vbox.addStretch(10)

        self.vbox_status = self.uservbox

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

        self.vbox.addLayout(self.home_btn_vbox)
        self.vbox.addStretch(10)
        self.vbox.addLayout(self.addvbox)
        self.vbox.addStretch(10)

        self.vbox_status = self.addvbox

        ## event
        self.add_event()


    def removeuserUI(self):
        ## make component
        self.removeuserprogress1 = QProgressBar(self)
        self.removeuserprogress1.setTextVisible(False)
        self.removeuserprogress1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.removeuserbtn1 = QPushButton('&SCAN', self)
        self.removeuserbtn1.setChecked(True)
        self.removeuserbtn1.toggle()

        ## set style
        self.removeuserprogress1.setStyleSheet(self.progress_style)
        self.removeuserbtn1.setStyleSheet(self.btn_style)

        ## layout
        self.removeuservbox = QVBoxLayout()
        self.removeuservbox.addStretch(5)
        self.removeuservbox.addWidget(self.removeuserprogress1)
        self.removeuservbox.addStretch(1)
        self.removeuservbox.addWidget(self.removeuserbtn1)
        self.removeuservbox.addStretch(1)

        self.vbox.addLayout(self.home_btn_vbox)
        self.vbox.addStretch(10)
        self.vbox.addLayout(self.removeuservbox)
        self.vbox.addStretch(10)

        self.vbox_status = self.removeuservbox

        ## event
        self.removeuser_event()


    def aboutUI(self):
        ## make component
        self.aboutlabel1 = QLabel("https://github.com/sungminna/FaceLocker", self)
        self.aboutlabel1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aboutlabel2 = QLabel('SUNGMIN NA', self)
        self.aboutlabel2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        ## set style
        self.aboutlabel1.setStyleSheet(self.small_label_style)
        self.aboutlabel2.setStyleSheet(self.small_label_style)

        ## layout
        self.aboutvbox = QVBoxLayout()
        self.aboutvbox.addStretch(5)
        self.aboutvbox.addWidget(self.aboutlabel1)
        self.aboutvbox.addStretch(1)
        self.aboutvbox.addWidget(self.aboutlabel2)
        self.aboutvbox.addStretch(5)

        self.vbox.addLayout(self.home_btn_vbox)
        self.vbox.addStretch(10)
        self.vbox.addLayout(self.aboutvbox)
        self.vbox.addStretch(10)

        self.vbox_status = self.aboutvbox

        ## event

    def password_UI(self, pass_df, table_name):
        # data config
        self.table_name = table_name
        self.passwordtable_row = 5
        df_rowcount = pass_df.shape[1]

        ## make component
        self.passwordtable = QTableWidget(self)
        self.passwordtable.setRowCount(self.passwordtable_row)
        self.passwordtable.setColumnCount(3)
        column_header = ['site', 'id', 'password']
        self.passwordtable.setHorizontalHeaderLabels(column_header)
        self.passwordtable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.passwordtable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.passwordbtn1 = QPushButton('&save')
        self.passwordbtn1.setChecked(True)
        self.passwordbtn1.toggle()

        ## set style
        self.passwordbtn1.setStyleSheet(self.btn_style)
        self.passwordtable.setStyleSheet(self.table_style)

        ## set data
        for i, row in pass_df.iterrows():
            for j in range(3):
                self.passwordtable.setItem(i, j, QTableWidgetItem(row[j]))

        ## layout
        self.passwordvbox = QVBoxLayout()
        self.passwordvbox.addStretch(5)
        self.passwordvbox.addWidget(self.passwordtable)
        self.passwordvbox.addStretch(1)
        self.passwordvbox.addWidget(self.passwordbtn1)
        self.passwordvbox.addStretch(1)

        self.vbox.addLayout(self.home_btn_vbox)
        self.vbox.addStretch(10)
        self.vbox.addLayout(self.passwordvbox)
        self.vbox.addStretch(10)

        self.vbox_status = self.passwordvbox

        ## event
        self.password_event()


    ## event listener

    def home_button_event(self):
        self.home_btn1.pressed.connect(lambda: self.home_btn_clicked())

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

    def removeuser_event(self):
        self.removeuserbtn1.pressed.connect(lambda: self.removeuser_btn_clicked())


    def password_event(self):
        self.passwordbtn1.pressed.connect(lambda: self.password_btn_clicked())


    ## delete UI

    def delete_UI(self, vbox):
        # delete widget in vbox that are in self.vbox
        for i in reversed(range(vbox.count())):
            if (vbox.itemAt(i).widget() != None):
                vbox.itemAt(i).widget().deleteLater()

        #delete self.vbox widget
        for i in reversed(range(self.vbox.count())):
            if (self.vbox.itemAt(i).widget() != None):
                self.vbox.itemAt(i).widget().deleteLater()

        # delete self.vbox layout
        for i in reversed(range(self.vbox.count())):
            if (self.vbox.itemAt(i).spacerItem()) != None:
                self.vbox.removeItem(self.vbox.itemAt(i).spacerItem())


    ##event

    def home_btn_clicked(self):
        #delete all component and
        print(self.vbox_status)
        self.delete_UI(self.vbox_status)

        self.frontUI()


    def front_btn_clicked(self, i):
        #self.delete_frontUI()
        self.delete_UI(self.frontvbox)
        if i==1:
            self.unlockUI()
        elif i==2:
            self.userUI()
        else:
            self.aboutUI()


    def unlock_btn_clicked(self):
        self.unlockprogress1.setValue(10)
        detect = img_processing.find_face.FaceDetection(3, self.unlockprogress1)

        table_name = self.ddbb.get_user(detect.oneface) #one face


        if table_name != 0:
            #self.delete_unlockUI()
            self.delete_UI(self.unlockvbox)
            pass_df, table_name = self.pdb.get_password(table_name)
            self.unlockprogress1.setValue(100)
            self.password_UI(pass_df, table_name)
            # show
        else:
            # no matching faces
            self.unlockprogress1.setValue(0)


        # opencv unlock

    def user_btn_clicked(self, i):
        #self.delete_userUI()
        self.delete_UI(self.uservbox)
        if i==1:
            self.addUI()
        else:
            self.removeuserUI()


    def add_btn_clicked(self):
        self.addprogress1.setValue(10)
        #detect = img_processing.find_face.FaceDetection(0, self.addprogress1)  #detect faces
        detect = img_processing.find_face.FaceDetection(3, self.addprogress1)   #detect one face

        #self.addprogress1.setValue(detect.cnt)
        table_name = self.ddbb.get_user(detect.oneface)

        if table_name == 0:
            # add user
            stime = str(int(time.time()))
            # self.ddbb.save_user_multi(stime, detect.faces)   #save faces
            self.ddbb.save_user1(stime, detect.oneface)  # one face

            self.addprogress1.setValue(100)

            self.pdb.add_user(stime)
            #self.delete_addUI()
            self.delete_UI(self.addvbox)
            table_name = "u_" + stime
            pass_df, table_name = self.pdb.get_password(table_name)
            self.password_UI(pass_df, table_name)
        else:
            # user exsists
            pass


    def removeuser_btn_clicked(self):
        self.removeuserprogress1.setValue(10)
        #detect = img_processing.find_face.FaceDetection(0, self.addprogress1)  #detect faces
        detect = img_processing.find_face.FaceDetection(3, self.removeuserprogress1)   #detect one face

        #self.addprogress1.setValue(detect.cnt)
        table_name = self.ddbb.get_user(detect.oneface)
        self.removeuserprogress1.setValue(100)


        if table_name != 0:
            # remove user
            print(table_name, "delete user")
            self.ddbb.remove_user(table_name)
            self.pdb.remove_user(table_name)

            #self.delete_addUI()
            self.delete_UI(self.removeuservbox)
        else:
            # no matching user to delete
            self.removeuserprogress1.setValue(0)


    def password_btn_clicked(self):
        # save(update) password data
        password_list = list()
        rowcount = self.passwordtable.rowCount()
        for i in range(rowcount):
            temp_list = list()
            for j in range(3):
                data = self.passwordtable.item(i, j)
                if data!= None:
                    temp_list.append(data.text())

            password_list.append(temp_list)
        self.pdb.update_password(password_list, self.table_name)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())