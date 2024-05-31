import pyautogui
from PIL import ImageGrab

# CHANGE LEFT_OFFSET, TOP_OFFSET, AND SQUARE_SIDE
left_offset = 564
top_offset = 255
square_side = 215

monwidth = pyautogui.size()[0]
monheight = pyautogui.size()[1]
right_offset = monwidth - (left_offset + square_side * 8)
bottom_offset = (monheight - top_offset - square_side * 8)

def screenshot():
    global df

    # Take a screenshot of window
    chessboard = (left_offset, top_offset, monwidth - right_offset, monheight - bottom_offset)
    im = ImageGrab.grab(chessboard)

    # Shows
    im.show()

screenshot()
