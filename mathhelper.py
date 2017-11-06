import sys
from sympy import sympify
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from design import Ui_MathHelperWindow


class MathHelper(QMainWindow, Ui_MathHelperWindow):
    
    def __init__(self):
        super(MathHelper, self).__init__(flags = Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.__exec()
        
    def __exec(self):
        self.inputBox.returnPressed.connect(self.__parse_input)
    
    def __parse_input(self):
        input = self.inputBox.text()
        
        self.__output(str(sympify(input)))
    
    def __output(self, result):
        self.outputLabel.setText(result)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mh = MathHelper()
    mh.show()
    app.exec_()
