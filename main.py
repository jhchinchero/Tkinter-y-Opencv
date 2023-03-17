from tkinter import Tk, Label, Button
import os

class Window():
	def __init__(self):
		self.window = Tk()
		self.window.geometry("500x500")

		self.label = Label(self.window, text="Imagen de la camara")
		self.label.place(x=10,y=10)

		btn_on = Button(self.window, text="Iniciar Camara", command=self.on_camera)
		btn_on.place(x=10, y=300)
		btn_close = Button(self.window, text="Salir del programa", command=self.close)
		btn_close.place(x=10,y=350)

		self.window.mainloop()

	def on_camera(self):
		print("camera")

	def close(self):
		self.window.destroy()
		os._exit(0)
		
if __name__ == '__main__':
	Window()