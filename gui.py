import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit,  QFileDialog, QVBoxLayout , QGroupBox, QDialog , QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from summer import summer, dirty_summer
from notepad import MainWindow
import listen as ls

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

        self.getMethod()
        if self.method == 'Filename':
            self.openFileNameDialog()
            #self.getName()
            self.getRatio()
            self.saveFileDialog()

            self.show()

            summer(self.name,self.ratio,self.saveName)

        elif self.method == 'TextInput':
            self.getText()
            self.getRatio()
            self.saveFileDialog()

            self.show()

            dirty_summer(self.text,self.ratio,self.saveName )

        else:
            self.getAudioMethod()
            if self.aMethod == "By Filename":

                self.openFileNameDialog()
                self.saveFileDialog()
                ls.file(self.name,self.saveName)
            else:
                print('MAke the other part work first')

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Copy You Text","Paste your aticle here: ", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.text = text


    def getAudioMethod(self):
        aMethods = ('By Filename','Live Record')
        aMethod, okPressed = QInputDialog.getItem(self, "Audio Method", "Choose the type of input:", aMethods , 0 , False)
        if okPressed:
            self.aMethod = aMethod


    def getRatio(self):
        ratio, okPressed = QInputDialog.getItem(self, "Get Ratio","Ratio :", self.ratioItems, 0, False)
        if ratio:
            self.ratio = float(ratio)

    def getMethod(self):
        methods = ("Filename","TextInput","Audio Input")
        method, okPressed = QInputDialog.getItem(self, "Get input method","Input Method: ", methods, 0, False)
        if okPressed:
            self.method = method


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            self.name = fileName

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        saveName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if saveName:
            self.saveName = saveName

    def startTextEditor(self):
        app = QApplication(sys.argv)
        app.setApplicationName("Edit your file before inputting...")

        window = MainWindow()
        print('exec done')
        app.exec_()
        print('exec done2')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    print('1st')
    ex = App()
    print('2nd')
    #sys.exit(app.exec_())
    #print('3rd')
