import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

def window():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("Game")
    window.setGeometry(50, 50, 500, 500)
    tableWidget = QtWidgets.QTableWidget(4, 4)
    tableWidget.resizeColumnsToContents()
    tableWidget.resize(500, 300)
    tableWidget.show()

    window.show()

    sys.exc_info(app.exec_())

window()
