import re
import sys
from database import db
from PySide6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QPushButton,
                               QLineEdit, QHBoxLayout, QGridLayout, QWidget, QLabel, QLayout)
from PySide6.QtCore import Qt

class StoreAppSignup (QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle('Store App')
        self.setFixedSize(1200, 700)
        self.setup_layout()
        self.setup_form_layout()
        self.setup_image_layout()
        self.create_widgets()
        self.locate_widgets()

    def setup_layout (self):
        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)

    def setup_form_layout (self):
        self.form_widget = QWidget()
        self.form_layout = QGridLayout()
        self.form_widget.setLayout(self.form_layout)
        self.main_layout.addWidget(self.form_widget, 3)

    def setup_image_layout (self):
        self.image_widget = QWidget()
        self.image_layout = QHBoxLayout()
        self.image_widget.setLayout(self.image_layout)
        self.main_layout.addWidget(self.image_widget, 2)

    def create_widgets (self):
        pass

    def locate_widgets (self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StoreAppSignup()
    window.show()
    sys.exit(app.exec())