from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.sureleb.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# 오색조 멤버 구성 db 삽입
# arr = [{'name':"김연수", 'color':"검정"},
#        {'name':"정대신", 'color':"파랑"},
#        {'name':"정호준", 'color':"카키"},
#        {'name':"변다슬", 'color':"노랑"},
#        {'name':"오길환", 'color':"주황"}]
#
# for i in arr:
#     db.ProjectMembers.insert_one(i)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/searchMember', methods=["GET"])
def serchMember():
    members_list = list(db.ProjectMembers.find({}, {'_id': False}))
    return jsonify({'membersList':members_list})

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
    count = len(visitorbook_list) + 1;

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