# from PyQt5.QtWidgets import QApplication

# app = QApplication([])
# screen = app.primaryScreen()
# screenshot = screen.grabWindow(QApplication.desktop().winId())

# # screenshot.show()

# pic = QtGui.QLabel(self)

# pic.setPixmap(QtGui.QPixmap(screenshot)) # "Q107.png"

# pic.show() # You were missing this.

# # print(type(screenshot.size()))

# # print(screenshot.width())

# # screenshot.save('/tmp/screenshot.png')

# # screenshot.save('screenshot.png')


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QRect
# import PyQt5.QRect
 
class App(QWidget):
 
	def __init__(self):
		super().__init__()
		self.title = 'PyQt5 image - pythonspot.com'
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480
		self.initUI()
 
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
 
		# Create widget
		label = QLabel(self)

		screen = app.primaryScreen()
		screenshot = screen.grabWindow(QApplication.desktop().winId())
		# r1 = QRect(O, О, 20, 20)
		# QRect r1(100, 200, 11, 16)
		
		wid2origRect = QRect(0, 0, 100, 100)
		image = screenshot.copy(wid2origRect)


		# QPixmap cropped = screenshot.copy(r1);
		# im2 = screenshot.copy(r1)


		pixmap = QPixmap(image)


		label.setPixmap(pixmap)
		self.resize(pixmap.width(),pixmap.height())
 
		self.show()
 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())