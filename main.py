import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from emoj import *
import get_emotion as ge

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.gen_btn.clicked.connect(self.gen_btn_clicked)

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

    def gen_btn_clicked(self):
        word_list=self.ui.textEdit1.toPlainText()
        #print(word_list)
        res = ge.get_emotion(word_list)
        print(res)
        emodzi='./emodzi/'

        sres = ['Радость']
        if (str(res).lower() == str(sres).lower()):
            emodzi += str('radost.png')

        sres=['Страх']
        if (str(res).lower() == str(sres).lower()):
            emodzi += str('strah.png')

        sres = ['Печаль']
        if (str(res).lower() == str(sres).lower()):
            emodzi += str('pechal.png')

        sres = ['Гнев']
        if (str(res).lower() == str(sres).lower()):
            emodzi += str('gnev.png')

        sres = ['Стыд']
        if (str(res).lower() == str(sres).lower()):
            emodzi += str('stid.png')

        print(emodzi)
        # <p style="font-size:18px">"""+word_list+"""</p>
        text = """
            <html>
            <body> 
            <p style="font-size:18px">"""+res[0]+' '+"""</p>  
            <img src="""+emodzi+""" width="84" height="84"/>
            </body>   
            </html>
        """
        self.ui.textBrowser1.setHtml(text)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())