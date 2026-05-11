import sys
from functools import partial

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QMainWindow,
    QGridLayout, QLineEdit
)

WINDOW_SIZE = 255
DISPLAY_HEIGHT = 40
DISPLAY_WIDTH = 230
BUTTON_SIZE = 40
ERROR = "ERROR"


class PyCalc(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self.generalLayout)
        self.setCentralWidget(central_widget)
        self.__create_display()
        self.__create_buttons()

    def __create_display(self):
        self.display = QLineEdit()
        self.display.setFixedSize(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def __create_buttons(self):
        buttons_layout = QGridLayout()
        key_board = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]
        self.button_map = {}

        for row, keys in enumerate(key_board):
            for column, key in enumerate(keys):
                self.button_map[key] = QPushButton(key)
                self.button_map[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttons_layout.addWidget(self.button_map[key], row, column)

        self.generalLayout.addLayout(buttons_layout)

    def set_display_text(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def get_display_text(self):
        return self.display.text()

    def clear_display_text(self):
        self.display.setText("")


def evaluate_expr(expr):
    try:
        res = str(eval(expr, {}, {}))
    except Exception:
        res = ERROR
    return res


class Controller:

    def __init__(self, model, view: PyCalc):
        self._view = view
        self._evaluate = model
        self._attach_all()

    def _calculate(self):
        res = self._evaluate(self._view.get_display_text())
        self._view.set_display_text(res)

    def _build_expr(self, sub_expr):
        if self._view.get_display_text() == ERROR:
            self._view.clear_display_text()
        expr = self._view.get_display_text() + sub_expr
        self._view.set_display_text(expr)

    def _attach_all(self):
        for key_symbol, button in self._view.button_map.items():
            if key_symbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._build_expr, key_symbol)
                )
        self._view.button_map["="].clicked.connect(self._calculate)
        self._view.display.returnPressed.connect(self._calculate)
        self._view.button_map["C"].clicked.connect(self._view.clear_display_text)


if __name__ == '__main__':
    app = QApplication([])
    view = PyCalc()
    view.show()
    controller = Controller(evaluate_expr, view)
    sys.exit(app.exec())
