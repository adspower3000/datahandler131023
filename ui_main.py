# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QFrame,
    QGraphicsView, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(701, 558)
        font = QFont()
        font.setFamilies([u"Finlandica-Medium"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"font-family: Finlandica-Medium;\n"
"background-color: rgb(31, 28, 53)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_openfile = QPushButton(self.centralwidget)
        self.btn_openfile.setObjectName(u"btn_openfile")
        font1 = QFont()
        font1.setFamilies([u"Finlandica-Medium"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_openfile.setFont(font1)
        self.btn_openfile.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"widht: 100px;\n"
"height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255,70);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_openfile)

        self.horizontalSpacer = QSpacerItem(578, 29, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"background-color: rgba(255, 255, 255,30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px")

        self.horizontalLayout.addWidget(self.graphicsView)

        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"background-color: rgba(255, 255, 255,30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px")
        self.verticalLayout_4 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, 12, 12, 30)
        self.entering_the_date = QHBoxLayout()
        self.entering_the_date.setSpacing(0)
        self.entering_the_date.setObjectName(u"entering_the_date")
        self.entering_the_date.setContentsMargins(-1, 12, 12, 12)
        self.entering_the_date_diapazon = QVBoxLayout()
        self.entering_the_date_diapazon.setSpacing(0)
        self.entering_the_date_diapazon.setObjectName(u"entering_the_date_diapazon")
        self.entering_the_date_diapazon.setContentsMargins(12, 12, 12, 12)
        self.by_date = QHBoxLayout()
        self.by_date.setSpacing(6)
        self.by_date.setObjectName(u"by_date")
        self.by_date.setContentsMargins(0, 0, 0, -1)
        self.label_7 = QLabel(self.MainFrame)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setFamilies([u"Finlandica-Medium"])
        font2.setPointSize(20)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none\n"
" ")

        self.by_date.addWidget(self.label_7)

        self.bytimepicker = QDateEdit(self.MainFrame)
        self.bytimepicker.setObjectName(u"bytimepicker")
        self.bytimepicker.setMaximumSize(QSize(170, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Finlandica-Medium"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.bytimepicker.setFont(font3)
        self.bytimepicker.setStyleSheet(u"color: white;\n"
"padding-left: 8px;\n"
"")
        self.bytimepicker.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.bytimepicker.setDateTime(QDateTime(QDate(2022, 12, 31), QTime(15, 0, 0)))

        self.by_date.addWidget(self.bytimepicker)


        self.entering_the_date_diapazon.addLayout(self.by_date)

        self.until_date = QHBoxLayout()
        self.until_date.setObjectName(u"until_date")
        self.until_date.setContentsMargins(0, -1, 0, 0)
        self.label_8 = QLabel(self.MainFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(60, 16777215))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.until_date.addWidget(self.label_8)

        self.untiltimepicker = QDateEdit(self.MainFrame)
        self.untiltimepicker.setObjectName(u"untiltimepicker")
        self.untiltimepicker.setMaximumSize(QSize(170, 16777215))
        self.untiltimepicker.setFont(font3)
        self.untiltimepicker.setStyleSheet(u"color: white;\n"
"padding-left: 8px")
        self.untiltimepicker.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.untiltimepicker.setDateTime(QDateTime(QDate(2022, 12, 31), QTime(15, 0, 0)))

        self.until_date.addWidget(self.untiltimepicker)


        self.entering_the_date_diapazon.addLayout(self.until_date)


        self.entering_the_date.addLayout(self.entering_the_date_diapazon)

        self.enterbtn = QPushButton(self.MainFrame)
        self.enterbtn.setObjectName(u"enterbtn")
        self.enterbtn.setFont(font3)
        self.enterbtn.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"widht: 100px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255,70);\n"
"}\n"
"")

        self.entering_the_date.addWidget(self.enterbtn)


        self.verticalLayout_4.addLayout(self.entering_the_date)

        self.data = QHBoxLayout()
        self.data.setObjectName(u"data")
        self.data_name = QVBoxLayout()
        self.data_name.setSpacing(0)
        self.data_name.setObjectName(u"data_name")
        self.data_name.setContentsMargins(12, 12, 12, 12)
        self.Sum_N_2 = QLabel(self.MainFrame)
        self.Sum_N_2.setObjectName(u"Sum_N_2")
        self.Sum_N_2.setFont(font2)
        self.Sum_N_2.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.data_name.addWidget(self.Sum_N_2)

        self.JobHour_2 = QLabel(self.MainFrame)
        self.JobHour_2.setObjectName(u"JobHour_2")
        self.JobHour_2.setFont(font2)
        self.JobHour_2.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.data_name.addWidget(self.JobHour_2)

        self.deltaT_2 = QLabel(self.MainFrame)
        self.deltaT_2.setObjectName(u"deltaT_2")
        self.deltaT_2.setFont(font2)
        self.deltaT_2.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.data_name.addWidget(self.deltaT_2)


        self.data.addLayout(self.data_name)

        self.data_digital = QVBoxLayout()
        self.data_digital.setSpacing(0)
        self.data_digital.setObjectName(u"data_digital")
        self.data_digital.setContentsMargins(12, 12, 12, 12)
        self.Sum_N = QLabel(self.MainFrame)
        self.Sum_N.setObjectName(u"Sum_N")
        self.Sum_N.setFont(font2)
        self.Sum_N.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.data_digital.addWidget(self.Sum_N)

        self.JobHour = QLabel(self.MainFrame)
        self.JobHour.setObjectName(u"JobHour")
        self.JobHour.setFont(font2)
        self.JobHour.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.data_digital.addWidget(self.JobHour)

        self.deltaT = QLabel(self.MainFrame)
        self.deltaT.setObjectName(u"deltaT")
        self.deltaT.setFont(font2)
        self.deltaT.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none")

        self.data_digital.addWidget(self.deltaT)


        self.data.addLayout(self.data_digital)


        self.verticalLayout_4.addLayout(self.data)


        self.horizontalLayout.addWidget(self.MainFrame)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView::section {\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item{\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTableItem::item:selected {\n"
"border: none;\n"
"color: rgba(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 30);\n"
"}")

        self.verticalLayout.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DataHandler", None))
        self.btn_openfile.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e", None))
        self.enterbtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434", None))
        self.Sum_N_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0437\u0430 \u0446\u0438\u043a\u043b", None))
        self.JobHour_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0447\u0438\u0435 \u0447\u0430\u0441\u044b", None))
        self.deltaT_2.setText(QCoreApplication.translate("MainWindow", u"deltaT", None))
        self.Sum_N.setText(QCoreApplication.translate("MainWindow", u"3423432", None))
        self.JobHour.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.deltaT.setText(QCoreApplication.translate("MainWindow", u"41.1", None))
    # retranslateUi

