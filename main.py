import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
# ==========부가 기능 수행 (일꾼) =========
from kiwoom import Kiwoom
from Qthread_1 import Thread1
# ==========프로그램 실행 ===============
form_class = uic.loadUiType("system_trading.ui")[0]

class Login_Machine(QDialog,QWidget,form_class):
    def __init__(self,*args,**kwargs):
        print("Login Machine 실행합니다.")
        super(Login_Machine, self).__init__(*args, **kwargs)
        form_class.__init__(self)
        self.setUI()
        # =========초기 셋팅 : 계좌평가잔고내역 ===========
        self.label_11.setText(str("총매입금액"))
        self.label_12.setText(str("총평가금액"))
        self.label_13.setText(str("추정예탁자산"))
        self.label_14.setText(str("총평가손익금액"))
        self.label_15.setText(str("총수익률(%)"))

        # ==========기타함수==========
        self.login_event_loop = QEventLoop()

        # ==========키움증권 로그인========
        self.k = Kiwoom()
        self.set_signal_slot()
        self.signal_login_commConnect()
    # ==============이벤트 생성 및 진행 =======
        self.call_account.clicked.connect(self.c_acc)
    def setUI(self):
        self.setupUI(self)

    def set_signal_slot(self):
        self.k.kiwoom.dynamicCall("CommConnect()")
        self.login_event_loop.exec_()

    def login_slot(self, errCode):
        if errCode == 0:
            print("로그인 성공")
            self.statusBar().showMessage('로그인 성공')
            self.get_account_info()

        elif errCode == 100:
            print("사용자 정보교환 실패")
        elif errCode == 101:
            print("서버접속 실패")
        elif errCode == 102:
            print("버전처리 실패")
        self.login_event_loop.exit()

    def get_account_info(self):
        account_list = self.k.kiwoom.dynamicCall("GetLoginInfo(String)", "ACCNO")

        for n in account_list.split(';'):
            self.accComboBox.addItem(n)
    def c_acc(self):
        print("선택 계좌 정보 가져오기")
#        =========1번 일꾼 실행===========
        Thread1(self).start()
if __name__=='__main__':

    app = QApplication(sys.argv)
    CH = Login_Machine()
    CH.show()
    app.exec_()