from PyQt5.QtWidgets import QApplication, QDesktopWidget
from watermark_front import MyWindow
import sys

def center_on_screen(window):
	frame = window.frameGeometry()
	screen = QDesktopWidget().availableGeometry().center()
	frame.moveCenter(screen)
	window.move(frame.topLeft())

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyWindow()
	screen_resolution = app.desktop().screenGeometry()
	window.resize(int(screen_resolution.width() * 0.8), int(screen_resolution.height() * 0.8))
	center_on_screen(window)
	window.show()
	sys.exit(app.exec_())