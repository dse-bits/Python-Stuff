#import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.font import Font

class dashFun:
	def __init__(self):
		self.test = "test text"
		print("\n::: gui.py init class userGui")

	@classmethod
	def pressButton(cls):
		""" for button"""
		print("\n::: gui.py pressing button")
	
	@classmethod
	def pressSaveFrameButton(cls):
		""" for button"""
		print("\n::: gui.py pressing lights ""save"" button")
		print("set option to", end=" "), print(str(comboLights.get()))
		labelLightsValue.configure(text=str(comboLights.get()))
		
	@classmethod
	def pressSaveTempButton(cls):
		""" for button"""
		print("\n::: gui.py pressing temperatur ""save"" button")
		newTemp = entryTemp.get()
		print("set option to", end=" "), print(str(newTemp))
		entryTemp.insert(END, newTemp)
	
#def baseCanvas(self):
print("\n start baseCanvas")
root = Tk()
iconBar= PhotoImage(file="ardu-trans_a.png")
root.iconphoto(False, iconBar)
root.geometry("360x200")
root.title("UAC 0.01")
root.grid_columnconfigure((0,1), weight=1)

lightsValues = ("Lights on", "Lights off")
tempValue = 20
w2, w7, w10, w15, w20, w30 = 2, 7, 10, 15, 20, 30

# TOP ROW : DESCRIPTION LABEL AND SPACERS
font09bold = Font(size=9, weight="bold")
labelDash = Label(root, text="TEST GUI     ", font=font09bold)
labelDash.grid(row=0, column=1)
labelSpacer0 = Label(root, width=w2, text="")
labelSpacer1 = Label(root, width=w2, text="")
labelSpacer2 = Label(root, width=w2, text="")
labelSpacer0.grid(row=0, column=2)
labelSpacer1.grid(row=0, column=4)
labelSpacer2.grid(row=0, column=6)

# FIRST ROW : FRAME AND COMBOBOX
labelLightsDescript = Label(root, width=w10, text="Lights: ")
comboLights = Combobox(root, width=w10)

labelLightsValue = Label(root, anchor="center", font=font09bold, width=w15, relief=GROOVE,
						 background="white", text=comboLights.get())
					#frameLights = Frame(root, border=1, relief=FLAT) # RELIEFS: FLAT, RAISED, SUNKEN, GROOVE, RIDGE
# comboLights['values'] = ("Lights on", "Lights off")
comboLights['values'] = lightsValues
comboLights.current(0)
buttonLights = Button(root, text='Save', command=dashFun.pressSaveFrameButton, width=w7)
labelLightsDescript.grid(row=1, column=0)
labelLightsValue.grid(row=1, column=1)
comboLights.grid(row=1, column=3)
buttonLights.grid(row=1, column=5)

# 2ND ROW : SPACER
labelSpacer4 = Label(root)
labelSpacer4.grid(row=2, column=1)

# 3ND ROW : ENTRY (TEXT BOX)
labelTempDescript = Label(root, width=w10, text="Temp: ") #, bg="white")
entryTemp = Entry(root, width=13)
labelTempValue = Label(root, anchor="center", font=font09bold, width=w15, relief=GROOVE,
						 background="white", text=tempValue)
buttonTemp = Button(root, text='Save', command=dashFun.pressSaveTempButton(), width=w7)
labelTempDescript.grid(row=2, column=0)
labelTempValue.grid(row=2, column=1)
entryTemp.grid(row=2, column=3)
buttonTemp.grid(row=2, column=5)

root.mainloop()