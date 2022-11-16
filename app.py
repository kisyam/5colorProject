from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.j7axpsz.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('orange.html')

@app.route("/teampj", methods=["POST"])
def comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    pw_receive = request.form['pw_give']

    count = random.uniform(1, 1000)

    doc = {
        'name' : name_receive,
        'comment': comment_receive,
        'pw': pw_receive,
        'num' : count,
        'done' : 0
    }
    db.orange.insert_one(doc)
    return jsonify({'msg': '응원 감사합니다'})

@app.route("/teampj", methods=["GET"])
def comment_get():
    comment_list = list(db.orange.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route("/comment/delete", methods=["POST"])
def comment_delete():
    deletepw_receive = request.form['deletepw_give']
    num_receive = request.form['num_give']
    doc = {
        'num': float(num_receive),
        'pw': deletepw_receive
    }

    gang = db.orange.find_one(doc)
    print(gang)
    if(gang == None):
        return jsonify({'msg' : '비밀번호 일치하지 않습니다'})
    else :
        db.orange.delete_one(gang)
    return jsonify({'msg': '삭제완료'})
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)