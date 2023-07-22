from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox, QLabel, QVBoxLayout, QWidget, QLineEdit

# Only needed for access to command line arguments
import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self, count):
        super().__init__()

        # Variables
        self.count = count

        self.setWindowTitle("Student Management System")
        self.setFixedSize(QSize(400, 300))  # .setFixedSize() .setMinimumSize() and .setMaximumSize()

        # Button 1
        self.button = QPushButton("Press Me!")
        self.button.setFixedSize(100, 25)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)

        # Button 2
        self.button2 = QPushButton("Press 2!")
        self.button2.setFixedSize(100, 25)
        self.button2.setCheckable(True)
        self.button2.clicked.connect(self.the_button_was_clicked)

        # label
        self.label = QLabel("-----")

        # Text
        self.text = QLineEdit("-----")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.button2)
        layout.addWidget(self.label)
        layout.addWidget(self.text)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        self.count += 1
        print("Clicked!")
        self.label.setText("Pressed " + str(self.count) + " times")
        self.text.setText(self.text.displayText() + " *** " + self.label.text())


app = QApplication(sys.argv)

window = MainWindow(10)
window.show()

app.exec()
