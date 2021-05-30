
"""
    Main GUI file.
"""

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from QtThreadExample import dataProcessingThread
from ui_mainwindow import Ui_MainWindow  # UI class
from os.path import expanduser
from PySide6 import QtCore
import sys
import os


class TheApp(QMainWindow, Ui_MainWindow):
    # Desktop path
    userDesktop = expanduser("~") + "\Desktop"

    def __init__(self, window):
        self.setupUi(window)

        # Threads/controllers
        self.dataProcessingWorkerThread = None

        # Connect slots/callbacks
        self.PushButton.clicked.connect(self.startThreads)



    # ============================================ Functions =================================================
    def startThreads(self):
        # Start data processing thread
        self.dataProcessingWorkerThread = dataProcessingThread.DataProcessingThread()

        # Update textBrowser (signal/slot for progress window)
        self.dataProcessingWorkerThread.message.connect(self.updateTextBrowser)
        self.dataProcessingWorkerThread.finished.connect(self.stopRunningThread)


    def stopRunningThreads(self):
        if self.dataProcessingWorkerThread != None:
            self.dataProcessingWorkerThread.stop()
            self.dataProcessingWorkerThread = None


    def updateTextBrowser(self, message):
        print(message)


if __name__ == "__main__":
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"      # For High DPI Displays
    app = QApplication(sys.argv)                         # Create the Qt Application
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # For High DPI Displays
    MainWindow = QMainWindow()

    # Create an instance
    ui = TheApp(MainWindow)

    # Show the window and start the app
    MainWindow.show()
    app.exec()
