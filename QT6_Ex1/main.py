from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QCheckBox, QLabel,
    QVBoxLayout, QWidget, QLineEdit, QComboBox
)

# Only needed for access to command line arguments
import sys

# Pyserial
import serial


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self, count):
        super().__init__()

        # Variables
        self.count = count

        self.setWindowTitle("Student Management System")
        self.setFixedSize(QSize(800, 600))  # .setFixedSize() .setMinimumSize() and .setMaximumSize()

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
        self.label_com_port = QLabel("COM Port")
        self.label_com_speed = QLabel("Speed (baud)")
        self.label_com_data = QLabel("Data bits")
        self.label_com_stop = QLabel("Stop bits")
        self.label_com_parity = QLabel("Parity")
        self.label_com_flow = QLabel("Flow control")

        # Text
        self.text = QLineEdit("-----")

        # ComboBox Parity
        self.combobox_parity = QComboBox()
        self.combobox_parity.addItems(["None", "Odd", "Even", "Mark", "Space"])
        # Flag to make the combobox editable
        # self.combobox_parity.setEditable(True)
        # Flag to determine how the insert is handled Sends the current index (position) of the selected item
        # self.combobox_parity.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        # To limit the number of items allowed in the box
        # self.combobox_parity.setMaxCount(10)
        self.combobox_parity.currentIndexChanged.connect(self.parity_index_changed)
        # There is an alternate signal to send the text.
        self.combobox_parity.currentTextChanged.connect(self.parity_text_changed)

        # ComboBox Flow control
        self.combobox_flow = QComboBox()
        self.combobox_flow.addItems(["None", "XON/XOFF", "RTS/CTS", "DSR/DTR"])
        # Sends the current index (position) of the selected item.
        self.combobox_flow.currentIndexChanged.connect(self.parity_index_changed)
        # There is an alternate signal to send the text.
        self.combobox_flow.currentTextChanged.connect(self.parity_text_changed)

        # Layout button
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.button2)

        # Layout label
        layout.addWidget(self.label_com_port)
        layout.addWidget(self.label_com_speed)
        layout.addWidget(self.label_com_data)
        layout.addWidget(self.label_com_stop)
        layout.addWidget(self.label_com_parity)
        layout.addWidget(self.label_com_flow)

        # Layout combobox
        layout.addWidget(self.combobox_parity)
        layout.addWidget(self.combobox_flow)

        # Layout text
        layout.addWidget(self.text)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        self.count += 1
        print("Clicked!")
        # self.label.setText("Pressed " + str(self.count) + " times")
        # self.text.setText(self.text.displayText() + " *** " + self.label.text())

    def parity_index_changed(self, i):  # i is an int
        print(i)

    def parity_text_changed(self, s):  # s is a str
        print(s)


app = QApplication(sys.argv)

window = MainWindow(10)
window.show()

app.exec()
