import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from summer import summer

class App(QWidget):

    ratioItems = [str(ratio / 100) for ratio in range(1,101)]

    def __init__(self):
        super().__init__()
        self.title = 'TL;DL'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.getName()
        self.getRatio()
        self.show()

        summer(self.name,self.ratio)

    def getName(self):
        name, okPressed = QInputDialog.getText(self, "File Name","FileName + extension: ", QLineEdit.Normal, "")
        if okPressed and name != '':
            self.name = name

    def getRatio(self):
        ratio, okPressed = QInputDialog.getItem(self, "Get Ratio","Ratio :", self.ratioItems, 0, False)
        if ratio:
            self.ratio = float(ratio)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    print('1st')
    ex = App()
    print('2nd')
    #sys.exit(app.exec_())
    #print('3rd')
