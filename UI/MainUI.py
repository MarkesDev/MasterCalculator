from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QCoreApplication

from UI.ui_STANDARD import StandardUI


class MainUI(QMainWindow):
    def __init__(self):
        """
        Initialize Class, QMainWindow and Components
        """
        super(MainUI, self).__init__()
        self.setGeometry(200, 200, 550, 550)
        self.setWindowTitle("Master Calculator")
        self.setStyleSheet("background-color: #303030")
        self.setMaximumSize(550, 550)
        self.frame = QtWidgets.QFrame(self)
        self.checked_button = None

        self.menuBar = self.menuBar()
        self.menuBar.setStyleSheet("background-color: white;"
                                   "selection-background-color: #357EC7;")
        self.fileMenu = self.menuBar.addMenu('File')
        self.calcMenu = self.menuBar.addMenu('Calculator')
        self.convertMenu = self.menuBar.addMenu('Convert')
        self.settingsAct = QtWidgets.QAction('Settings', self)
        self.calc_STANDARD = QtWidgets.QAction('Standard', self, checkable=True)
        self.exitAct = QtWidgets.QAction('Exit', self)

        self.ui_init()

    def ui_init(self):
        """
        Initialize User-Interface
        """
        self.fileMenu.addAction(self.settingsAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)
        self.calcMenu.addAction(self.calc_STANDARD)
        self.frame.resize(550, 550)
        self.exitAct.setShortcut('Ctrl+Q')

        self.exitAct.triggered.connect(QCoreApplication.instance().quit)
        self.calc_STANDARD.triggered.connect(lambda: self.set_frame(StandardUI(), self.calc_STANDARD))
        self.set_frame(StandardUI(), self.calc_STANDARD)

    def set_frame(self, root, checked_button):
        """
        Set content [from other class] into frame
        :param checked_button: Button which is checked
        :param root: Class which gets into frame
        """
        if not self.checked_button is None:
            self.checked_button.setChecked(False)

        self.checked_button = checked_button
        checked_button.setChecked(True)
        layout, width, height = root.request_layout()
        self.setMaximumSize(width, height)
        self.frame.setLayout(layout)
