import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from kiwoom import Kiwoom

form_class = uic.loadUiType("system_trading.ui")[0]

class Login_Machine(QDialog,QWidget,form_class):
    def __init__(self,*args,**kwargs):
        print("Login Machine 실행합니다.")
        super(Login_Machine, self).__init__(*args, **kwargs)
        form_class.__init__(self)
        self.setUI()


        self.k = Kiwoom()

    def setUI(self):
        self.setupUI(self)

if __name__=='__main__':

    app = QApplication(sys.argv)
    CH = Login_Machine()
    CH.show()
    app.exec_()

