from . import passport_blu
from flask import current_app, jsonify
from flask import make_response
from flask import request

from info import constants
from info import redis_store
from info.utils.captcha.captcha import captcha
from info.utils.response_code import RET
from . import passport_blu

"""在 passport 目录下的 view.py 文件中添加获取验证码的路由 image_code
步骤：
获取参数
生成验证码
删除之前验证码并保存当前验证码
错误处理
响应返回
"""


@passport_blu.route('/image_code')
def get_image_code():
    """获取图片验证码的后端接口
    :return:
    """
    # １　获取到当前图片编号id
    code_id = request.args.get('code_id')
    # 2 生成验证码图片，验证码图片的真实值
    image_name, text, image_data = captcha.generate_captcha()

    try:
        redis_store.setex('ImageCode_' + code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        current_app.logger.error(e)
        return make_response(jsonify(errno=RET.DATAERR, errmsg='保存图片验证码失败'))


        # 返回验证码图片（返回的数据是二进制格式，不能兼容所有浏览器）
    resp = make_response(image_data)
    resp.headers['Content-Type'] = 'image/jpg'
    return resp
