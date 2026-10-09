import re
import sys
from database import db
from PySide6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QPushButton,
                               QLineEdit, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QLayout)
from PySide6.QtCore import Qt

class StoreAppSignup (QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle('Store App')
        self.setFixedSize(1200, 700)
        self.setup_layout()
        self.create_widgets()
        self.locate_widgets()

    def setup_layout (self):
        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)

    def setup_form_layout (self):
        pass

    def setup_image_layout (self):
        pass

    def create_widgets (self):
        pass

    def locate_widgets (self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StoreAppSignup()
    window.show()
    sys.exit(app.exec())