# Workshop with SQLite and Vector database
* [SQLite-vec](https://github.com/asg017/sqlite-vec)

## Install
Python
```
$pyenv uninstall 3.12.7
$PYTHON_CONFIGURE_OPTS="--enable-loadable-sqlite-extensions --enable-optimizations" pyenv install 3.12.7
```

Dependencies
```
$pip install -r requirements.txt
```

## Run demo
```
$export OPENAI_API_KEY=your api key
$python main.py
```

### References
* [vscode-sqlite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)
* [Problem on MacOS](https://alexgarcia.xyz/sqlite-vec/python#updated-sqlite)