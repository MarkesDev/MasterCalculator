from UI.MainUI import MainUI
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
win = MainUI()
win.show()
sys.exit(app.exec_())