from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5Singleton.PyQt5Singleton import Singleton

class Kiwoom(QWidget, metaclass=Singleton):

    def __init__(self, parent=None, **kwargs):

        print("로그인 프로그램을 실행합니다.")

        super().__init__(parent, **kwargs)

        #  ========로그인 관련 정보==================
        self.kiwoom = QAxWidget('KHOPENAPI.KHOpenAPICtrl.1')
#         =========전체 공유 데이터==================
        self.All_Stock_Code = {}
        self.acc_portfolio = {}

