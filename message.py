#!/usr/bin/env python
# encoding: utf-8
"""
@author: dxy
"""
from flask import Flask
from flask import render_template  # 读取网页模板
from flask import request
from flask import redirect
from flask import url_for
import logging
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)

message_list = []
logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='message.log',
    filemode='a')


@app.route('/')
def message_view():
    return render_template('message_index.html', messages=message_list)


@app.route('/message/add', methods=['POST'])
def message_add():
    data = {'content': request.form.get('msg_post', '')}  # data是从前端获取的参数
    message_list.append(data)
    r = request.form.get('msg_post')
    logging.warning('用户输入的参数是：' + r)
    return redirect('/')  # redirect 参数是路由路径
    # return redirect(url_for('message_view')) # url_for 参数是路由函数的名字


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)
