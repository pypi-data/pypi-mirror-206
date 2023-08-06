# BottleCORS
CORS plugin for Bottle

## Installation
### Pip
```bash
```

### Source
```bash
wget https://raw.githubusercontent.com/thepure12/bottle-cors/main/src/bottle_cors/bottle_cors.py
```

## Usage
### Install Plugin
```python
from bottle import Bottle
from bottle_cors import EnableCors
app = Bottle()
plugin = EnableCors()
app.install(plugin)
```