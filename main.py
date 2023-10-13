import sys

# from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtSql import QSqlTableModel

from ui_main import Ui_MainWindow
# from connection import Data

class DataHandler(QMainWindow):
    def __int__(self):
        super(DataHandler, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.conn = Data()
        # self.view_data()
        # self.reload_data()

        # self.ui.enterbtn.clicked.connect(self.total_N, self.total_JobHour, self.get_deltaT) #- обновить по нажатию ввода диапазона дат сразу 3 окна и таблицу с графиком

    # def reload_data(self):
    #     self.ui.Sum_N(self.conn.total_N())
    #     self.ui.JobHour(self.conn.total_JobHour)
    #     self.ui.deltaT(self.conn.get_deltaT)
    #
    # def view_data(self):
    #     self.model = QSqlTableModel(self)
    #     self.model.setTable('data_day_suz')
    #     self.model.select()
    #     self.ui.tableView.setModel(self.model)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataHandler()
    window.show()

    sys.exit(app.exec())
