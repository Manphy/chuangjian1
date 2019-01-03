from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config
import logging

# 只是申明了数据库对象，并没有真正初始化操作
db = SQLAlchemy()
# ３把redis数据库对象申明成全局变量
redis_store = None

def create_app(config_name):
    # 通过传入不同的配置名字，初始化其对应配置的应用实例
    #配置项目日志
    setup_log(config_name)
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    #  创建数据库对象，延迟加载，懒加载
    db.init_app(app)
    #     配置redis(懒加载）
    global redis_store
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST,port = config[config_name].REDIS_PORT)

#     开启ｃｓｒｆ保护
    CSRFProtect(app)
#     设置session保存配置
    Session(app)


    return app

def setup_log(config_name):
    "配置日志"

#     设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)
    #创建日志记录器，指明日志保存的路径，每个日志文件的最大大小，保存日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log",maxBytes=1024*1024*100,backupCount=10)
    #创建日志记录的格式，日志等级，输入日志信息的文件名，行数，日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    #为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormaatter(formatter)
    #为全局　日志工具对象（flask_app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)



