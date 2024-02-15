import sys
import hashlib
import platform
import psutil
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QClipboard
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
     
        # Connect Auto_Load_ID to the initialization of the MainWindow
        self.Auto_Load_ID()

        # Handle Button's
        self.ui.Copy_id_Btn.clicked.connect(self.Copy_HID_lineEdit)
        #self.ui.Name_Paste_Btn.clicked.connect(self.Paste_Name_Btn)
        #self.ui.Key_Paste_Btn.clicked.connect(self.Paste_Key_Btn)
        self.ui.Generate_Btn.clicked.connect(self.Generate_Key)
        self.ui.Close_Btn.clicked.connect(self.close)

    # Auto Load Hardware ID In HID_lineEdit Function's
    def Auto_Load_ID(self):
        # Call generate_unique_id and set the result in HID_lineEdit
        unique_id = self.generate_unique_id()
        self.ui.HID_lineEdit.setText(unique_id)

    def generate_unique_id(self):
        # Get hardware information
        hardware_info = self.get_hardware_info()

        # Hash the hardware information to create a unique identifier
        unique_id = hashlib.sha1(hardware_info.encode()).hexdigest().upper()

        # Format the hash into a readable pattern
        formatted_id = '-'.join([unique_id[i:i+5] for i in range(0, len(unique_id), 5)])

        return formatted_id

    def get_cpu_info(self):
        # Get processor information using the platform module
        cpu_info = platform.processor()
        return f"CPU: {cpu_info}"

    def get_mac_address(self):
        # Find the first available network interface and get its MAC address
        for interface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    # Convert each character to its ASCII value and then to an integer
                    mac_integers = [int(ord(char)) for char in addr.address]
                    # Use the converted integers with hex
                    return ":".join(hex(i)[2:].zfill(2) for i in mac_integers)

        # Return a default value if no suitable network interface is found
        return "00:00:00:00:00:00"

    def get_hardware_info(self):
        # Gather hardware information (you can customize this based on your requirements)
        cpu_info = self.get_cpu_info()
        mac_address = self.get_mac_address()
        disk_serial = subprocess.run(['wmic', 'diskdrive', 'get', 'serialnumber'], capture_output=True, text=True)
        # Extract the stdout attribute
        output = disk_serial.stdout.strip()

        # Combine hardware information into a string
        hardware_info_str = f"{cpu_info}{mac_address}{output}"

        return hardware_info_str
    
    # Combine hardware information into a lineEdit & Copy Text To Clipboard
    def Copy_HID_lineEdit(self):
        text_to_copy = self.ui.HID_lineEdit.text()

        # Copy Text To Clipboard
        clipboard = QClipboard()
        clipboard.setText(text_to_copy)

        # You can perform additional actions with the copied text if needed
        print(f"Copying text: {text_to_copy}")


    # Generate Key From Unique ID & User Name
    def Generate_Key(self):
        # Get the user-entered name from the Name_lineEdit field
        user_name = self.ui.Name_lineEdit.text().strip()

        # Ensure that the user has entered a name
        if not user_name:
            QMessageBox.warning(self, "Warning", "Please enter a name.")
            return

        # Get hardware information
        hardware_info = self.get_hardware_info()

        # Concatenate hardware information and user name
        key_data = f"{hardware_info}{user_name}"

        # Hash the combined data using sha256
        unique_key = hashlib.sha512(key_data.encode()).hexdigest()

        # Set the generated key in the Key_textEdit field
        self.ui.Key_textEdit.setPlainText(unique_key)        

        # Display the generated key in a message box
        QMessageBox.information(self, "Generated Key", f"Generated Key: {unique_key}")

        # Print the final unique key result to the console
        print(f"Final Unique Key: {unique_key}")

    # Close Window Function's



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
