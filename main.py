from tkinter import Tk, Label, Button
import os
import cv2
import threading
import imutils
from PIL import Image, ImageTk

class Window():
	def __init__(self):
		self.window = Tk()
		self.window.geometry("500x500")

		self.label = Label(self.window, text="Imagen de la camara")
		self.label.place(x=10,y=10)

		btn_on = Button(self.window, text="Iniciar Camara", command=self.init_camera)
		btn_on.place(x=10, y=320)
		btn_of = Button(self.window, text="Apagar Camara", command=self.close_camera)
		btn_of.place(x=120, y=320)
		btn_close = Button(self.window, text="Salir del programa", command=self.close)
		btn_close.place(x=10,y=350)

		self.capture = None

		self.window.mainloop()
	def init_camera(self):
		self.capture = cv2.VideoCapture(0)
		thread = threading.Thread(target=self.on_camera, args=())
		thread.start()

	def on_camera(self):
		while True:
			ret, frame = self.capture.read()
			if ret == False:
				print("Camara apagada")
				break
			frame = cv2.flip(frame, 1)
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			frame = imutils.resize(frame, width=400)

			image = Image.fromarray(frame)
			image = ImageTk.PhotoImage(image)
			self.label.configure(image=image)
			self.label.image =image

	def close_camera(self):
		self.label.configure(image="")
		self.label.image=""
		self.capture.release()
		print("camara apagada")
	def close(self):
		self.window.destroy()
		os._exit(0)

if __name__ == '__main__':
	Window()