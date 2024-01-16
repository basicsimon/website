from flask import Flask, render_template,request
import json
app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/')
def hello_world2():
    data = "hello data"
    return render_template("blog.html", data=data)

@app.route("/user/<username>", methods=["GET","POST"])
def get_user(username):
    return"hello %s" % username

@app.route('/data', methods=["POST","GET"])
def test_world():
    #print(request.args)
    #print(request.args.get("a"),request.args.get("b"))
    #print(request.headers)
    #print(request.headers.get("User-Agent"))
    #print(request.data)
    #import json
    #print(json.loads(request.data))
    #print(request.cookies)
    #print(request.cookies.get("token"))
    print(request.form)
    print(request.form.get("username",request.form.get("password")))
    return 'success'

@app.route("/use_template")
def use_template():
    datas = [(1,"name1"),(2,"name2"),(3,"name3")]
    title="student info"
    return render_template("use_template.html",datas=datas,title=title)

def read_pvuv_data():
    data = []
    with open("./data/pvuv.txt") as fin:
        for line in fin:
            line = line[:-1]
            pdate, pv, uv = line.split("\t")
            data.append((pdate, pv, uv))
    return data

@app.route("/pvuv")
def pvuv():
    data = read_pvuv_data()
    return render_template("pvuv.html",data = data)

@app.route("/getjson")
def getjson():
    data = read_pvuv_data()
    return json.dumps(data)

if __name__ == '__main__':
    app.run()
