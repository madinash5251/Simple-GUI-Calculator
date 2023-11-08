# main.py
import sys
from PyQt5.QtWidgets import QApplication
from app.functions import CalculatorApp  # Remove the unnecessary import

def main():
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
