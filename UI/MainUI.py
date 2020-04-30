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
        self.setMaximumSize(550, 550)
        self.frame = QtWidgets.QFrame(self)

        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu('File')
        self.newMenu = QtWidgets.QMenu('New', self)
        self.newAct_STANDARD = QtWidgets.QAction('Standard', self)
        self.exitAct = QtWidgets.QAction('Exit', self)

        self.ui_init()

    def ui_init(self):
        """
        Initialize User-Interface
        """
        self.newMenu.addAction(self.newAct_STANDARD)
        self.fileMenu.addMenu(self.newMenu)
        self.fileMenu.addAction(self.exitAct)
        self.frame.resize(550, 550)
        self.exitAct.setShortcut('Ctrl+Q')

        self.exitAct.triggered.connect(QCoreApplication.instance().quit)
        self.newAct_STANDARD.triggered.connect(lambda: self.set_frame(StandardUI()))

    def set_frame(self, root):
        """
        Set content [from other class] into frame
        :param root: Class which gets into frame
        """
        layout = root.request_layout()
        self.frame.setLayout(layout)
