from flask import Flask, render_template, request, jsonify
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

