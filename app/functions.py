# app/functions.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from app.db import save_operation

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        layout.addWidget(self.display)

        buttons = [
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', '*',
            'C', '0', '=', '/'
        ]

        grid = []
        for i in range(4):
            row = []
            for j in range(4):
                button = QPushButton(buttons[i * 4 + j])
                button.clicked.connect(self.on_button_click)
                row.append(button)
            grid.append(row)

        for row in grid:
            h_layout = QHBoxLayout()
            for button in row:
                h_layout.addWidget(button)
            layout.addLayout(h_layout)

        self.setLayout(layout)
        self.current_input = ''

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == '=':
            try:
                result = eval(self.current_input)
                self.display.setText(str(result))
                self.store_calculation(self.current_input, result)
                self.current_input = str(result)  # Clear current input
            except Exception as e:
                self.display.setText('Error')
        elif text == 'C':
            self.current_input = ''
            self.display.clear()
        else:
            self.current_input += text
            self.display.setText(self.current_input)

    def store_calculation(self, expression, result):
        calculation = f"{expression} = {result}\n"
        with open('calculations.txt', 'a') as file:
            file.write(calculation)
