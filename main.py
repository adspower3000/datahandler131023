import sys


from PySide6.QtWidgets import QApplication, QMainWindow


from ui_main import Ui_MainWindow


class DataHandler(QMainWindow):
    def __int__(self):
        super(DataHandler, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataHandler()
    window.show()

    sys.exit(app.exec())
