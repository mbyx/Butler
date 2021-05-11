from PyQt5.QtWidgets import QApplication, QSystemTrayIcon
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
import os


def path():
    root = __file__
    if os.path.islink(root):
        root = os.path.realpath(root)
    return os.path.dirname(os.path.abspath(root))


def toast(title: str = 'Notification', msg: str = 'Here Comes The Message!', delay: int = 2, icon: str = '', msg_icon: str = ''):
    App = QApplication([])
    Tray = QSystemTrayIcon(QIcon(icon))
    Tray.show()
    QTimer.singleShot(delay * 1000, App.exit)
    Tray.showMessage(title, msg, QIcon(msg_icon), delay * 1000)
    App.exec_()