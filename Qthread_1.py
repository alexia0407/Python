from PyQt5.QtCore import *
from kiwoom import Kiwoom
from PyQt5.QtWidgets import *

class Thread1(QThread):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        # =====================키움 서버 함수를 사용하기 위해서 kiwoom의 능력을 상속받는다.===========
        self.k = Kiwoom()
        # =====================사용되는 변수=======================
        self.Acc_Screen = '1000'



        # ==================슬롯==========================
        self.k.kiwoom.OnReceiveTrData.connect(self.trdata_slot)
        # =================EventLoop=====================
        self.detail_account_info_event_loop = QEventLoop()
        # =================계좌정보 가져오기================
        self.getItemList()
        self.detail_account_mystock()

    def getItemList(self):
        marketList = ["0", "10"]
        for market in marketList:
            codeList = self.k.kiwoom.dynamicCall("GetCodeListByMarket(Qstring)", market).split(";")[:-1]

            for code in codeList:
                name = self.k.kiwoom.dynamicCall("GetMasterCodeName(Qstring)", code)
                self.k.All_Stock_Code.update({code: {"종목명":name}})

    def detail_account_mystock(self, sPrevNext="0"):
        print("계좌평가잔고내역 조회")
        account = self.parent.accComboBox.currentText()
        self.account_num = account
        print("최종 선택 계좌는 %s" % self.account_num)

        self.k.kiwoom.dynamicCall("SetInputValue(String, String)", "계좌번호", account)
        self.k.kiwoom.dynamicCall("SetInputValue(String, String)", "비밀번호", "0000")
        self.k.kiwoom.dynamicCall("SetInputValue(String, String)", "비밀번호입력매체구분", "00")
        self.k.kiwoom.dynamicCall("SetInputValue(String, String)", "조회구분", "2")
        self.k.kiwoom.dynamicCall("CommRqData(String, String, int, String)", "계좌평가잔고내역요청", "opw00018", sPrevNext,self.Acc_Screen)
        self.detail_account_info_event_loop.exec_()