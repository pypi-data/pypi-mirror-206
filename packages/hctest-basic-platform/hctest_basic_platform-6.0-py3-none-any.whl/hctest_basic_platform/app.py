from flask import Flask, jsonify, request

from flask_cors import CORS
from sql_manage import SQLite3Helper
import site
import os
os.chdir(f'{site.getsitepackages()[-1]}/hctest_basic_platform')
app = Flask(__name__)
CORS(app)  # 允许跨域访问


@app.route("/testcase/manage/list", methods=["GET"])
def get_all_testcase():
    # 获取前端传递的参数
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)

    # 分页处理
    start = (page - 1) * limit
    end = start + limit
    db = SQLite3Helper("identifier.sqlite")
    all_ = db.select_data("TestCase", "*")
    # print(all_)
    # 获取符合条件的数据
    filtered_data = all_[start:end]
    # 构造返回结果
    result = {'code': 0, 'count': len(all_), 'data': filtered_data}

    # 返回 JSON 格式数据
    return jsonify(result)


# 根据 ID 查询数据
@app.route('/testcase/<int:n>', methods=['GET'])
def get_testcase(n):
    db = SQLite3Helper("identifier.sqlite")
    result = db.select_data("TestCase", "*", f"id={n}")
    if result:
        filtered_data = result[0]
        result = {'code': 0, 'data': filtered_data}
        return jsonify(result)
    else:
        return jsonify({'code': 1, 'msg': 'Not found'})


@app.route("/testcase/manage/add", methods=["POST"])
def add_testcase():
    db = SQLite3Helper("identifier.sqlite")
    db.insert_data("TestCase", request.json)

    result = {'code': 0, 'msg': "添加成功", 'data': ""}

    # 返回 JSON 格式数据
    return jsonify(result)


@app.route("/testcase/manage/update/<int:n>", methods=["POST"])
def update_testcase(n):
    db = SQLite3Helper("identifier.sqlite")
    db.update_data("TestCase", request.json, f"id={n}")
    result = {'code': 0, 'msg': "更新成功", 'data': ""}
    return jsonify(result)


@app.route("/testcase/manage/delete/", methods=["POST"])
def delete_testcase():
    db = SQLite3Helper("identifier.sqlite")
    n = request.json["id"]
    db.delete_data("TestCase", f"id={n}")
    result = {'code': 0, 'msg': "删除成功", 'data': ""}
    return jsonify(result)


@app.route("/testcase/manage/run", methods=["POST"])
def run_testcase():
    n = request.json

    result = tobe_case(n["data"])

    return jsonify(result)


def tobe_case(ids):
    import json
    db = SQLite3Helper("identifier.sqlite")
    all_data = list()
    for i in ids:
        data = db.select_data("TestCase", "*", f"id={i}")
        all_data.append(data[0])

    for i in all_data:

        i.pop("id")
        i.pop("number")
        i.pop("title")
        i.pop("created_at")
        i.pop("updated_at")
        i["url"] = i["path"]
        i.pop("path")

        for j in ["headers", "params", "json", "data"]:
            if i[j]:
                i[j] = json.loads(i[j])

    from run import RunData
    RunData.data = all_data

    import pytest
    import os
    pytest.main(["test_execute.py", '--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result/ -o ./allure_report/ --clean')
    os.system('allure open ./allure_report/')
    result = {'code': 0, 'msg': "运行成功", 'data': ""}

    return result


if __name__ == '__main__':
    app.run(debug=True)
