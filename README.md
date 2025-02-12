<div align="center">
  <h1>♟️ Chess Bot v3 ♟️</h1>
  
  By [gladdyator](https://github.com/Thegladster) and [lookxing](https://github.com/vLooking).
  
  **Note:** This project was designed for Windows OS users and operates on [**chess.com**](https://chess.com/).

  Additionally: this project is pretty old (and also kinda slow), and I don't condone cheating in any way. Use at your own risk.

<div align="left">
<details open>
<summary><b>Installation</b></summary>
<br>

> Make sure to follow the instructions **very** carefully. The installation process should take ~10-15 minutes if all steps are correctly done.
 
<h4>1. Download chessbot, check Python version and install text editor</h4>

&nbsp;&nbsp;&nbsp;&nbsp;**a.** Download ZIP folder of the repository (green code button, press `Download ZIP`), and **_rename the ZIP folder to `chessbot`_**. 

Extract the files once renamed.

&nbsp;&nbsp;&nbsp;&nbsp;**b.** Make sure Command Prompt is in a [**Python>=3.8.0**](https://www.python.org/) environment.

To find python version, run this line in Command Prompt:

```bash
python --version
```
If python version is less than 3.8.0 or not installed at all, download Python [**here**](https://www.python.org/).

&nbsp;&nbsp;&nbsp;&nbsp;**c.** Download a text editor. I recommend [**Notepad++**](https://notepad-plus-plus.org/downloads/) (more user-friendly) or [**PyCharm Community Edition**](https://www.jetbrains.com/pycharm/download/?section=windows#section=windows) (specifically made for Python, and is harder to use).

> By default, `.py` files will be opened in the application [**Notepad**](https://apps.microsoft.com/detail/9msmlrh6lzf3?hl=en-US&gl=US), but it is _not_ recommended to use because  it is deprecated, and there are much better options nowadays.

<hr>

<h4>2. Install dependencies</h4>

By default, downloads are saved in the Downloads folder, so the following code would generally work for most computers. 

  ```bash
  cd C:\Users\%username%\Downloads\chessbot\chess-bot-v3-master
  pip install -r requirements.txt
  ```

> If `chess-bot-v3-master` is _not_ in the downloads folder, refer to the 2nd issue in the Troubleshooting/FAQ section of this document.
> 
<hr>

<h4>3. Install Stockfish and recognition model.</h4>

&nbsp;&nbsp;&nbsp;&nbsp;**a.** Download the latest version of [**Stockfish**](https://stockfishchess.org/download/) (preferably version AVX2 on Windows computers). Extract all files.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Move the file to the `Downloads` area of your File Explorer (if it is not there already).

&nbsp;&nbsp;&nbsp;&nbsp;**b.** Download file [**best.pt**](https://drive.google.com/file/d/1qWDevhJstvmbeFPu9nRYgxwbgm6eo1My/view?usp=sharing) from Google Drive (filesize is too large for GitHub.)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Move the file to the `Downloads` area of your computer (if it is not there already).

<hr>

<h4>4. Find the dimensions of the chessboard.</h4>

&nbsp;&nbsp;&nbsp;&nbsp;**a.** Open chess.com, start a game, then abort it right away (to set the code up for accurate dimensions).

**IMPORTANT:** MAKE SURE YOUR CHESS WINDOW IS IN WINDOWED FULLSCREEN. If your chess window is in split screen mode, then it will _not_ be consistent.

Press the square on the top right of your window to enable Windowed Fullscreen. You can also press key `F11` to enable true Fullscreen, but keep in mind that when using the chess bot in the future, the window will always have to be true fullscreen or else _the screenshot will not capture accurately_.

> The chessboard location for playing vs a human and playing vs a computer are in **DIFFERENT SPOTS**. If you would like to use the bot against a computer, then you will have to use different measurements than the one you use for playing against a human.

&nbsp;&nbsp;&nbsp;&nbsp;**b.** Take three screenshots of your chess window.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **1.** the distance from the _left_ side of the chessboard to the _left_ side of the monitor.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **2.** the distance from the _top_ side of the chessboard to the _top_ of the monitor.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **3.** the size of _one_ chessboard square.

<img width="1500" alt="image" src="https://github.com/Thegladster/chess-bot-v3/assets/64565266/0c2abf3a-3392-4c94-938c-53679b9adc15">

&nbsp;&nbsp;&nbsp;&nbsp;**c.** Upload the images to an image measuring software, such as [**this**](https://tools.knowledgewalls.com/image-size-finder), and write down the:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **1.** width of the first image

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **2.** height of the second image

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **3.** width OR height (it doesn't matter because it should be a square).

&nbsp;&nbsp;&nbsp;&nbsp;**d.** Open `screenshot.py` from the extracted folder `chess-bot-v3-master`.

> The file `screenshot.py` is simply for _testing_ if your dimensions of the chessboard are correct before running it on `chessbot.py`! It is _not_ the chessbot.

Change the variables `square_side`, `left_offset`, and `top_offset` (lines 7, 8, and 9).

```python
# Example (use your own dimensions):
left_offset = 564
top_offset = 255
square_side = 215
```

> Make sure to save changes before running.

&nbsp;&nbsp;&nbsp;&nbsp;**e.** To run `screenshot.py`, run the following command in command prompt:

```bash
cd C:\Users\%username%\Downloads\chessbot\chess-bot-v3-master
python screenshot.py
```

If the right side of the chessboard is cropped, change the `square_side` variable in `screenshot.py` by 2 pixels. This will make the image slightly wider on the right and bottom side.

&nbsp;&nbsp;&nbsp;&nbsp;**f.** Once the output screenshot looks like how you want it to, (all 64 squares on the chessboard are perfectly seen and no pieces are cut off) open `chessbot.py` on your text editor.

Replace the variables on `left_offset`, `top_offset`, and `square_side` (lines 17, 18, and 19) with the numbers you used for `screenshot.py`.

**IMPORTANT**: Make sure to always save the python file after you make an edit! (`Ctrl+S`)

<hr>

<h4>5. Running the project</h4>

&nbsp;&nbsp;&nbsp;&nbsp;**a.** Change chess piece style to **Neo**. Follow [**these instructions**](https://support.chess.com/en/articles/8594320-how-do-i-change-my-background-board-and-pieces) in order to change the chess pieces. 

If the pieces are not Neo, the bot will be **unreliable** in its detection.

> By default, chess pieces should be **Neo**. This step can be skipped if you are using the default pieces.

&nbsp;&nbsp;&nbsp;&nbsp;**b.** Run the project whenever after inputting command,

  ```bash
  cd C:\Users\%username%\Downloads\chessbot\chess-bot-v3-master
  python chessbot.py
  ```

> Once edited, save the code into your text editor so you can copy and paste it into the command prompt whenever you need.

If already in the folder's directory, only `python chessbot.py` has to be executed.

If you want the chessbot to stop (as long as it is already moving the mouse for you), press the `p` key on your computer and hold it down until the process is aborted.

> Be sure to reference 'Additional Info' and 'Troubleshooting/FAQ' for further customization/inquiries. If you cannot find a solution to a problem in 'Troubleshooting/FAQ`, create an issue description in the main page.

</details>
<details>
  
<summary><b>Additional Info</b></summary>

<h4>1.</h4> To know if Command Prompt is already in the folder's directory, run the simple line

```bash
cd
```

and the output will be what directory (folder) Command Prompt is currently looking into.

After installing requirements, if Command Prompt is reopened, the folder has to be directed into to find the python code.

  ```bash
  cd C:\Users\%username%\Downloads\chessbot\chess-bot-v3-master
  python chessbot.py
  ```

Using just the line `python chessbot.py` will not work unless you are **already** in the `chess-bot-v3-master` directory!

<hr>

<h4>2.</h4> 

To raise or lower the engine's ELO (skill level), adjust variable `a` (line 34).

```python
a = 2500
stockfish.set_elo_rating(a)
```

<hr>

<h4>3.</h4>

Confused on the `Specify castling: [K/Q/k/q]:` input? This question simply asks if the king _can_ castle queenside or kingside. It does not matter what pieces are in the way.

Castling will normally always be KQkq (`K` representing kingside _white_ castling, `Q` representing queenside _white_ castling, `k` representing kingside _black_ castling, and `q` representing queenside _black_ castling). There are many exceptions, however.

&nbsp;&nbsp;&nbsp;&nbsp;**1.** The king has been moved. If the king has been moved in previous moves, the king for that color will _never_ be able to castle that round!

Example: if the white king moves up, then castling can only occur for the black side, and input would be `kq`.

&nbsp;&nbsp;&nbsp;&nbsp;**2.** The rook has moved. There are two rooks, the [**queenside rook and the kingside rook**](https://herculeschess.com/wp-content/uploads/2020/04/chess-side.gif). If the queenside rook for the black side moves, for instance, castling _cannot_ occur with that rook, meaning the input for the user would be `KQk` (assuming all other rooks and kings have remained stationary).

**IMPORTANT:** Make sure the input is always in the order `KQkq`! An input such as `kQKq` will be invalid.

<h4>4.</h4>

Want Stockfish to run faster (in exchange for your computer's resources?)

Uncomment line 43 to change Stockfish `Hash` and `Thread` values. By default, `Hash` = 16 and `Threads` = 1, but the higher the thread count, the stronger Stockfish will be.

**IMPORTANT:** `Threads` value should _never_ exceed the number of [**logical processors (cores)**](https://support.microsoft.com/en-us/windows/find-out-how-many-cores-your-processor-has-3126ef99-0247-33b3-81fc-065e9fb0c35b) on your computer. `Hash` value should stay about the same (it _has_ to be a multiple of 2<sup>x</sup>, e.g. 2, 4, 8, 16, 32, 64, etc.)

</details>
<details>

<summary><b>Troubleshooting/FAQ</b></summary>

<h4>1.</h4>

If you receive error `ModuleNotFoundError`, make sure that file [`requirements.txt`](https://github.com/Thegladster/chess-bot-v3/blob/master/requirements.txt) is uploaded to the directory,

```bash
cd C:\Users\user\Downloads\chessbot\chess-bot-v3-master
pip install -r requirements.txt
```

Or try uploading yourself through `pip`, simply through

```bash
pip install [title]
```

with `title` being the name of the missing module.

<hr>

<h4>2.</h4> If, when inputting this command into Command Prompt,

 ```bash
  cd C:\Users\%username%\Downloads\chessbot\chess-bot-v3-master
  pip install -r requirements.txt
  ```

the error arises,

```bash
The system cannot find the path specified.
```

find the `chessbot` folder, double click, find the `chess-bot-v3-master` folder underneath, right-click the folder, and select 'Copy as Path'.

Run this code in Command Prompt, but replace line `path/to/chess-bot-v3-master` with the path you copied.

  ```bash
  # Example
  cd path/to/chess-bot-v3-master
  pip install -r requirements.txt
  ```

<hr>

<h4>3.</h4> 

If the `torch` module is having trouble installing, install the CPU version instead through `pip`,

```bash
pip3 install torch torchvision torchaudio
```

<h4>4.</h4> If you recieve an error that your command isn't found,

```bash
Error: command not found.
```

Make sure that you are _not_ in a Python environment, by either closing out the command prompt tab and re-opening, or applying this line:

```bash
exit()
```

<h4>5.</h4> 

If you make an edit to the `chessbot.py` file and the result has not changed, try closing out command prompt and make sure that your changes have been saved in the text editor.

If you have additional issues, create an issues post and a detailed description of the issue.
</details>

<div align="center">
