# from PySide6 import  QtWidgets, QtSql
# # from ui_main import DatePicker
#
# class Data:
#     def __int__(self):
#         super(Data, self).__init__()
#         self.create_connection()
#
#
#     def create_connection(self):
#         db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
#         db.setDatabaseName('data_handler_db.db')
#
#         if not db.open():
#             QtWidgets.QMessageBox.critical(None, "Cannot open database",
#                                            "Click Cancel to exit", QtWidgets.QMessageBox.Cancel)
#             return False
#
#         query = QtSql.QSqlQuery()
#         query.exec("CREATE TABLE IF NOT EXISTS data_hours (ID integer primary key AUTOINCREMENT, ")
#         query.exec("CREATE TABLE IF NOT EXISTS data_with_srk_day (ID integer primary key AUTOINCREMENT, ")
#         query.exec("CREATE TABLE IF NOT EXISTS data_day_suz (ID integer primary key AUTOINCREMENT, ")
#         return True
#
#     def execute_query_with_params(self, sql_query, query_values=None):
#         query = QtSql.QSqlQuery()
#         query.prepare(sql_query)
#
#         if query_values is not None:
#             for query_value in query_values:
#                 query.addBindValue(query_value)
#
#         return query.exec()
#
#     # нужен фильтр по диапазону дат от и до
#     def get_total(self, column, filter=None, value=None):
#         sql_query = f"SELECT SUM({column}) FROM data_day_suz"
#
#         if filter is not None or value is not None:
#             sql_query += f"WHERE @bytimepickerdate.date <= {filter} <= @untiltimepicker.date = ?"
#
#         query_values = []
#
#         if value is not None:
#             query_values.append(value)
#
#         query = self.execute_query_with_params(sql_query, query_values)
#
#         if query.next():
#             return str(query_values(0))
#
#         return '0'
#
#     def get_average(self, column, filter=None):
#         sql_query = f"SELECT AVERAGE ({column}) FROM data_day_suz"
#
#         if filter is not None:
#             sql_query += f"WHERE @bytimepickerdate.date <= {filter} <= @untiltimepicker.date = ?"
#
#         query = self.execute_query_with_params(sql_query)
#
#         return str(query)
#
#     def total_N(self):
#         return self.get_total(column="Sum_N", filter="date")
#
#     def total_JobHour(self):
#         return self.get_total(column="JobHour", filter="date")
#
#     def get_deltaT(self):
#         return self.get_average(column="deltaT", filter="date")
#
#
#
#
#   # current = QtCore.QDateTime.currentDateTime()
#   #       self.startDate.setDate(current.date())
#   #       self.endDate.setDate(current.date())
#   #       self.startDate.setDisplayFormat("M/dd/yyyy")
#   #       self.endDate.setDisplayFormat("M/dd/yyyy")
#
#
# # def FilterBetweenDates(self):
# #     start = str(self.startDate.text())
# #     finish = str(self.endDate.text())
# #     filter = "EventDate BETWEEN '{}' AND '{}'".format(start, finish)
# #     print(filter)  # for debugging
# #     self.model.setFilter(filter)
#
