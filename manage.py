from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from info import create_app,db
from config import config
import logging

# 创建app,并传入配置模式：development/production
app = create_app('development')
# Flask-script 添加扩展命令行
manager = Manager(app)
# 数据库迁移
Migrate(app,db)
manager.add_command('db',MigrateCommand)


# @app.route('/index')
# def index():
#
#     logging.debug("This is a debug log.")
#     logging.info("This is a info log.")
#     logging.warning("This is a warning log.")
#     logging.error("This is a error log.")
#     logging.critical("This is a critical log.")
#     return  "index"

if __name__ == '__main__':
    manager.run()