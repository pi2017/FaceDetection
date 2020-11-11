

from os import listdir
from flask import Flask, render_template
from flask_caching import Cache

config = {
    "DEBUG": False,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 100
}


app = Flask(__name__, static_url_path='/static')
app.config.from_mapping(config)
cache = Cache(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/view/')
def get_pic():
    data = ['' + file for file in listdir('static')]
    return render_template('get_pic.html', data=data)


#if __name__ == '__main__':
 #  app.run()
