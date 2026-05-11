import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel
)

app = QApplication([])

window = QWidget()
window.setWindowTitle("My PyQT Application")
window.setGeometry(300, 300, 400, 200)

hello_msg = QLabel("<h1>My PyQT App</h1>", parent=window)
hello_msg.move(100, 50)

window.show()
sys.exit(app.exec())
