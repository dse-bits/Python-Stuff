#import tkinter as tk
from tkinter import *
from tkinter.font import Font

class dashGui:
	def __init__(self):
		self.test = "test text"
		self.txtTemp = "Temp"
		self.txtCo2 = "CO2"
		print("\n::: gui.py init class userGui")
		
	@classmethod
	def pressTemp(cls):
		""" action for Temp button"""
		print("\n::: gui.py pressing Temp")
	
	@classmethod
	def pressCo2(cls):
		""" action for CO2 button"""
		print("\n::: gui.py pressing CO2")
	
	@classmethod
	def pressLight(cls):
		""" action for Light button"""
		print("\n::: gui.py pressing Light")
	
	@classmethod
	def pressMoist(cls):
		""" action for Moisture button"""
		print("\n::: gui.py pressing Moisture")
	
	@classmethod
	def pressLogout(cls):
		""" action for Logout button"""
		print("\n::: gui.py pressing Logout")
		
	@classmethod
	def pressButton(cls):
		""" for button"""
		print("\n::: gui.py pressing button")
		
#def baseCanvas(self):
	print("\n start baseCanvas")
	root = Tk()
	iconBar= PhotoImage(file="D:/HQ/projects/dev/icon_32.png")
	root.iconphoto(False, iconBar)
	root.geometry("480x200")
	root.title("UAC 0.01")
	root.grid_columnconfigure((0,1), weight=1)
# screen_dash = Canvas(root, width=640, height=480) # geometry in pixels
	font11norm = Font(size=11, weight="normal")
	font10bold = Font(size=10, weight="bold")
		#descriptDash = Label(root, text="Current Sensor Values0", font=("Arial", 12))
		#descriptDash = Label(root, text="Current Sensor Values0", font=fontCalibri12bold)
# description of dashboard
	descriptDash = Label(root, text="Current Sensor Values     ", font=font10bold)
# description of values (very left side)
	descriptTemp = Label(root, width=9, text="Temp [C]")
	descriptCo2 = Label(root, width=9, text="CO2 Level")
	descriptLight = Label(root, width=9, text="Light Power")
	descriptMoist = Label(root, width=9, text="Moisture")
	descriptTest = Label(root, width=9, text="Test")
# values of sensors (middle)
	entryTemp = Entry(root, width=45)
	entryCo2 = Entry(root, width=45)
	entryLight = Entry(root, width=45)
	entryMoist = Text(root, height=1, width=34) # state="disabled")
	entryMoist.insert(END, "aaaa")
	entryMoist = Text(root, height=1, width=34, state="disabled")
	#entryMoist = Text(root, state="disabled", width=45)
	#entryMoist.insert(0, "moiii")
# buttons (right side)
	buttonTemp = Button(root, text='Temp', command=pressButton, width=7)
	buttonCo2 = Button(root, text='CO2', command=pressButton, width=7)
	buttonLight = Button(root, text='Light', command=pressButton, width=7)
	buttonMoist = Button(root, text='Moist', command=pressButton, width=7)
	buttonTest = Button(root, text='Test', command=pressButton, width=7)
# buttons (right side)
	#buttonRefresh = Button(text='Refresh ', command=pressButton, width=7)
	buttonLogout = Button(text='Logout ', command=pressButton, width=7)
# spacers (very right side)
	spacerTempRight = Label(root, width=3, text="")
	# spacerCo2Right = Label(root, width=3, text="")
	# spacerLightRight = Label(root, width=3, text="")
	# spacerMoistRight = Label(root, width=3, text="")
	spacerRow5 = Label(root, width=3, text="")
# grid alignment of the dashboard description
	descriptDash.grid(row=0, column=1)
# grid alignment of the descriptions
	descriptTemp.grid(row=1, column=0)
	descriptCo2.grid(row=2, column=0)
	descriptLight.grid(row=3, column=0)
	descriptMoist.grid(row=4, column=0)
# grid alignment of the value fields (entries)
	entryTemp.grid(row=1, column=1)
	entryCo2.grid(row=2, column=1)
	entryLight.grid(row=3, column=1)
	entryMoist.grid(row=4, column=1)
# grid alignment of the buttons
	buttonTemp.grid(row=1, column=2)
	buttonCo2.grid(row=2, column=2)
	buttonLight.grid(row=3, column=2)
	buttonMoist.grid(row=4, column=2)
# alignment of bottom buttons
	#buttonRefresh.grid(row=0, column=2)
	buttonLogout.grid(row=6, column=2)
# grid alignment of the spacers
	spacerTempRight.grid(row=1, column=3)
	# spacerCo2Right.grid(row=2, column=3)
	# spacerLightRight.grid(row=3, column=3)
	# spacerMoistRight.grid(row=4, column=3)
	spacerRow5.grid(row=5, column=0)
	
	root.mainloop()
