from PyQt5 import QtWidgets


class StandardUI:
    def __init__(self):
        """
        Initialize Class and Components
        """
        super(StandardUI, self).__init__()
        self.boxLayout = QtWidgets.QVBoxLayout()

    def request_layout(self):
        """
        :return: Layout
        """
        return self.boxLayout
