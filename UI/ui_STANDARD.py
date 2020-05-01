from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QRect
from ProgrammClasses import StandardCalculator as sc


class StandardUI(QtWidgets.QWidget):
    def __init__(self):
        """
        Initialize Class and Components
        """
        super(StandardUI, self).__init__()

        # region ButtonGenerating
        self.percentage_BUTTON = QPushButton('%', self)
        self.ce_BUTTON = QPushButton('CE', self)
        self.c_BUTTON = QPushButton('C', self)
        self.back_BUTTON = QPushButton('Del', self)
        self.divided_by_x_BUTTON = QPushButton('1/x', self)
        self.pow_of_2_BUTTON = QPushButton('x^2', self)
        self.root_BUTTON = QPushButton('Root', self)
        self.divide_BUTTON = QPushButton('/', self)
        self.seven_BUTTON = QPushButton('7', self)
        self.eight_BUTTON = QPushButton('8', self)
        self.nine_BUTTON = QPushButton('9', self)
        self.multiply_BUTTON = QPushButton('*', self)
        self.four_BUTTON = QPushButton('4', self)
        self.five_BUTTON = QPushButton('5', self)
        self.six_BUTTON = QPushButton('6', self)
        self.minus_BUTTON = QPushButton('-', self)
        self.one_BUTTON = QPushButton('1', self)
        self.two_BUTTON = QPushButton('2', self)
        self.three_BUTTON = QPushButton('3', self)
        self.plus_BUTTON = QPushButton('+', self)
        self.plus_minus_BUTTON = QPushButton('+/-', self)
        self.zero_BUTTON = QPushButton('0', self)
        self.comma_BUTTON = QPushButton('.', self)
        self.equal_BUTTON = QPushButton('=', self)
        # endregion

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.overwrite_able = False
        self.ui_init(50, 90, 60)

    def ui_init(self, x_start, y_start, bz):
        """
        Initialize User-Interface
        """
        gray_buttons = [self.c_BUTTON, self.percentage_BUTTON, self.ce_BUTTON, self.back_BUTTON,
                        self.back_BUTTON, self.divided_by_x_BUTTON, self.pow_of_2_BUTTON,
                        self.root_BUTTON, self.divide_BUTTON, self.multiply_BUTTON, self.minus_BUTTON,
                        self.plus_BUTTON]

        white_buttons = [self.zero_BUTTON, self.one_BUTTON, self.two_BUTTON, self.three_BUTTON, self.four_BUTTON,
                         self.five_BUTTON, self.six_BUTTON, self.seven_BUTTON, self.eight_BUTTON, self.nine_BUTTON,
                         self.plus_minus_BUTTON, self.comma_BUTTON]

        for i in gray_buttons:
            i.setStyleSheet("background-color: #A0A0A0;"
                            "border-style: outset")

        for j in white_buttons:
            j.setStyleSheet("background-color: white;"
                            "border-style: outset")

        self.equal_BUTTON.setStyleSheet("background-color: #ADD8E6;"
                                        "border-style: outset")

        # region ButtonPlacement
        """
        Position all buttons on the screen
        """
        self.percentage_BUTTON.setGeometry(QRect(x_start, y_start, bz, bz))
        self.ce_BUTTON.setGeometry(QRect(x_start + 2 + bz, y_start, bz, bz))
        self.c_BUTTON.setGeometry(QRect(x_start + 4 + 2 * bz, y_start, bz, bz))
        self.back_BUTTON.setGeometry(QRect(x_start + 6 + 3 * bz, y_start, bz, bz))

        self.divided_by_x_BUTTON.setGeometry(QRect(x_start, y_start + 2 + bz, bz, bz))
        self.pow_of_2_BUTTON.setGeometry(QRect(x_start + 2 + bz, y_start + 2+bz, bz, bz))
        self.root_BUTTON.setGeometry(QRect(x_start + 4 + 2 * bz, y_start + 2+bz, bz, bz))
        self.divide_BUTTON.setGeometry(QRect(x_start + 6 + 3 * bz, y_start + 2+bz, bz, bz))

        self.seven_BUTTON.setGeometry(QRect(x_start, y_start + 4 + 2 * bz, bz, bz))
        self.eight_BUTTON.setGeometry(QRect(x_start + 2 + bz, y_start + 4 + 2 * bz, bz, bz))
        self.nine_BUTTON.setGeometry(QRect(x_start + 4 + 2 * bz, y_start + 4 + 2 * bz, bz, bz))
        self.multiply_BUTTON.setGeometry(QRect(x_start + 6 + 3 * bz, y_start + 4 + 2 * bz, bz, bz))

        self.four_BUTTON.setGeometry(QRect(x_start, y_start + 6 + 3 * bz, bz, bz))
        self.five_BUTTON.setGeometry(QRect(x_start + 2 + bz, y_start + 6 + 3 * bz, bz, bz))
        self.six_BUTTON.setGeometry(QRect(x_start + 4 + 2 * bz, y_start + 6 + 3 * bz, bz, bz))
        self.minus_BUTTON.setGeometry(QRect(x_start + 6 + 3 * bz, y_start + 6 + 3 * bz, bz, bz))

        self.one_BUTTON.setGeometry(QRect(x_start, y_start + 8 + 4 * bz, bz, bz))
        self.two_BUTTON.setGeometry(QRect(x_start + 2 + bz, y_start + 8 + 4 * bz, bz, bz))
        self.three_BUTTON.setGeometry(QRect(x_start + 4 + 2 * bz, y_start + 8 + 4 * bz, bz, bz))
        self.plus_BUTTON.setGeometry(QRect(x_start + 6 + 3 * bz, y_start + 8 + 4 * bz, bz, bz))

        self.plus_minus_BUTTON.setGeometry(QRect(x_start, y_start + 10 + 5 * bz, bz, bz))
        self.zero_BUTTON.setGeometry(QRect(x_start + 2 + bz, y_start + 10 + 5 * bz, bz, bz))
        self.comma_BUTTON.setGeometry(QRect(x_start + 4 + 2 * bz, y_start + 10 + 5 * bz, bz, bz))
        self.equal_BUTTON.setGeometry(QRect(x_start + 6 + 3 * bz, y_start + 10 + 5 * bz, bz, bz))
        # endregion

        # region ButtonCommand
        """
        Connecting all buttons to commands
        """
        self.zero_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.zero_BUTTON.text()))
        self.one_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.one_BUTTON.text()))
        self.two_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.two_BUTTON.text()))
        self.three_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.three_BUTTON.text()))
        self.four_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.four_BUTTON.text()))
        self.five_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.five_BUTTON.text()))
        self.six_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.six_BUTTON.text()))
        self.seven_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.seven_BUTTON.text()))
        self.eight_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.eight_BUTTON.text()))
        self.nine_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.nine_BUTTON.text()))

        self.minus_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.minus_BUTTON.text()))
        self.plus_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.plus_BUTTON.text()))
        self.divide_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.divide_BUTTON.text()))
        self.multiply_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.multiply_BUTTON.text()))

        self.equal_BUTTON.clicked.connect(lambda: sc.set_result(self))
        self.back_BUTTON.clicked.connect(lambda: sc.delete_command(self))
        self.pow_of_2_BUTTON.clicked.connect(lambda: sc.calc_pow(self))
        self.root_BUTTON.clicked.connect(lambda: sc.calc_root(self))
        self.plus_minus_BUTTON.clicked.connect(lambda: sc.calc_inverse_sign(self))
        self.comma_BUTTON.clicked.connect(lambda: sc.expanse_expression(self, self.comma_BUTTON.text()))
        self.divided_by_x_BUTTON.clicked.connect(lambda: sc.calc_divide_x(self))
        # endregion

        self.lineEdit.setReadOnly(True)
        self.lineEdit.setGeometry(QRect(x_start, y_start + 5 - bz, 4 * bz + 6, 35))
        self.lineEdit.setStyleSheet("color: white")
        font = self.lineEdit.font()
        font.setPointSize(17)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.lineEdit.setMaxLength(18)
        self.c_BUTTON.clicked.connect(lambda: sc.clear_display(self))

    def request_layout(self):
        """
        request_layout generates the layout and returns it
        :return: Layout
        """
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self)
        return layout, 370, 500
