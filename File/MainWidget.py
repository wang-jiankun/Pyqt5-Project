from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from browser_ui import Ui_Form
import cv2
import time


class Browser(QWidget):
    # 初始化
    def __init__(self, parent=None):
        super(Browser, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pb_browser.clicked.connect(self.slot_open_browser)
        self.ui.pb_open.clicked.connect(self.slot_openfile)

    # 打开文件浏览器槽函数
    def slot_open_browser(self):
        # 打开文件浏览器，获得选择的文件
        file_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Images (*.png *.xpm *.jpg *.avi *.mp4)')
        # print(file_name)
        # 判断是否选择了文件
        if file_name[0] != '':
            # print('open')
            # 显示文件名
            self.ui.lineEdit.setText(file_name[0])
            # 显示文件内容
            # with open(file_name[0], 'r') as f:
            #     my_txt = f.read()
            #     self.lineEdit.setPlainText(my_txt)

    # 打开文件槽函数
    def slot_openfile(self):
        # 获取文件名
        file_name = self.ui.lineEdit.text()
        if file_name == '':
            QMessageBox.information(self, 'empty error', '请选择文件')
            return
        temp = file_name.split('.')[-1]
        if temp == 'avi' or temp == 'mp4':
            self.th = Thread(file_name, self)
            self.th.show_signal.connect(self.show_image)
            self.th.start()
            # 如果th不不定义为类属性，需要下面这两句，程序运行播放视频才不会出错
            # self.image = QImage(file_name)
            # self.ui.lb_show.setPixmap(QPixmap.fromImage(self.image))
            return

        # img = cv2.imread(file_name)
        # cv2.imshow('photo', img)
        # 把图像转换为QT格式
        self.image = QImage(file_name)
        self.ui.lb_show.setPixmap(QPixmap.fromImage(self.image))

    def show_image(self, image):
        # 在label上显示图片
        self.ui.lb_show.setPixmap(QPixmap.fromImage(image))
        # 缩放窗
        # self.resize(self.image.width(), self.image.height())


# 采用线程来播放视频
class Thread(QThread):
    # 自定义信号
    show_signal = pyqtSignal(QImage)

    # 构造函数，接受参数
    def __init__(self, file_name, browser):
        QThread.__init__(self)
        self.video_name = file_name
        self.browser = browser

    # 重写run()方法
    def run(self):
        # 实例化一个读取视频对象
        cap = cv2.VideoCapture(self.video_name)

        while cap.isOpened():
            # 读取视频帧
            ret, frame = cap.read()
            # 获取视频的帧数
            fps = cap.get(cv2.CAP_PROP_FPS)

            if ret:
                # 转换图片格式
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                qt_image = QImage(rgb_image.data, rgb_image.shape[1], rgb_image.shape[0], QImage.Format_RGB888)
                p = qt_image.scaled(640, 480, Qt.KeepAspectRatio)
                # 发射信号
                print('线程: %s' % hex(int(QThread.currentThreadId())))
                self.show_signal.emit(p)
                time.sleep(1/fps)
            else:
                image = QImage('E:/11.jpg')
                self.browser.ui.lb_show.setPixmap(QPixmap.fromImage(image))
                self.browser.ui.lb_show.adjustSize()
                print('播放结束')
                break
