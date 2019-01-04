from flask import current_app
from . import index_blu
from info import redis_store
from flask import render_template



@index_blu.route('/index')
def log():
    current_app.logger.debug("debug日志信息")
    #设置redis键值对数据
    redis_store.set("name","laowang")
    return 'index'

@index_blu.route('/')
def index():
    return render_template('news/index.html')

# @app.route('/index')
# def index():
#     return 'index'
