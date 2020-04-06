from flask import Flask, jsonify, abort, make_response, request, url_for, render_template
from flask_cors import CORS
import pymysql


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
CORS(app, supports_credentials=True)


@app.route("/login", methods=["POST"])
def login():
    if not request.form or "username" not in request.form or "password" not in request.form:
        abort(400)
    db = pymysql.connect(host="localhost", user="root", password="root", db="talent_bank", port=3306)
    cur = db.cursor()
    username = request.form["username"]
    password = request.form["password"]
    if username and password:
        sql1 = "select password from sys_user where username='%s';" % username
        cur.execute(sql1)
        try:
            passwd = cur.fetchall()[0][0]
            if passwd and passwd == password:
                res = jsonify({"success": 1, "message": "登录成功"})
            else:
                res = jsonify({"success": "0", "message": "用户名或密码错误"})
        except Exception as e:
            raise e
        finally:
            cur.close()
    else:
        res = jsonify({"success": "0", "message": "账号和密码不能为空"})

    return make_response(res)


@app.route("/register", methods=["POST"])
def register():
    if not request.form or "username" not in request.form or "password" not in request.form:
        abort(400)
    db = pymysql.connect(host="localhost", user="root", password="root", db="talent_bank", port=3306)
    cur = db.cursor()
    username = request.form["username"]
    password = request.form["password"]
    try:
        sql1 = "insert into sys_user(username,password) values('%s','%s')" % (username, password)
        cur.execute(sql1)
        res = jsonify({"success": 1, "message": "注册成功"})
    except Exception as e:
        raise e
    finally:
        cur.close()

    return make_response(res)


@app.route("/getHumans", methods=["POST"])
def gethumans():
    if request.form["user_id"] == "":
        sql = "select * from talents;"
    else:
        sql = "select * from talents where id = '%s'" % request.form["user_id"]
    db = pymysql.connect(host="localhost", user="root", password="root", db="talent_bank", port=3306)
    cur = db.cursor()
    try:
        cur.execute(sql)
        humans = cur.fetchall()
        res = jsonify({"success": 1, "message": "成功", "data": humans})
    except Exception as e:
        raise e
    finally:
        cur.close()

    return make_response(res)


@app.route("/create", methods=["POST"])
def create():
    in_name = request.form["name"]
    in_age = request.form["age"]
    in_gender = request.form["gender"]
    in_experience = request.form["experience"]
    in_appraise = request.form["appraise"]
    in_telephone = request.form["telephone"]
    sql = "insert into talents(name,age,gender,experience,appraise,telephone) values('%s','%s','%s','%s','%s','%s')" % (in_name, in_age, in_gender, in_experience, in_appraise, in_telephone)
    db = pymysql.connect(host="localhost", user="root", password="root", db="talent_bank", port=3306)
    cur = db.cursor()
    try:
        cur.execute(sql)
        res = jsonify({"success": 1, "message": "人才新建成功"})
    except:
        res = jsonify({"success": 0, "message": "人才新建失败"})
    finally:
        cur.close()

    return make_response(res)


if __name__ == "__main__":
    app.run(port=8081, debug=True)



