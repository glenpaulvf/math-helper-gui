import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design import Ui_MathHelperWindow


class MathHelper(QMainWindow, Ui_MathHelperWindow):
    
    def __init__(self):
        super(MathHelper, self).__init__()
        self.setupUi(self)
        self.__exec()
        
    def __exec(self):
        self.inputBox.returnPressed.connect(self.output)
    
    def output(self):
        input = self.inputBox.text()
        self.outputLabel.setText(input)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mh = MathHelper()
    mh.show()
    app.exec_()
