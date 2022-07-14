from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.210xc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/homework", methods=["POST"])
def homework_post():
    nickname_receive = request.form['nickname_give']
    comment_receive = request.form['comment_give']
    
    doc={'nickname':nickname_receive,
         'comment':comment_receive}

    db.fanusers.insert_one(doc)

    return jsonify({'msg': '저장 완료'})


@app.route("/homework", methods=["GET"])
def homework_get():
    users_list = list(db.fanusers.find({}, {'_id': False}))
    return jsonify({'users': users_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
