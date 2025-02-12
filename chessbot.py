import pyautogui
import torch
import pathlib
from PIL import ImageGrab
from stockfish import Stockfish
import math
import keyboard
import os
import sys
import random
import time

# Finds monitor dimensions for offset + login info
monwidth = pyautogui.size()[0]
monheight = pyautogui.size()[1]
username = os.getlogin()

# var initialization
bestpath = "C:\\Users\\" + username + "\\Downloads\\best.pt"
modelpath = "C:\\Users\\" + username + "\\Downloads\\stockfish-windows-x86-64-avx2\\stockfish\\stockfish-windows-x86-64-avx2.exe"
print(bestpath)

# CHESSBOARD OFFSET (EDIT THESE, CHECK README.md)
left_offset = 458
top_offset = 180
square_side = 235
right_offset = monwidth - (left_offset + square_side * 8)
bottom_offset = (monheight - top_offset - square_side * 8)

# Initialization (EDIT THE FOLLOWING LINE)
stockfish = Stockfish(modelpath)
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
player = "unknown"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']



# STOCKFISH ELO (max possible is ~3500)
a = 2000
stockfish.set_elo_rating(a)

print("Loading model...")

# Model (EDIT THE FOLLOWING LINE)
model = torch.hub.load('ultralytics/yolov5', 'custom', path=bestpath)
model.conf = 0.9

timevar = input("Time control? (min.) ")
timevar = float(timevar)

# Stockfish runs faster, but uses more resources (uncomment following line and change values)
# stockfish.update_engine_parameters({"Hash": 1024, "Threads": 10})

print(stockfish.get_parameters())
def screenshot():
    global df

    # Take a screenshot of window
    chessboard = (left_offset, top_offset, monwidth - right_offset, monheight - bottom_offset)
    im = ImageGrab.grab(chessboard)

    # Inference
    results = model(im)
    # results.show()
    df = (results.pandas().xyxy[0])


def isolate(column, row):
    r = (df.loc[row])
    iso = str(r[[column]])
    return iso


def find_class(cs):
    piece = ('b', 'k', 'n', 'p', 'q', 'r', 'B', 'K', 'N', 'P', 'Q', 'R')
    return (piece[cs])


def write_FEN():
    global written_real_fen
    global written_digital_fen
    global player

    written_real_fen = str('')
    for y in range(8):
        written_real_fen = written_real_fen + '/'
        for x in range(8):
            z = 0
            for row in range(df.shape[0]):

                # Checks if object fits x criteria
                column = "xmax"
                iso = (isolate(column, row))

                # Variable cleaning
                iso = iso.replace(column, '')
                iso = iso.replace('Name:', '')
                iso = iso.replace('dtype: object', '')
                row = str(row)
                iso = iso.replace(row + ',', '')
                iso = float(iso)
                row = int(row)

                if iso < square_side * ((x % 8) + 1) and iso > square_side * (x % 8):

                    # Checks if object fits y criteria
                    column = "ymax"
                    iso = (isolate(column, row))

                    # Variable cleaning
                    iso = iso.replace(column, '')
                    iso = iso.replace('Name:', '')
                    iso = iso.replace('dtype: object', '')
                    row = str(row)
                    iso = iso.replace(row + ',', '')
                    iso = float(iso)
                    row = int(row)

                    if iso < square_side * ((y % 8) + 1) and iso > square_side * (y % 8):
                        iso = (isolate('class', row))

                        # Mild variable cleaning
                        iso = iso.replace('class', '')
                        row = str(row)
                        iso = iso.replace('Name:' + ' ' + row + ', dtype: object', '')
                        row = int(row)
                        iso = iso.replace(' ', '')
                        iso = int(iso)
                        iso = str(iso)

                        # Both x and y criteria are met, class is printed
                        iso = int(iso)
                        written_real_fen = written_real_fen + find_class(iso)
                        z = 1

                    else:
                        row = row
                else:
                    row = row

                if row == df.shape[0] - 1 and z == 0:
                    written_real_fen = written_real_fen + 'X'

    written_digital_fen = written_real_fen

    # Replaces Is with numbers
    written_real_fen = written_real_fen.replace('XXXXXXXX', '8')
    written_real_fen = written_real_fen.replace('XXXXXXX', '7')
    written_real_fen = written_real_fen.replace('XXXXXX', '6')
    written_real_fen = written_real_fen.replace('XXXXX', '5')
    written_real_fen = written_real_fen.replace('XXXX', '4')
    written_real_fen = written_real_fen.replace('XXX', '3')
    written_real_fen = written_real_fen.replace('XX', '2')
    written_real_fen = written_real_fen.replace('X', '1')
    written_real_fen = written_real_fen[:0] + written_real_fen[1:]

    if player == "b":
        written_real_fen = written_real_fen[::-1]
        written_digital_fen = written_digital_fen[::-1]


def FEN_addition():
    # FEN additional info
    global additional
    global written_real_fen
    global written_fen
    global player
    global move

    if written_real_fen == "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR":
        move = "w"
        movenum = str(1)
        castling = "KQkq"
        player = "w"
    else:
        if written_real_fen == "RNBKQBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbkqbnr":
            move = "w"
            movenum = str(1)
            castling = "KQkq"
            player = "b"
        else:
            if 'pppppppp/rnbkqbnr' in written_real_fen:
                move = "b"
                movenum = str(1)
                castling = "KQkq"
                player = "b"
            else:
                move = input("Whose turn is it to move? [w/b]: ")
                movenum = str(1)
                castling = input("Specify castling: [K/Q/k/q]: ")
                player = input("What color player are you? [w/b]: ")

                if castling == '':
                    castling = '-'

    if player == "b":
        written_real_fen = written_real_fen[::-1]

    additional = " " + move + " " + castling + " - 0 " + movenum
    written_fen = written_real_fen + additional

def conversion(coord, location):
    return (letters.index(coord[location]))


def move_mouse(x1, y1, x2, y2):
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    if player == "w":
        pyautogui.click(left_offset + square_side * x1 + square_side / 2,
                        monheight - bottom_offset - square_side * y1 + square_side / 2, button='left')
        pyautogui.click(left_offset + square_side * x2 + square_side / 2,
                        monheight - bottom_offset - square_side * y2 + square_side / 2, button='left')
    else:
        pyautogui.click(monwidth - right_offset - square_side * x1 - square_side / 2,
                        top_offset + square_side * y1 - square_side / 2, button='left')
        pyautogui.click(monwidth - right_offset - square_side * x2 - square_side / 2,
                        top_offset + square_side * y2 - square_side / 2, button='left')


def write_digital_FEN():
    global written_digital_fen
    global stockfish_digital_fen
    written_digital_fen = written_real_fen
    stockfish_digital_fen = stockfish_real_fen
    written_digital_fen = written_digital_fen.replace('/', '')
    written_digital_fen = written_digital_fen.replace('8', 'XXXXXXXX')
    written_digital_fen = written_digital_fen.replace('7', 'XXXXXXX')
    written_digital_fen = written_digital_fen.replace('6', 'XXXXXX')
    written_digital_fen = written_digital_fen.replace('5', 'XXXXX')
    written_digital_fen = written_digital_fen.replace('4', 'XXXX')
    written_digital_fen = written_digital_fen.replace('3', 'XXX')
    written_digital_fen = written_digital_fen.replace('2', 'XX')
    written_digital_fen = written_digital_fen.replace('1', 'X')
    stockfish_digital_fen = stockfish_digital_fen.replace('/', '')
    stockfish_digital_fen = stockfish_digital_fen.replace('8', 'XXXXXXXX')
    stockfish_digital_fen = stockfish_digital_fen.replace('7', 'XXXXXXX')
    stockfish_digital_fen = stockfish_digital_fen.replace('6', 'XXXXXX')
    stockfish_digital_fen = stockfish_digital_fen.replace('5', 'XXXXX')
    stockfish_digital_fen = stockfish_digital_fen.replace('4', 'XXXX')
    stockfish_digital_fen = stockfish_digital_fen.replace('3', 'XXX')
    stockfish_digital_fen = stockfish_digital_fen.replace('2', 'XX')
    stockfish_digital_fen = stockfish_digital_fen.replace('1', 'X')

# Running commands
time_constraint = 0
screenshot()
write_FEN()
FEN_addition()

# Checks if it is your turn
while not player == move:
    old_fen = written_real_fen
    screenshot()
    write_FEN()

    if old_fen == written_real_fen:
        old_fen = written_real_fen
    else:
        player = move

# Finds best move
stockfish.set_fen_position(written_fen)
bestmove = stockfish.get_best_move()

# Sets x/y coordinates for mouse travel
x1 = (conversion(bestmove, 0))
y1 = (bestmove[1])
x2 = (conversion(bestmove, 2))
y2 = (bestmove[3])
move_mouse(x1, y1, x2, y2)

# Clicks extra option if move is promotion:
mousex = pyautogui.position()
mousey = mousex[1]
mousex = mousex[0]

if len(bestmove) > 4:
    if bestmove[4] == 'q':
        pyautogui.click(mousex, mousey, button='left')
    if bestmove[4] == 'n':
        pyautogui.click(mousex, mousey + square_side, button='left')
    if bestmove[4] == 'r':
        pyautogui.click(mousex, mousey + square_side * 2, button='left')
    if bestmove[4] == 'b':
        pyautogui.click(mousex, mousey + square_side * 3, button='left')

# Makes move in Stockfish and gets Stockfish FEN
stockfish.make_moves_from_current_position([bestmove])
stockfish_fen = (stockfish.get_fen_position())

# Decreases stockfish FEN to simply the piecedata
stockfishadd = stockfish_fen.find(' w ')

if stockfishadd < 0:
    stockfishadd = stockfish_fen.find(' b ')

stockfishadd = (stockfish_fen[stockfishadd:len(stockfish_fen)])
stockfish_real_fen = stockfish_fen.replace(stockfishadd, '')

# SHOULD BE OPPONENT TURN
while not keyboard.is_pressed('p'):
    screenshot()
    write_FEN()

    while stockfish_real_fen == written_real_fen:
        screenshot()
        write_FEN()

    # Given there has been a position change, retakes screenshot
    time.sleep(0.1)
    screenshot()
    write_FEN()
    write_digital_FEN()
    n = 0

    # To retry when there are weird exception FEN errors
    if len(written_digital_fen) == len(stockfish_digital_fen):
        for i in range(len(written_digital_fen)):
            if written_digital_fen[i] == stockfish_digital_fen[i]:
                n = n
            else:
                if written_digital_fen[i] == 'X':
                    num1 = str(8 - math.floor(i / 8))
                    letter1 = str(letters[i % 8])
                    n += 1
                else:
                    num2 = str(8 - math.floor(i / 8))
                    letter2 = str(letters[i % 8])
                    n += 1
    else:
        time.sleep(0.25)
        screenshot()
        write_FEN()
        write_digital_FEN()
        n = 0

        # To end when there are weird exception FEN errors
        if len(written_digital_fen) == len(stockfish_digital_fen):
            for i in range(len(written_digital_fen)):
                if written_digital_fen[i] == stockfish_digital_fen[i]:
                    n = n
                else:
                    if written_digital_fen[i] == 'X':
                        num1 = str(8 - math.floor(i / 8))
                        letter1 = str(letters[i % 8])
                        n += 1
                    else:
                        num2 = str(8 - math.floor(i / 8))
                        letter2 = str(letters[i % 8])
                        n += 1
        else:
            print('Something went wrong.')

    oppmove = (letter1 + num1 + letter2 + num2)

    if n > 3:
        if player == 'w':
            if stockfish_digital_fen[5] == written_digital_fen[7]:
                oppmove = 'e8g8'
            else:
                oppmove = 'e8c8'
        else:
            if stockfish_digital_fen[61] == written_digital_fen[63]:
                oppmove = 'e1g1'
            else:
                oppmove = 'e1c1'

    # Tries making move, if illegal, bot ends
    try:
        stockfish.make_moves_from_current_position([oppmove])
        time_constraint += 1
    except:
        # Maybe it's a promotion? (Last-ditch effort)
        try:
            if player == 'b':
                oppmove += 'Q'
            else:
                oppmove += 'q'

            stockfish.make_moves_from_current_position([oppmove])
            time_constraint += 1
        except:
            print('Your opponent seems to have made an illegal move,',
                  oppmove + '. Make sure move speed is set to "fast" and restart the bot.')
            sys.exit()

    # PLAYER'S TURN
    eval = str(stockfish.get_evaluation())
    print(eval[0])

    stockfish.set_elo_rating(a)

    if time_constraint < 8:
        bestmove = stockfish.get_best_move_time(100)
    else:
        bestmove = stockfish.get_best_move_time((timevar * 60000) / (random.randint(60, 200)))

    # Sets x/y coordinates for mouse travel
    x1 = (conversion(bestmove, 0))
    y1 = (bestmove[1])
    x2 = (conversion(bestmove, 2))
    y2 = (bestmove[3])
    move_mouse(x1, y1, x2, y2)

    # Clicks extra option if move is promotion:
    mousex = pyautogui.position()
    mousey = mousex[1]
    mousex = mousex[0]

    if len(bestmove) > 4:
        if bestmove[4] == 'q':
            pyautogui.click(mousex, mousey, button='left')
        if bestmove[4] == 'n':
            pyautogui.click(mousex, mousey + square_side, button='left')
        if bestmove[4] == 'r':
            pyautogui.click(mousex, mousey + square_side * 2, button='left')
        if bestmove[4] == 'b':
            pyautogui.click(mousex, mousey + square_side * 3, button='left')

    # Makes move in Stockfish and gets Stockfish FEN
    stockfish.make_moves_from_current_position([bestmove])
    stockfish_fen = (stockfish.get_fen_position())

    # Decreases stockfish FEN to simply the piecedata (in stockfish_real_fen)
    stockfishadd = stockfish_fen.find(' w ')

    if stockfishadd < 0:
        stockfishadd = stockfish_fen.find(' b ')

    stockfishadd = (stockfish_fen[stockfishadd:len(stockfish_fen)])
    stockfish_real_fen = stockfish_fen.replace(stockfishadd, '')

print('Process ended.')
