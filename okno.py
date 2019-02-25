import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)



    def run(self):
       f = open('GAME_SETTINGS.txt', 'w')
       #level
       f.write('Элементарно; Легко; Нормально; Сложно'+ '\n')
       if self.radioButton_15.isChecked():
           f.write('1' + '\n')
       elif self.radioButton_16.isChecked():
           f.write('2' + '\n')
       elif self.radioButton_17.isChecked():
           f.write('3' + '\n')
       elif self.radioButton_18.isChecked():
           f.write('4' + '\n')



app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())