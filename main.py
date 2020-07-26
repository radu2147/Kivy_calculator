import kivy
kivy.require('1.11.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Main(BoxLayout):
	rez = ObjectProperty(None)
	d0 = ObjectProperty(None)
	d1 = ObjectProperty(None)
	d2 = ObjectProperty(None)
	d3 = ObjectProperty(None)
	d4 = ObjectProperty(None)
	d5 = ObjectProperty(None)
	d6 = ObjectProperty(None)
	d7 = ObjectProperty(None)
	d8 = ObjectProperty(None)
	d9 = ObjectProperty(None)
	plus = ObjectProperty(None)
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.value = 0
		self.op = ''

	def clear(self):
		self.rez.text = '0.0'
		self.value = 0

	def add(self):
		if float(self.rez.text) != self.value and self.value != 0:
			self.value += float(self.rez.text)
		else:
			self.value = float(self.rez.text)
		self.rez.text = ''
		self.op = '+'

	def period(self):
		if '.' in self.rez.text:
			self.rez.text = '0.'
			self.value = 0
		else:
			self.rez.text += '.'

	def back(self):
		if self.rez.text == '':
			pass
		else:
			self.rez.text = self.rez.text[:-1]


	def minus(self):
		if float(self.rez.text) != self.value and self.value != 0:
			self.value -= float(self.rez.text)
		else:
			self.value = float(self.rez.text)
		self.rez.text = ''
		self.op = '-'

	def multiply(self):
		if float(self.rez.text) != self.value and self.value != 0:
			self.value *= float(self.rez.text)
		else:
			self.value = float(self.rez.text)
		self.rez.text = ''
		self.op = '*'
	def division(self):
		if float(self.rez.text) != self.value and self.value != 0:
			self.value /= float(self.rez.text)
		else:
			self.value = float(self.rez.text)
		self.rez.text = ''
		self.op = '/'

	def equal(self):
		if self.op == '+':
			self.value += float(self.rez.text)
			self.op = ''
			self.rez.text = str(self.value)
		if self.op == '-':
			self.value -= float(self.rez.text)
			self.op = ''
			self.rez.text = str(self.value)
		if self.op == '*':
			self.value *= float(self.rez.text)
			self.op = ''
			self.rez.text = str(self.value)
		if self.op == '/':
			self.value /= float(self.rez.text)
			self.op = ''
			self.rez.text = str(self.value)


	def digit_button_0(self):
		if self.rez.text == '0.0':
			self.rez.text = self.d0.text
			return
		self.rez.text += self.d0.text

	def digit_button_1(self):
		if self.rez.text == '0.0':
			self.rez.text = self.d1.text
			return
		self.rez.text += self.d1.text
	def digit_button_2(self):
		if self.rez.text == '0.0':
			self.rez.text = self.d2.text
			return
		self.rez.text += self.d2.text
	def digit_button_3(self):
		if self.rez.text == '0.0':
			self.rez.text = self.d3.text
			return
		self.rez.text += self.d3.text
	def digit_button_4(self):
		if self.rez.text == '0.0':
			self.rez.text = self.d4.text
			return
		self.rez.text += self.d4.text
	def digit_button_5(self):
		if self.rez.text == '0.0':
			self.rez.text = self.d5.text
			return
		self.rez.text += self.d5.text
	def digit_button_6(self):
		if self.rez.text == '0.0':
			self.rez.text = self.d6.text
			return
		self.rez.text += self.d6.text
	def digit_button_7(self):
		if self.rez.text == '0.0':
			self.rez.text = self.d7.text
		else:
			self.rez.text += self.d7.text
	def digit_button_8(self):
		if self.rez.text == '0.0':
			self.rez.text = self.d8.text
		else:
			self.rez.text += self.d8.text
	def digit_button_9(self):
		if self.rez.text == '0.0':
			self.rez.text = self.d9.text
		else:
			self.rez.text += self.d9.text


class MainApp(App):
	title = "Kivy Calculator"
	def build(self):
		return Main()

if __name__ == '__main__':
    MainApp().run()