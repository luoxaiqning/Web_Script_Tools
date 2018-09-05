from PyQt4.QtGui import QApplication
from PyQt4.QtCore import *
from PyQt4.QMainWindow import *

class Main_Ui(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_ui = Main_Ui()
    main_ui.show()
    app.exec_()