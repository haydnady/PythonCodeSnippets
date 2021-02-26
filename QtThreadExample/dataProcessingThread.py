"""
    Thread class for processing data.
"""

from PySide6.QtCore import QThread, Signal


class DataProcessingThread(QThread):
    message = Signal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)


    """
    - The starting point for the thread. After calling start(), 
      QThreads begin executing in run(). By default, 
      run() starts the event loop by calling exec() 
      and runs a Qt event loop inside the thread.
    - https://doc.qt.io/qt-6/qthread.html#details
    """
    def run(self):
        try:
            self.dataProcessingFunc()

        except Exception as e:
            self.message.emit(f"<b style=color:LightCoral;>{e}<br></b>")


    def stop(self):
        self.quit()
        self.wait()
        self.deleteLater()  # May not be needed, added to delete object when finished..


    # Processing function
    def dataProcessingFunc(self):
        self.message.emit("Data")