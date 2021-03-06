# MIT License
#
# Copyright (c) 2017 Arkadiusz Netczuk <dev.arnet@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#


from . import uiloader


UiTargetClass, QtBaseClass = uiloader.loadUiFromClassName( __file__ )


class DevicesListDialog(QtBaseClass):
    def __init__(self, parentWidget=None):
        super().__init__(parentWidget)

        self.connector = None
        self.finishedState = 0
        self.foundItems = list()

        self.ui = UiTargetClass()
        self.ui.setupUi(self)

        self.ui.scanBTPB.clicked.connect(self._scanDevices)
        self.ui.connectPB.clicked.connect(self._connectToSelected)
        self.finished.connect(self._setFinished)

    def attachConnector(self, connector):
        self.connector = connector

    def getFinishedState(self):
        return self.finishedState

    def itemDoubleClicked(self, modelIndex):
        currRow = modelIndex.row()
        self.connectToIndexedItem(currRow)

    def _scanDevices(self):
#         print "Scanning for devices"
        self.ui.devicesView.clear()
        self.foundItems = self.connector.scanDevices()
        if self.foundItems is None:
            return
#         print "Found:", foundItems
        for item in self.foundItems:
            self.ui.devicesView.addItem( item.name )

    def _connectToSelected(self):
        currRow = self.ui.devicesView.currentRow()
        self.connectToIndexedItem(currRow)

    def _setFinished(self, result):
        self.finishedState = result

    def connectToIndexedItem(self, itemIndex):
        if itemIndex < 0:
            return
        item = self.foundItems[itemIndex]
        self.connector.connectTo( item.address )
        self.accept()
