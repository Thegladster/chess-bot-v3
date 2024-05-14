<div align="center">
  <h1>♟️ Chess Bot v3 ♟️</h1>
  <p> <b>Note:</b> This project was designed for Windows OS users.</p>
<div align="left"> 
  
<details open>
<summary>Get Started</summary>

<h4>1. Quickstart</h4>

&nbsp;&nbsp;&nbsp;&nbsp;Download ZIP file of the repository. Make sure command prompt is in a [**Python>=3.8.0**](https://www.python.org/) environment.
  
  ```bash
  cd chess-bot-v3-master
  pip install -r requirements.txt
  ```

<h4>2. Modify the chessbot.py file.</h4>

&nbsp;&nbsp;&nbsp;&nbsp;**2a.** Download [**Stockfish>=16.1.0**](https://stockfishchess.org/download/) (preferably version AVX2 on Windows computers). Unzip the folder, and locate `stockfish-windows-x86-64-avx2.exe`. 

Replace line 24 of `chessbot.py` with `stockfish = Stockfish("path/to/stockfish-windows-x86-64-avx2.exe")`, but with the actual path to your local file (Right click on the `.exe` file and select 'Copy as Path').

Then, replace all the back slashes with _forward_ slashes.

```bash
# Example:
stockfish = Stockfish("C:/Users/user/Downloads/stockfish-windows-x86-64-avx2/stockfish/stockfish-windows-x86-64-avx2.exe")
```

&nbsp;&nbsp;&nbsp;&nbsp;**2b.** Download file [**best.pt**](https://drive.google.com/file/d/1qWDevhJstvmbeFPu9nRYgxwbgm6eo1My/view?usp=sharing) from Google Drive (filesize is too large for GitHub.) Copy the path to the `best.pt` file.

Replace line 38 of `chessbot.py` with `model = torch.hub.load('ultralytics/yolov5', 'custom', path='path/to/best.pt')`, but with the actual path to the `best.pt` file (Right click on the `.exe` file and select 'Copy as Path').

Then, once again, replace all the back slashes with forward slashes.

```bash
# Example:
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/user/best.pt')
```

&nbsp;&nbsp;&nbsp;&nbsp;**2c.** Change the variables `square_side`, `left_offset`, and `top_offset`. These will be used to accurately screenshot the board (Resulting screenshot should be just the board).

```bash
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

<h4>CJ will help me see what else to add to the [requirements.txt](https://github.com/Thegladster/chess-bot-v3/blob/master/requirements.txt) file because I don't really know.</h4>

After installing requirements, if command prompt is reopened, the folder has to be directed into to find the python code.

  ```bash
  cd chess-bot-v3-master
  python chessbot.py
  ```

</details>
<details>

<summary>Troubleshooting</summary>

<h4>1.</h4>

If you receive error `ModuleNotFoundError`, make sure that file [**requirements.txt**](https://github.com/Thegladster/chess-bot-v3/blob/master/requirements.txt) is uploaded to the directory,

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
