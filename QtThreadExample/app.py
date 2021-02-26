
"""
    Main GUI file.
"""

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from os.path import expanduser
from PySide6 import QtCore


class TheApp(QMainWindow, Ui_MainWindow):
    userDesktop = expanduser("~") + "\Desktop"

    def __init__(self, window):
        self.setupUi(window)

        # Threads/controllers
        self.generalAnalysesWorkerThread = None