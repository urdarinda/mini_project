import sys
import time
import matplotlib.pyplot as plt
import new_interface
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

	def __init__(self):
	    super().__init__()
	    self.title = 'Data about DHT'
	    self.left = 20
	    self.top = 20
	    self.width = 640
	    self.height = 480
	    self.initUI()
	    self.Object = new_interface.UIHandler(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)


	    #######
		self.textbox_one = QLineEdit(self)
		self.textbox_one.move(20,20)
		self.textbox_one.resize(220,27)

		self.button_one = QPushButton('Get the CPU usage of this node', self)
		self.button_one.move(280, 20)
		self.button_one.resize(250,self.button_one.sizeHint().height())
		self.button_one.clicked.connect(self.on_click_one)


		#######
		self.textbox_two = QLineEdit(self)
		self.textbox_two.move(20, 80)
		self.textbox_two.resize(220, 27)

		self.button_two = QPushButton('Get the list of nodes having this image', self)
		self.button_two.move(280, 80)
		self.button_two.resize(250, self.button_two.sizeHint().height())
		self.button_two.clicked.connect(self.on_click_two)


        #######
		self.button_three = QPushButton('Get the list of all the peers present in DHT', self)
		self.button_three.move(20, 140)
		self.button_three.resize(500, self.button_three.sizeHint().height())
		self.button_three.clicked.connect(self.on_click_three)


        #######
		self.textbox_three = QLineEdit(self)
		self.textbox_three.move(20, 200)
		self.textbox_three.resize(240, 27)

		self.textbox_four = QLineEdit(self)
		self.textbox_four.move(280, 200)
		self.textbox_four.resize(240, 27)

		'''
		self.textbox_five = QLineEdit(self)
		self.textbox_five.move(20,300)
		self.textbox_five.resize(500,500)
		'''

		self.button_four = QPushButton('Get the CPU usage of this node for the entered number of seconds.', self)
		self.button_four.move(20, 250)
		self.button_four.resize(500, self.button_two.sizeHint().height())
		self.button_four.clicked.connect(self.on_click_four)



		self.show()

	def on_click_one(self):

		self.textboxvalue = self.textbox_one.text()
		self.textboxvalue = str(self.Object.extract_info(1,self.textboxvalue))
		#self.textboxvalue = code.func(self.textboxvalue)
		QMessageBox.question(self,'Information',self.textboxvalue,QMessageBox.Ok,QMessageBox.Ok)
		self.textbox_one.setText("")
		#self.textbox.text("")

	def on_click_two(self):
		self.textboxvalue = self.textbox_two.text()
		self.textboxvalue = str(self.Object.extract_info(2,self.textboxvalue))
		print ()
		#self.textboxvalue = code.func(self.textboxvalue)
		QMessageBox.question(self,'Information',self.textboxvalue,QMessageBox.Ok,QMessageBox.Ok)
		self.textbox_two.setText("")
		#self.textbox.text("")

	def on_click_three(self):
		#obj = code2.MyClass()
		#self.textboxvalue = obj.func()
		self.textboxvalue = str(self.Object.extract_info(3,""))
		QMessageBox.question(self,'Information',self.textboxvalue,QMessageBox.Ok,QMessageBox.Ok)
		self.textbox_one.setText("")
		self.textbox_two.setText("")
		#self.textbox.text("")

	def on_click_four(self):
		self.textboxvalue_one = self.textbox_three.text()
		self.textboxvalue_two = self.textbox_four.text()
		number_of_secs = int(self.textboxvalue_two)
		y_axis = []
		x_axis = []
		
		for i in range(1,number_of_secs + 1):
			val_to_append = str(self.Object.extract_info(1,self.textboxvalue_one))
			y_axis.append(float(val_to_append))
			x_axis.append(i)
			time.sleep(1)
			#self.textbox_five.setText(answer)
		print(y_axis)

		plt.plot(x_axis,y_axis)
		plt.show()
		#QMessageBox.question(self,'Information',answer,QMessageBox.Ok,QMessageBox.Ok)
		#self.textbox_five.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

