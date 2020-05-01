from numexpr import evaluate


def clear_display(root):
    """
    clear_display deletes all characters from the calculator
    :param root: data from StandardUI
    """
    root.lineEdit.setText('')


def get_display_text(root):
    """
    get_display_text returns the equation on the calculator
    :param root: data from StandardUI
    :return: equation on the calculator
    """
    return root.lineEdit.text()


def set_display_text(root, text):
    """
    set_display_text sets the displayed text on the calculator
    :param root: data from StandardUI
    :param text: text to print on calculator
    """
    root.lineEdit.setText(text)


def expanse_expression(root, button_text):
    """
    expanse_expression expanses the displayed equation with the new input
    :param root: data from StandardUI
    :param button_text: new input
    """
    if root.overwrite_able:
        current_expression = button_text
        root.overwrite_able = False
    else:
        current_expression = get_display_text(root) + button_text
    set_display_text(root, current_expression)


def check_number(number):
    """
    check_number checks if parameter is a valid number
    :param number: data from StandardUI
    :return: True: is number; False: is not number
    """
    try:
        float(number)
        return True
    except ValueError:
        return False


def calc_result(root):
    """
    calc_result calculates the result
    :param root: data from StandardUI
    :return: result
    """
    try:
        eval_result = evaluate(get_display_text(root)).item()
        return str(eval_result)
    except:
        root.overwrite_able = True
        return "Error"


def set_result(root):
    """
    set_result calculates result and shows it on display
    :param root: data from StandardUI
    """
    _result = calc_result(root)
    if not _result == "Error":
        set_display_text(root, str(round(float(calc_result(root)), 2)))
    else:
        set_display_text(root, _result)


def delete_command(root):
    """
    delete_command deletes the last character from the display
    :param root: data from StandardUI
    """
    last_deleted = get_display_text(root)[:-1]
    set_display_text(root, last_deleted)


def calc_pow(root):
    """
    calc_pow calculates ^2
    :param root: data from StandardUI
    """
    if not get_display_text(root).isdigit():
        _result = calc_result(root)
        _pow = pow(float(_result), 2)
    else:
        _pow = pow(float(get_display_text(root)), 2)
    set_display_text(root, str(round(_pow, 2)))


def calc_root(root):
    """
    calc_root calculates the square root
    :param root: data from StandardUI
    """
    if not get_display_text(root).isdigit():
        _result = calc_result(root)
        _root = float(_result)**(1/2)
    else:
        _root = float(get_display_text(root))**(1/2)
    set_display_text(root, str(round(_root, 2)))


def calc_inverse_sign(root):
    """
    calc_inverse_sign calculates *-1
    :param root: data from StandardUI
    """
    if not check_number(get_display_text(root)):
        inverse_sign = "-(" + get_display_text(root) + ")"
    else:
        inverse_sign = float(get_display_text(root)) * -1
    set_display_text(root, str(inverse_sign))


def calc_divide_x(root):
    """
    calc_divide_x calculates 1/x
    :param root: data from StandardUI
    """
    if not check_number(get_display_text(root)):
        _divide = calc_result(root)
        if not _divide == "Error":
            _result = 1 / float(_divide)
    else:
        _divide = 1 / float(get_display_text(root))
    set_display_text(root, str(_divide))