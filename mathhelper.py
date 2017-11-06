import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design import Ui_MathHelperWindow


class MathHelper(QMainWindow, Ui_MathHelperWindow):
    
    def __init__(self):
        super(MathHelper, self).__init__()
        self.setupUi(self)
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mh = MathHelper()
    mh.show()
    app.exec_()
