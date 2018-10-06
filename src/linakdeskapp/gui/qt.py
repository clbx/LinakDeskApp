##
##
##


try:
    from PyQt5 import QtCore
    from PyQt5 import QtWidgets
    from PyQt5.QtCore import Qt
    from PyQt5.QtCore import QObject, pyqtSignal
    from PyQt5.QtWidgets import QApplication, qApp
    from PyQt5.QtWidgets import QPushButton
    from PyQt5.QtWidgets import QSpinBox
    from PyQt5.QtWidgets import QLabel
    from PyQt5.QtWidgets import QCheckBox
    from PyQt5.QtWidgets import QSystemTrayIcon
    from PyQt5.QtWidgets import QSpacerItem
    from PyQt5.QtWidgets import QSizePolicy
    from PyQt5.QtWidgets import QStyle, QMenu, QAction
    from PyQt5.QtWidgets import QHBoxLayout
    from PyQt5.QtGui import QIcon
#     from PyQt5 import uic
except ImportError as e:
    ### No module named <name>
    print('Exception while importing:', e)
    exit(1)


## ====================================================


def clearLayout(layout):
    for i in reversed(range(layout.count())): 
        item = layout.takeAt( i )
        if item.widget() != None: 
            item.widget().deleteLater()
        if item.layout() != None:
            clearLayout( item.layout() )
    
    