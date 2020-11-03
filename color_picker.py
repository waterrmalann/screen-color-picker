# colorPicker.py
# windows only

"""
	A simple python application that allows you to pick colors on your screen.
	
	-> Keep the program running in the background
	-> Move your mouse cursor to anywhere on the screen.
	-> Hit the keyboard shortcut. (Default: CTRL + ALT + C)
	-> The color code (Hex by default) will then be available on your clipboard.
	-> It also shows up on the console application alongside it's RGB value.
"""

import keyboard
import pyscreenshot
import pyperclip
import ctypes
import os

try:
	# https://stackoverflow.com/a/32541666/11912727
	ctypes.windll.user32.SetProcessDPIAware()
except AttributeError:
	pass
	
class POINT(ctypes.Structure):
	_fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def get_position():
	cursor = POINT()
	ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
	return (cursor.x, cursor.y)

clamp = lambda x: max(0, min(x, 255))
def rgb2hex(rgb):
	return f"#{clamp(rgb[0]):02x}{clamp(rgb[1]):02x}{clamp(rgb[2]):02x}"
	
def get_color(coordX, coordY):
	screenie = pyscreenshot.grab()
	image = screenie.convert('RGB')
	r, g, b = image.getpixel((coordX, coordY))
	return (r, g, b)

def on_hotkey_press():
	cursor_position = get_position()
	color = get_color(cursor_position[0], cursor_position[1])
	hex_color = rgb2hex(color)
	print(f"Coordinates: X = {cursor_position[0]}, Y = {cursor_position[1]}")
	print(f"RGB: {', '.join(str(i) for i in color)}")
	print(f"HEX: {hex_color}")
	print()
	pyperclip.copy(hex_color)

keyboard.add_hotkey("ctrl+alt+c", on_hotkey_press)
os.system('cls & title Color Picker & color e')
print("Point your mouse cursor at anywhere on the screen, hit CTRL + ALT + C")
print("The HEX color code will be available on your clipboard. (Also printed on the console app)\n")
keyboard.wait()