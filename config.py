
import redis


  # ０　创建配置类
class Config(object):
    """工程配置信息"""


    SECRET_KEY = "FHRFHTRndsnfeiuofetrij"


    # 数据库配置信息
    # 连接ｍｙｓｑｌ数据库配置     "mysql://root:密码ip:端口/数据库名称"
    SQLALCHEMY_DATABASE_URI="mysql://root:mysql@127.0.0.1:5000/test"
    # 开启数据库跟踪模式
    SQLALchemy_TRACK_MODIFICATIONS = False


    # redis数据库配置信息
    REDIS_HOST ="127.0.0.1"
    REDIS_PORT =6379

#     flask_session配置信息
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER =True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT,db=1)
    PERMANENT_SESSION_LIFETIME = 86400

#     默认日志等级
    LOG_LEVEL = logging.DEBUG



class DevelopmentConfig(Config):
    # 开发模式下的配置
    DEBUG =True


class ProductionConfig(Config):
    # 生产模式下的配置
    LOG_LEVEL = logging.ERROR


# 定义配置字典,给外界使用提供一个接口
config = {
    "development":DevelopmentConfig,
    "production":ProductionConfig
}