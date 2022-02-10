"""GUI interface for TL;DL"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QGroupBox,
    QHBoxLayout,
    QInputDialog,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

import listen as ls
from notepad import MainWindow
from summer import dirty_summer, summer

RATIOS = (str(ratio / 100) for ratio in range(1, 101, 10))
FILE_INPUT_METHODS = ("Filename", "TextInput", "Audio Input")
AUDIO_INPUT_METHODS = ('By Filename', 'Live Record')


class App(QWidget):
    """Main widget"""

    def __init__(self):
        super().__init__()
        self.title = 'TL;DL'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.init_ui()

    def init_ui(self):
        """Initialize UI"""
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.get_method()
        if self.method == 'Filename':
            self.open_file_name_dialog()
            # self.getName()
            self.get_ratio()
            self.save_file_dialog()

            self.show()

            summer(self.name, self.ratio, self.save_name)

        elif self.method == 'TextInput':
            self.get_text()
            self.get_ratio()
            self.save_file_dialog()

            self.show()

            dirty_summer(self.text, self.ratio, self.save_name)

        else:
            self.get_audio_method()
            if self.audio_method == "By Filename":

                self.open_file_name_dialog()
                self.save_file_dialog()
                ls.file(self.name, self.save_name)
            else:
                print('Make the other part work first')

    def get_text(self):
        """Open dialogue for user input"""
        text, is_pressed = QInputDialog.get_text(
            self, "Copy You Text", "Paste your aticle here: ", QLineEdit.Normal, ""
        )
        if is_pressed and text != '':
            self.text = text

    def get_audio_method(self):
        """Retrieve user audio method"""
        audio_method, is_pressed = QInputDialog.getItem(
            self,
            "Audio Method",
            "Choose the type of input:",
            AUDIO_INPUT_METHODS,
            0,
            False,
        )
        if is_pressed:
            self.audio_method = audio_method

    def get_ratio(self):
        """Get desired summarization ratio"""
        ratio, is_pressed = QInputDialog.getItem(
            self, "Get Ratio", "Ratio :", self.RATIOS, 0, False
        )
        if ratio:
            self.ratio = float(ratio)

    def get_method(self):
        """Get user input method"""
        method, is_pressed = QInputDialog.getItem(
            self, "Get input method", "Input Method: ", FILE_INPUT_METHODS, 0, False
        )
        if is_pressed:
            self.method = method

    def open_file_name_dialog(self):
        """Self explanatory"""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Text Files (*.txt)",
            options=options,
        )
        if file_name:
            self.name = file_name

    def save_file_dialog(self):
        """Get file info"""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        save_name, _ = QFileDialog.getSaveFileName(
            self,
            "QFileDialog.getSaveFileName()",
            "",
            "All Files (*);;Text Files (*.txt)",
            options=options,
        )
        if save_name:
            self.save_name = save_name

    def start_text_editor(self):
        """Open edit widget"""
        app = QApplication(sys.argv)
        app.setApplicationName("Edit your file before inputting...")

        window = MainWindow()
        print('exec done')
        app.exec_()
        print('exec done2')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    # sys.exit(app.exec_())
