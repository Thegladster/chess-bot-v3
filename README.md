<div align="center">
  <h1>♟️ Chess Bot v3 ♟️</h1>
  
  **Note:** This project was designed for Windows OS users.
<div align="left"> 
  
<details open>
<summary><b>Get Started</b></summary>

<h4>1. Check Python version and install text editor</h4>

&nbsp;&nbsp;&nbsp;&nbsp;**a.** Download ZIP folder of the repository and extract the files once downloaded. Then open command prompt (Windows + R and type cmd). 

&nbsp;&nbsp;&nbsp;&nbsp;**b.** Make sure command prompt is in a [**Python>=3.8.0**](https://www.python.org/) environment.

To find python version, run this line in command prompt:

```bash
python --version
```
If python version is less than 3.8.0 or not installed at all, download Python [**here**](https://www.python.org/).

&nbsp;&nbsp;&nbsp;&nbsp;**c.** Download a text editor. I recommend [**Notepad++**](https://notepad-plus-plus.org/downloads/) (more user-friendly) or [**PyCharm Community Edition**](https://www.jetbrains.com/pycharm/download/?section=windows#section=windows) (specifically made for Python, is harder to use).

<hr>

<h4>2. Install dependencies.</h4>

By default, downloads are saved in the Downloads folder, so the following code would generally work for most computers. 

Simply copy this text into the text editor you downloaded in the previous step, and replace `user` with the username of the computer.

  ```bash
  cd C:\Users\user\Downloads\chess-bot-v3-master\chess-bot-v3-master
  pip install -r requirements.txt
  ```

If the following command leads to error,

```bash
The system cannot find the path specified.
```

find the `chess-bot-v3-master` folder, double click, find the secondary `chess-bot-v3-master` folder underneath, right-click the folder, and select 'Copy as Path'.

Run this code in command prompt, but replace line `path/to/chess-bot-v3-master` with the path you copied.

  ```bash
  cd path/to/chess-bot-v3-master
  pip install -r requirements.txt
  ```

<hr>

<h4>3. Modify the chessbot.py file.</h4>

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

Replace line 38 of `chessbot.py` with `model = torch.hub.load('ultralytics/yolov5', 'custom', path='path/to/best.pt')`, but with the actual path to the `best.pt` file (Right click on the `best.pt` file and select 'Copy as Path').

Then, once again, replace all the back slashes with forward slashes.

```python
# Example:
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/user/best.pt')
```

&nbsp;&nbsp;&nbsp;&nbsp;**2c.** Change the variables `square_side`, `left_offset`, and `top_offset`. These will be used to accurately screenshot the board (Resulting screenshot should be just the board).

```python
square_side = x
left_offset = y
top_offset = z
```

Make sure to save changes before running.

<h4>3. Running the project</h4>

Run the project whenever after inputting command,

  ```bash
  python chessbot.py
  ```

Be sure to reference 'Additional Info' and 'Troubleshooting' for any issues, or create an issue description in the main page.

</details>
<details>
  
<summary>Additional Info</summary>

<h4>please help me out here CJ</h4>

CJ will help me see what else to add to the [`requirements.txt`](https://github.com/Thegladster/chess-bot-v3/blob/master/requirements.txt) file because I don't really know yet, note add pyautogui

After installing requirements, if command prompt is reopened, the folder has to be directed into to find the python code.

  ```bash
  cd chess-bot-v3-master
  python chessbot.py
  ```

</details>
<details>

<summary>Troubleshooting</summary>

<h4>1.</h4>

If you receive error `ModuleNotFoundError`, make sure that file [`requirements.txt`](https://github.com/Thegladster/chess-bot-v3/blob/master/requirements.txt) is uploaded to the directory,

```bash
cd chess-bot-v3-master
pip install -r requirements.txt
```

Or try uploading yourself through `pip`, simply through

```bash
pip install [title]
```
with `title` being the name of the missing module.

</details>
