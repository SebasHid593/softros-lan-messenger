# build 83e26de5b5
# (auto) dd1728
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
