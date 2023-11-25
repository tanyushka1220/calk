from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QButtonGroup, QLabel

from calku import Ui_MainWindow

class Widget(QMainWindow):
    def init(self):
        super().init()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.num1 = ""
        self.num2 = ""
        self.op = ""
        all_btn = self.ui.centralwidget.findChildren(QWidget)
        self.group = QButtonGroup()
        for btn in all_btn:
            if type(btn) != QLabel:
                self. group.addButton(btn)
        self.group.buttonClicked.connect(self.work)
    def work(self,btn):
        if btn.text()=="=":
            if self.operation=="-":
                res = int(self.num1) - int(self.num2)
                txt = self.ui.lbl_win.text()
                self.ui.lbl_win.setText(txt+" = "+str(res))
            elif self.operation=="+":   
                res = int(self.num1) + int(self.num2)
                txt = self.ui.lbl_win.text()
                self.ui.lbl_win.setText(txt+" = "+str(res))
            elif self.operation=="*":
                res = int(self.num1) * int(self.num2)
                txt = self.ui.lbl_win.text()
                self.ui.lbl_win.setText(txt+" = "+str(res))
            elif self.operation=="/":
                if (self.num2) != 0:
                    res = int(self.num1) / int(self.num2)
                    txt = self.ui.lbl_win.text()
                    self.ui.lbl_win.setText(txt+" = "+str(res))
                else:
                     self.ui.lbl_win.setText("ERORR")
            self.num1 = str(res)
            self.num2 = ""
            self.operation = ""
        elif btn.text() in ["-", "+", "*", "/"]:
            self.operation = btn.text()
            txt = self.ui.lbl_win.text()
            self.ui.lbl_win.setText(txt+" "+self.operation+" ")
        elif btn.text() == "CE":
            self.num1 = ""
            self.num2 = ""
            self.operation = ""
            self.ui.lbl_win.setText("0")
        else:
            if self.ui.lbl_win.text() == "0":
                txt = ""
            else:
                txt = self.ui.lbl_win.text()
                num = btn.text()
            if  self.operation == "":
                self.num1 + num
            else:
                self.num2 + num
            
            txt += num
            self.ui.lbl_win.setText(txt)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()