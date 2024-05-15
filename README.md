<div align="center">
  <h1>♟️ Chess Bot v3 ♟️</h1>
  
  **Note:** This project was designed for Windows OS users.

<div align="left">
<details open>
<summary><b>Get Started</b></summary>

<h4>1. Check Python version and install text editor</h4>

&nbsp;&nbsp;&nbsp;&nbsp;**a.** Download ZIP folder of the repository, and rename the ZIP folder to `chessbot`. 

Extract the files once renamed. Then open Command Prompt (Windows + R and type cmd). 

&nbsp;&nbsp;&nbsp;&nbsp;**b.** Make sure Command Prompt is in a [**Python>=3.8.0**](https://www.python.org/) environment.

To find python version, run this line in Command Prompt:

```bash
python --version
```
If python version is less than 3.8.0 or not installed at all, download Python [**here**](https://www.python.org/).

&nbsp;&nbsp;&nbsp;&nbsp;**c.** Download a text editor. I recommend [**Notepad++**](https://notepad-plus-plus.org/downloads/) (more user-friendly) or [**PyCharm Community Edition**](https://www.jetbrains.com/pycharm/download/?section=windows#section=windows) (specifically made for Python, and is harder to use).

<hr>

<h4>2. Install dependencies</h4>

By default, downloads are saved in the Downloads folder, so the following code would generally work for most computers. 

Simply copy this text into the text editor you downloaded in the previous step, and replace `user` with the username of the computer.

  ```bash
  cd C:\Users\user\Downloads\chessbot\chess-bot-v3-master
  pip install -r requirements.txt
  ```

If `chess-bot-v3-master` is _not_ in the downloads folder, refer to the 2nd issue in the Troubleshooting/FAQ section of this document.

<hr>

<h4>3. Install Stockfish and recognition model.</h4>

&nbsp;&nbsp;&nbsp;&nbsp;**a.** Open the file `chessbot.py` in your text editor.

&nbsp;&nbsp;&nbsp;&nbsp;**b.** Download the latest version of [**Stockfish**](https://stockfishchess.org/download/) (preferably version AVX2 on Windows computers). Extract all files.

&nbsp;&nbsp;&nbsp;&nbsp;**c.** If your Stockfish folder is in the 'Downloads' area of your computer, in your `chessbot.py` file (line 24), replace the `user` area with the username of the computer.

```python
stockfish = Stockfish("C:/Users/user/Downloads/stockfish-windows-x86-64-avx2/stockfish/stockfish-windows-x86-64-avx2.exe")
```

&nbsp;&nbsp;&nbsp;&nbsp;**d.** If the Stockfish folder is another directory, locate the `stockfish-windows-x86-64-avx2.exe` file within the folder (via search), copy the path, and replace the path in line 24.

**IMPORTANT:** Make sure that you replace all the back slashes with _forward slashes._

```python
stockfish = Stockfish("path/to/stockfish-windows-x86-64-avx2.exe")
```

&nbsp;&nbsp;&nbsp;&nbsp;**e.** Download file [**best.pt**](https://drive.google.com/file/d/1qWDevhJstvmbeFPu9nRYgxwbgm6eo1My/view?usp=sharing) from Google Drive (filesize is too large for GitHub.)

If your `best.pt` file is in the 'Downloads' area of your computer, in your `chessbot.py` file (line 38), replace the `user` area with the username of the computer.

```python
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/user/Downloads/best.pt')
```

&nbsp;&nbsp;&nbsp;&nbsp;**f.** If the `best.pt` file is another directory, locate the file (via search), copy the path, and replace the path in line 38.

**IMPORTANT:** Make sure that you replace all the back slashes with _forward slashes._

```python
model = torch.hub.load('ultralytics/yolov5', 'custom', path='path/to/best.pt')
```

Remember to save the file (Ctrl+S) once done.

<hr>

<h4>4. Find the dimensions of the chessboard.</h4>

&nbsp;&nbsp;&nbsp;&nbsp;**a.** Open chess.com, start a game, then abort it right away (to set the code up for accurate dimensions).

**IMPORTANT:** MAKE SURE YOUR CHESS WINDOW IS IN WINDOWED FULLSCREEN. If your chess window is in split screen mode, then it will _not_ be consistent.

Press the square on the top right of your window to enable Windowed Fullscreen. You can also press key `F11` to enable true Fullscreen, but keep in mind that when using the chess bot in the future, the window will always have to be true fullscreen or else the screenshot will not capture accurately.

Additionally, the chessboard location for playing vs a human and playing vs a computer are in **DIFFERENT SPOTS**. If you would like to use the bot against a computer, then you will have to use different measurements than the one you use for playing against a human.

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

**NOTE:** The file `screenshot.py` is simply for _testing_ if your dimensions of the chessboard are correct before running it on `chessbot.py`! It is _not_ the chessbot.

Change the variables `square_side`, `left_offset`, and `top_offset` (lines 7, 8, and 9).

```python
# Example (use your own dimensions):
left_offset = 564
top_offset = 255
square_side = 215
```

Make sure to save changes before running.

&nbsp;&nbsp;&nbsp;&nbsp;**e.** To run `screenshot.py`, edit the following command in your text editor:

```bash
cd C:\Users\user\Downloads\chessbot\chess-bot-v3-master
python screenshot.py
```

As we did in step 1, change the `user` field of the first line to your username.

If the right side of the chessboard is cropped, change the `square_side` variable in `screenshot.py` by 2 pixels. This will make the image slightly wider on the right and bottom side.

&nbsp;&nbsp;&nbsp;&nbsp;**f.** Once the output screenshot looks like how you want it to (all chess pieces on the board have a label around them, and only the chessboard is in frame, nothing else), open `chessbot.py` on your text editor.

Replace the variables on `left_offset`, `top_offset`, and `square_side` (lines 17, 18, and 19) with the numbers you used for `screenshot.py`.

After all that, the project should be ready to run.

<hr>

<h4>5. Running the project</h4>

&nbsp;&nbsp;&nbsp;&nbsp;Run the project whenever after inputting command,

  ```bash
  cd C:\Users\user\Downloads\chessbot\chess-bot-v3-master
  python chessbot.py
  ```

Obviously, change the `user` field of the first line to your computer's username.

If already in the folder's directory, only `python chessbot.py` has to be executed.

Be sure to reference 'Additional Info' and 'Troubleshooting/FAQ' for any issues. If you cannot find a solution, create an issue description in the main page.

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
  cd C:\Users\user\Downloads\chessbot\chess-bot-v3-master
  python chessbot.py
  ```

<h4>2.</h4> 

To raise or lower the engine's ELO (skill level), adjust variables `a` and `b` (lines 33 and 34).

```python
a = 2000
b = 2400
```

`a` represents the minimum elo, and `b` represents the maximum ELO; every move, it picks a random integer in between this range to vary the skill level.

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

<h4>2.</h4> If, when inputting this command into Command Prompt,

 ```bash
  cd C:\Users\user\Downloads\chessbot\chess-bot-v3-master
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

<h4>3.</h4> If the `torch` module is having trouble installing, install the CPU version instead through `pip`,

```bash
pip3 install torch torchvision torchaudio
```

If you have additional issues, create an issues post and a detailed description of the issue.
</details>
