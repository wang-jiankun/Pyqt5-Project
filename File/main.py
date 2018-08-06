import sys
from PyQt5 import sip
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread
from MainWidget import Browser

app = QApplication(sys.argv)
print('主线程: %s' % hex(int(QThread.currentThreadId())))
my_window = Browser()
my_window.show()
sys.exit(app.exec_())
