from flask import Flask, render_template, request, jsonify
<<<<<<< HEAD
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.jnbuc2e.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('kakhi.html')

@app.route("/kakhi_cmt", methods=["POST"])
def web_kakhi_post():
    nick_receive = request.form['nick_give']
    comment_receive = request.form['comment_give']

    kakhi_list = list(db.kakhi_cmt.find({}, {'id': False}))
    count = len(kakhi_list) + 1;

    doc = {
        'num': count,
        'nick': nick_receive,
        'comment': comment_receive,
    }
    db.kakhi_cmt.insert_one(doc)

    return jsonify({'msg': '댓글이 달렸어요!'})

@app.route("/kakhi_cmt", methods=["GET"])
def web_kakhi_get():
    nick_list = list(db.kakhi_cmt.find({}, {'_id': False}))
    return jsonify({'nicks': nick_list})

@app.route("/kakhi_cmt/del", methods=["POST"])
def delete_comment():
    num_receive = request.form['num_give']
    db.kakhi_cmt.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)


=======
import random
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.j7axpsz.mongodb.net/cluster0?retryWrites=true&w=majority')
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

@app.route('/orange')
def orange():
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
>>>>>>> 3d7a4358b5c030b3a4b400ada8390c37e8a3bbeb
