# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets, uic, QtCore
import pull_bitcoin
import json

from bitcoin_notifications import Ui_MainWindow

class bitcoin_notifications_(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(bitcoin_notifications_, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pullButton.clicked.connect(self.buttonUpdate)
        self.comboBoxCryptos.addItems(["Bitcoin", "Ethereum", "Litecoin"])

    def updateFields(self):
        with open("/home/jordan/Dev/BitcoinUI/crypto.json", 'r') as cFile:
            data = cFile.read()

        obj = json.loads(data)

        # Fill in fields
        for key in obj['data']:
            percent1h = key["quote"]["USD"]["percent_change_1h"]
        percent1h = str(round(percent1h,2))
        self.lineEdit1H.setText(percent1h)
        print(self.lineEdit1H.text())

        # 24 Hr Change
        for key in obj['data']:
            percent24h = key["quote"]["USD"]["percent_change_24h"]
        percent24h = str(round(percent24h,2))
        self.lineEdit24H.setText(percent24h)
        print(self.lineEdit24H.text())

        # Price
        for key in obj['data']:
            price = key["quote"]["USD"]["price"]
        price = str(round(price,2))
        self.lineEditPrice.setText(price)
        print(self.lineEditPrice.text())

        # Name
        for key in obj['data']:
            name = key["name"]
        self.lineEditCrypto.setText(name)
        print(self.lineEditCrypto.text())

    def determineSelection(self):
        if(self.comboBoxCryptos.currentText() == "Bitcoin"):
            returnID = '1'
        elif(self.comboBoxCryptos.currentText() == "Ethereum"):
            returnID = '2'
        else:
            returnID = '6'
        return returnID

    def buttonUpdate(self):
        id = self.determineSelection()
        pull_bitcoin.cryptoPull(id)
        # Check to see if cryptofile exists before updating
        try:
            cryptoFile = open("/home/jordan/Dev/BitcoinUI/crypto.json")
            self.updateFields()
        except IOError:
            print("File not accessible")
        finally:
            cryptoFile.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = bitcoin_notifications_()
    window.show()
    app.exec()
