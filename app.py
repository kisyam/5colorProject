from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test01:sparta@cluster0.vmvppsv.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/parc", methods=["POST"])
def web_parc_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.parc.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num':count,
        'name':name_receive,
        'comment':comment_receive,
        'del':0
    }
    db.parc.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})

@app.route("/parc/del", methods=["POST"])
def web_parc_del():
    num_receive = request.form["num_give"]
    db.parc.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})

@app.route("/parc", methods=["GET"])
def web_parc_get():
    comment_list = list(db.parc.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
