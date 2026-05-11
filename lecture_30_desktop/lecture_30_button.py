import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)


def greet():
    if msg_label.text():
        msg_label.setText("")
    else:
        msg_label.setText("Hello")


app = QApplication([])

window = QWidget()
window.setWindowTitle("App with Button")
layout = QVBoxLayout()

button = QPushButton("Greet")
button.clicked.connect(greet)
layout.addWidget(button)

msg_label = QLabel("")
layout.addWidget(msg_label)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
