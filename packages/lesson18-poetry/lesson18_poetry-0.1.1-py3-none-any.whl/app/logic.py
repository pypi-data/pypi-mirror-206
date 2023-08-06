from .models import User


def main_logic():
    """
    Логика программы
    :return:
    """
    user = User()
    return user.__dir__()
