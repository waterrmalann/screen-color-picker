# Screen Color Picker

A python application that enables you to pick colors from your screen using your mouse cursor to point.

## Usage

Keep the program running in the background, move your mouse cursor to any point on the screen. Hit the keyboard shortcut combination (CTRL + ALT + C by default). The hex color code of the pixel on that exact point your cursor was on will be sent to your clipboard (eg: #ffffff). It'll also get printed on the console application alongside it's RGB value and the coordinate.

## Requirements

- [Python](https://www.python.org/) 3.7 or above.
- [ctypes](https://pypi.org/project/ctypes/)
- os
- [keyboard](https://pypi.org/project/keyboard/) (for listening to hotkeys)
- [pyscreenshot](https://pypi.org/project/pyscreenshot/) (for taking the screenshot)
- [pyperclip](https://pypi.org/project/pyperclip/) (for copying hex code to clipboard)

### Notes

This program is written specifically to run on Windows systems. I will update it soon though so that it will work on Mac and Linux systems.

### Todos

- MacOS support.
- Linux support.
- Config file so that users can easily change the hotkeys, alongside other settings.

License
----

MIT License