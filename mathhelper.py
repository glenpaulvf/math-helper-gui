import sys
import re
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
        
        regex_comparam = "^([A-Za-z]+)?(.*)$"
        regex_expvar = "^\((|.+),\s*(|\w+)\)$"

        derivative_keywords = ["diff", "differentiate", "derivative"]
        integral_keywords = ["int", "integrate", "integral"]
        solve_keywords = ["sol", "solve", "solution"]
        
        try:
            # Basic syntax of SymPy:
            # <command>(<expression>, <variable>)
            
            # Extract command
            com = re.sub(regex_comparam, r"\1", input)
            
            # Extract parameters (<expression>, <variable>)
            param = re.sub(regex_comparam, r"\2", input)
            
            # Extract expression
            exp = re.sub(regex_expvar, r"\1", param)
            
            # Extract variable
            var = re.sub(regex_expvar, r"\2", param)
            
            # Allow multiple keywords for SymPy derivative function diff
            for d in derivative_keywords:
                if com == d:
                    com = "diff"
                    break
            
            # Allow multiple keywords for SymPy integrate function integrate
            for i in integral_keywords:
                if com == i:
                    com = "integrate"
                    break
                
            # Allow multiple keywords for SymPy solving function solve
            for s in solve_keywords:
                if com == s:
                    com = "solve"
                    break
            
            # Concatenate input back together
            input = com + param 
            
            # Output result of SymPy input
            self.__output(str(sympify(input)))
        except:
            try:
                # Basic SymPy syntax:
                # <expression>
                
                # Extract expression
                input = re.sub(regex_comparam, r"\2", input)
                
                # Output result of SymPy input
                self.__output(self.__eval(input))
            except:
                # No valid input detected
                
                # Output error message
                error_msg = "Error: invalid input"
                self.__output(error_msg)
            
    def __output(self, result):
        self.outputLabel.setText(result)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mh = MathHelper()
    mh.show()
    app.exec_()
