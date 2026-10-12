import re
import sys
from database import db
from PySide6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QPushButton,
                               QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget, QLabel, QLayout)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class StoreAppSignup (QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle('Store App')
        self.setFixedSize(1200, 700)
        self.setup_layout()
        self.setup_form_layout()
        self.setup_image_layout()
        self.create_widgets()
        self.style_widgets()

    def setup_layout (self):
        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    def setup_form_layout (self):
        self.form_widget = QWidget()
        self.form_layout = QVBoxLayout()
        self.form_widget.setLayout(self.form_layout)
        self.main_layout.addWidget(self.form_widget, 3)

        self.title_box = QGridLayout()
        self.form_widget.setLayout(self.title_box)

        self.form_box_widget = QWidget()
        self.form_box_layout = QHBoxLayout()
        self.form_box_widget.setLayout(self.form_box_layout)

        self.left_form_box = QVBoxLayout()
        self.form_box_layout.addLayout(self.left_form_box)
        self.right_form_box = QVBoxLayout()
        self.form_box_layout.addLayout(self.right_form_box)
        self.form_widget.setLayout(self.form_box_layout)

        self.footer_box = QVBoxLayout()
        self.form_widget.setLayout(self.footer_box)

    def setup_image_layout (self):
        self.image_widget = QWidget()
        self.image_layout = QHBoxLayout()
        self.image_widget.setLayout(self.image_layout)
        self.main_layout.addWidget(self.image_widget, 1.5)

    def create_widgets (self):
        self.form_title = QLabel("Create Account")
        title_font = QFont("Segoe UI", 24)
        title_font.setBold(True)
        self.form_title.setFont(title_font)
        self.title_box.addWidget(self.form_title)

        self.first_name_line_edit = QLineEdit()
        self.first_name_line_edit.setFixedSize(400,40)
        self.left_form_box.addWidget(self.first_name_line_edit)

    def style_widgets (self):
        self.form_widget.setStyleSheet("""
                                      QWidget {
                                        background-color: #FFFFFF;
                                        border-radius: 18px;
                                        box-shadow: 1px, 1px, 5px gray;
                                      }
                                       """)

        self.form_title.setStyleSheet("""
                                      color: #000;
                                      """)

        self.first_name_line_edit.setStyleSheet("""
                                                background-color: #000;
                                                """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StoreAppSignup()
    window.show()
    sys.exit(app.exec())