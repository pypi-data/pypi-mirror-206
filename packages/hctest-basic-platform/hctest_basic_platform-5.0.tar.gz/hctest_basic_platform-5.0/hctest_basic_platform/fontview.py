from flask import Flask, jsonify, request, render_template

from flask_cors import CORS
from sql_manage import SQLite3Helper

app = Flask(__name__, template_folder="templates", static_folder="layui")
CORS(app)  # 允许跨域访问


@app.route('/')
def index():
    return render_template('caseList.html')


@app.route('/addTestCase')
def add_testcase():
    return render_template('addTestCase.html')


@app.route('/updateTestCase/<int:n>')
def update_testcase(n):
    return render_template('updateTestCase.html', id=n)


if __name__ == '__main__':
    app.run(debug=True, port=80)
