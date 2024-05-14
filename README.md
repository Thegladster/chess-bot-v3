<div align="center">
  <h1> Chess Bot v3 </h1>
  <p> <b>Note:</b> This project was designed for Windows OS users.</p>
<div align="left"> 
  
<details open>
<summary>Get Started</summary>
<br>
  
<h4>1.</h4>

Clone repo and install [`requirements.txt`](https://github.com/Thegladster/chess-bot-v3/blob/master/requirements.txt). Make sure command prompt is in a [**Python>=3.8.0**](https://www.python.org/) environment.
  
  ```bash
  git clone https://github.com/Thegladster/chess-bot-v3
  cd chess-bot-v3
  pip install -r requirements.txt
  ```

<h4>2.</h4>Modify the `chessbot.py` file.

After that, run the project whenever after inputting command,

  ```bash
  python chessbot.py
  ```

</details>
<details>
  
<summary>Additional Info</summary>
<br>

CJ will help me see what else to add to the [requirements.txt](https://github.com/Thegladster/chess-bot-v3/blob/master/requirements.txt) file because I don't really know.

After installing requirements and cloning the repository, if command prompt is reopened, the folder has to be directed into to find the python code.

  ```bash
  cd chess-bot-v3
  python chessbot.py
  ```

</details>
<details>

<summary>Troubleshooting</summary>

<h4>1.</h4> If after cloning repository, command prompt outputs this fatal error:

```bash
fatal: destination path 'chess-bot-v3' already exists and is not an empty directory.
```

Pull the repository instead of cloning it. The resulting code will look like

```bash
git init
git add *
git stash
git pull https://github.com/Thegladster/chess-bot-v3
cd chess-bot-v3
```

If you receive error `ModuleNotFoundError`, make sure that file [`requirements.txt`](https://github.com/Thegladster/chess-bot-v3/blob/master/requirements.txt) is uploaded to the directory,

```bash
pip install -r requirements.txt
```

</details>
