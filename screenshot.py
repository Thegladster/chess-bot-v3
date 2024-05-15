import pyautogui
import torch
from PIL import ImageGrab
import pathlib

# CHANGE LEFT_OFFSET, TOP_OFFSET, AND SQUARE_SIDE
left_offset = 564
top_offset = 255
square_side = 215

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

monwidth = pyautogui.size()[0]
monheight = pyautogui.size()[1]
right_offset = monwidth - (left_offset + square_side * 8)
bottom_offset = (monheight - top_offset - square_side * 8)

print("Loading model...")
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/LY GAMING PC/yolov5/best.pt')
model.conf = 0.8

def screenshot():
    global df

    # Take a screenshot of window
    chessboard = (left_offset, top_offset, monwidth - right_offset, monheight - bottom_offset)
    im = ImageGrab.grab(chessboard)

    # Inference
    results = model(im)
    results.show()

screenshot()
