from PyQt5.QtCore import QThread, QObject


# 创建自己的类继承自QObject，并写一个工作函数
class Worker(QObject):
    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)

    def work(self):
        print('当前线程: %s' % hex(int(QThread.currentThreadId())))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    # 查看当前线程id
    print('主线程: %s' % hex(int(QThread.currentThreadId())))
    # 实例化线程对象
    t = QThread()
    # 实例化工作类对象
    worker = Worker()
    # 工作类对象转化为线程对象
    worker.moveToThread(t)
    # 绑定线程启动信号的槽函数
    t.started.connect(worker.work)
    # 启动线程
    t.start()

    app.exec_()
