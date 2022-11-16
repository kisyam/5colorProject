from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.j7axpsz.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/orange')
def home():
    return render_template('orange.html')

@app.route("/orange/save", methods=["POST"])
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

@app.route("/orange/show", methods=["GET"])
def comment_get():
    comment_list = list(db.orange.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route("/orange/delete", methods=["POST"])
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

@app.route('/yellow')
def getYellow():
    return render_template('yellow.html')


@app.route("/yellow/homework/click", methods=["POST"])
def remove_comment():
    num_receive = request.form['num_give']
    db.YellowVbook.update_one({'num': int(num_receive)},{'$set':{'click':1}})

    return jsonify({'msg': '삭제 완료!'})

@app.route("/yellow/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    visitorbook_list = list(db.YellowVbook.find({}, {'id':False}))
    count = len(visitorbook_list) + 1

    doc = {
        'num':count,
        'name':name_receive,
        'comment':comment_receive,
        'click':0
    }
    db.YellowVbook.insert_one(doc)

    return jsonify({'msg':'기록 완료!'})

@app.route("/yellow/homework", methods=["GET"])
def homework_get():
    visitor_list = list(db.YellowVbook.find({}, {'_id': False}))
    return jsonify({'visitorbooks':visitor_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)