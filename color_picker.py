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

import keyboard  # to set up and listen to hotkeys.
import pyscreenshot  # to take a screenshot. (duh)
import pyperclip  # to copy color codes to clipboard.
import ctypes  # to access cursor position.
import os  # to clear screen and set window title.

HOTKEY = "ctrl+alt+c"

try:
	# https://stackoverflow.com/a/32541666/11912727
	# for accurate cursor coordinates.
	ctypes.windll.user32.SetProcessDPIAware()
except AttributeError:
	pass  # apparently it doesn't work on Windows XP.
	
class POINT(ctypes.Structure):
	_fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def get_position():
	"""Get current cursor position."""
	
	cursor = POINT()
	# grab the position of the mouse cursor.
	ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
	return (cursor.x, cursor.y)

def rgb2hex(rgb):
	"""To convert the RGB values to HEX."""
	
	clamp = lambda x: max(0, min(x, 255))
	return f"#{clamp(rgb[0]):02x}{clamp(rgb[1]):02x}{clamp(rgb[2]):02x}"
	
def get_color(coordX, coordY):
	"""To get the color of the pixel of a given coord on the screen."""
	
	screenie = pyscreenshot.grab()  # take a screenshot.
	image = screenie.convert('RGB')
	r, g, b = image.getpixel((coordX, coordY))  # get the color of the pixel at the coords.
	return (r, g, b)

def on_hotkey_press():
	"""Called when CTRL+ALT+C is pressed"""
	
	cursor_position = get_position()
	color = get_color(cursor_position[0], cursor_position[1])
	hex_color = rgb2hex(color)
	print("[Color Picked]")
	print(f"Coordinates: X = {cursor_position[0]}, Y = {cursor_position[1]}")
	print(f"RGB: {', '.join(str(i) for i in color)}")
	print(f"HEX: {hex_color}")
	print()
	pyperclip.copy(hex_color)  # copy the hex code to clipboard.

keyboard.add_hotkey(HOTKEY, on_hotkey_press)  # set up the keyboard combo and hook it to the function.
os.system('cls & title Screen Color Picker & color e')
print(f"Point your mouse cursor at anywhere on the screen, hit {HOTKEY.upper()}")
print("The HEX color code will be available on your clipboard. (Also printed here)\n")
keyboard.wait()  # infinite blocking loop just to listen for the hotkey.