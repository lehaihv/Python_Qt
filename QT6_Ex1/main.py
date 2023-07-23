from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QCheckBox, QLabel, QMessageBox,
    QVBoxLayout, QWidget, QLineEdit, QComboBox, QGridLayout, QTextEdit
)
from PyQt6.QtGui import QPalette, QColor

# Only needed for access to command line arguments
import sys

# Pyserial
import serial
import time


def URAT_setup(COMPort, baud, data, stop, parity):
    global serial_obj
    serial_obj = serial.Serial(COMPort)  # COMxx  format on Windows
    # ttyUSBx format on Linux
    serial_obj.baudrate = baud  # set Baud rate to 9600
    serial_obj.bytesize = data  # Number of data bits = 8
    serial_obj.stopbits = stop  # Number of Stop bits = 1
    serial_obj.parity = parity  # No parity
    # serial_obj.xonxoff = flow  # Flow control
    time.sleep(1)


def UART_send(data):
    serial_obj.write(data.encode('utf-8'))  # transmit data (8bit)
    time.sleep(1)


def UART_receive():
    data = serial_obj.read()
    print(data)


# Class color
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self, count):
        super().__init__()

        # Variables
        self.count = count

        self.setWindowTitle("UART Transceiver Version 1.0")
        self.setFixedSize(QSize(1000, 800))  # .setFixedSize() .setMinimumSize() and .setMaximumSize()

        # Button 1
        self.button_send = QPushButton("Send")
        self.button_send.setStyleSheet("background-color: rgb(193,205,205)")
        self.button_send.setFixedSize(100, 25)
        # self.button_send.setCheckable(True)
        self.button_send.clicked.connect(self.the_button_send_was_clicked)

        # Button 2
        self.button_receive = QPushButton("Receive")
        self.button_receive.setStyleSheet("background-color: rgb(193,205,205)")
        self.button_receive.setFixedSize(100, 25)
        # self.button_receive.setCheckable(True)
        self.button_receive.clicked.connect(self.the_button_receive_was_clicked)

        # label
        self.label_com_port = QLabel("COM Port")
        self.label_com_port.setFixedSize(100, 25)
        self.label_com_speed = QLabel("Speed (baud)")
        self.label_com_speed.setFixedSize(100, 25)
        self.label_com_data = QLabel("Data bits")
        self.label_com_stop = QLabel("Stop bits")
        self.label_com_parity = QLabel("Parity")
        self.label_com_flow = QLabel("Flow control")

        # Text
        self.text_port = QLineEdit("COM3")
        self.text_port.setFixedSize(100, 25)
        self.text_send = QLineEdit()
        self.text_send.setFixedSize(500, 25)
        self.text_send.setPlaceholderText("Enter data to send")
        self.text_receive = QTextEdit()
        self.text_receive.setFixedSize(500, 200)
        self.text_receive.setPlaceholderText("Receiving data")
        self.text_receive.textChanged.connect(self.text_receive_changed)

        # ComboBox Speed (baud)
        self.combobox_speed = QComboBox()
        self.combobox_speed.addItems(["115200", "19200", "9600"])
        self.combobox_speed.setFixedSize(100, 25)
        # Sends the current index (position) of the selected item.
        self.combobox_speed.currentIndexChanged.connect(self.parity_index_changed)
        # There is an alternate signal to send the text.
        self.combobox_speed.currentTextChanged.connect(self.parity_text_changed)

        # ComboBox Data bits
        self.combobox_data = QComboBox()
        self.combobox_data.addItems(["8", "7", "6", "5"])
        self.combobox_data.setFixedSize(80, 25)
        # Sends the current index (position) of the selected item.
        self.combobox_data.currentIndexChanged.connect(self.parity_index_changed)
        # There is an alternate signal to send the text.
        self.combobox_data.currentTextChanged.connect(self.parity_text_changed)

        # ComboBox Stop bits
        self.combobox_stop = QComboBox()
        self.combobox_stop.addItems(["1", "2", "1 1/2"])
        self.combobox_stop.setFixedSize(80, 25)
        # Sends the current index (position) of the selected item.
        self.combobox_stop.currentIndexChanged.connect(self.parity_index_changed)
        # There is an alternate signal to send the text.
        self.combobox_stop.currentTextChanged.connect(self.parity_text_changed)

        # ComboBox Parity
        self.combobox_parity = QComboBox()
        self.combobox_parity.addItems(["None", "Odd", "Even", "Mark", "Space"])
        self.combobox_parity.setFixedSize(80, 25)
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
        self.combobox_flow.setFixedSize(80, 25)
        # Sends the current index (position) of the selected item.
        self.combobox_flow.currentIndexChanged.connect(self.parity_index_changed)
        # There is an alternate signal to send the text.
        self.combobox_flow.currentTextChanged.connect(self.parity_text_changed)

        # Layout style
        # layout = QVBoxLayout()
        layout = QGridLayout()

        # Layout button
        layout.addWidget(self.button_send, 6, 0)
        layout.addWidget(self.button_receive, 7, 0)

        # Layout label
        layout.addWidget(self.label_com_port, 0, 0)
        layout.addWidget(self.label_com_speed, 1, 0)
        layout.addWidget(self.label_com_data, 2, 0)
        layout.addWidget(self.label_com_stop, 3, 0)
        layout.addWidget(self.label_com_parity, 4, 0)
        layout.addWidget(self.label_com_flow, 5, 0)

        # Layout combobox
        layout.addWidget(self.combobox_speed, 1, 3)
        layout.addWidget(self.combobox_data, 2, 3)
        layout.addWidget(self.combobox_stop, 3, 3)
        layout.addWidget(self.combobox_parity, 4, 3)
        layout.addWidget(self.combobox_flow, 5, 3)

        # Layout text
        layout.addWidget(self.text_port, 0, 3)
        layout.addWidget(self.text_send, 6, 3)
        layout.addWidget(self.text_receive, 7, 3)

        # Setup UART
        # URAT_setup("COM3", 115200, 8, 1, "N")
        URAT_setup(self.text_port.displayText(), int(self.combobox_speed.currentText()),
                   int(self.combobox_data.currentText()), int(self.combobox_stop.currentText()), "N")

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def the_button_send_was_clicked(self):
        # self.count += 1
        # print("Clicked!")
        # self.label.setText("Pressed " + str(self.count) + " times")
        # self.text_send.setText(self.text_port.displayText() + " " + self.combobox_speed.currentText() +
        #                       " " + self.combobox_data.currentText() + " " + self.combobox_stop.currentText() +
        #                       " " + self.combobox_parity.currentText() + " " + self.combobox_flow.currentText())
        # serial_obj.write(b'A')
        serial_obj.write(self.text_send.displayText().encode('utf-8'))

    def the_button_receive_was_clicked(self):
        # self.count += 1
        # print("Clicked!")
        # self.label.setText("Pressed " + str(self.count) + " times")
        # self.text_receive.setText(self.combobox_speed.currentText())
        # UART_receive()
        # data = serial_obj.read(10)  # read n bytes
        data = serial_obj.readline()  # read a line until \n
        # self.text_receive.setText(str(data))
        self.text_receive.append(data.decode('utf-8'))

    def text_receive_changed(self):
        data = serial_obj.readline()  # read a line until \n
        # self.text_receive.setText(str(data))
        # self.text_receive.setText(self.text_receive.text() + data.decode('utf-8'))
        # self.text_receive.append(data.decode('utf-8'))
        print("receive changed")

    def parity_index_changed(self, i):  # i is an int
        print(i)

    def parity_text_changed(self, s):  # s is a str
        print(s)

    def closeEvent(self, e):
        print("closeEvent has been called")
        close = QMessageBox.question(self, "QUIT", "Are you sure want to quit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if close == QMessageBox.StandardButton.Yes:
            if serial_obj.is_open: serial_obj.close()
            e.accept()
        else:
            e.ignore()


app = QApplication(sys.argv)

window = MainWindow(10)
window.show()

app.exec()
