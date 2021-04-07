from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app, supports_credentials=True)

user_info = {'user': 'zhangsan', 'pwd': '123456'}

project_data = {
    'code': 1,
    'data': [{'title': '标题1', 'id': '1001'},
             {'title': '标题2', 'id': '1002'},
             {'title': '标题3', 'id': '1003'},
             {'title': '标题4', 'id': '1004'}],
    'msg': '四个项目'}

# 接口数据
interface_data = {
    '1001': {'code': 1,
             'data': [{'name': '登陆1001'},
                      {'name': '注册1001'}],
             'msg': '2个接口'},
    '1002': {'code': 1,
             'data': [{'name': '登陆1002'},
                      {'name': '注册1002'},
                      {'name': '贷款1002'}],
             'msg': '3个接口'},
    '1003': {'code': 1,
             'data': [{'name': '登陆1003'},
                      {'name': '注册1003'},
                      {'name': '下单1003'}],
             'msg': '3个接口'},
    '1004': {'code': 1,
             'data': [{'name': '登陆1004'},
                      {'name': '注册1004'},
                      {'name': '吃饭1004'},
                      {'name': '睡觉1004'}],
             'msg': '3个接口'}
}


# @app.route('/api/', methods=['get'])
# def index():
#     return render_template('index.html')


@app.route('/api/login', methods=['post'])
def login():
    data = request.form
    if user_info.get('user') == data.get('user') and user_info.get('pwd') == data.get('pwd'):
        return jsonify({'code': 1, 'data': None, 'msg': '成功'})
    else:
        return jsonify({'code': 0, 'data': None, 'msg': '密码有误'})


@app.route('/api/pro_list', methods=['get'])
def pro_list():
    return jsonify(project_data)


@app.route('/api/interface', methods=['post'])
def interface():
    inter_id = request.form.get('pro_id')
    if inter_id:
        res_data = interface_data.get(inter_id)
        if res_data:
            return jsonify(res_data)
        else:
            return jsonify({'code': 0, 'data': None, 'msg': '没有该项目'})
    else:
        return jsonify({'code': 0, 'data': None, 'msg': '请求参数不能为空'})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
