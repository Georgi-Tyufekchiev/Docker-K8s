import flask
from bert_model import predict
from pymongo import MongoClient

app = flask.Flask(__name__, template_folder='templates')

mongo_client = MongoClient("db",27017)  
db = mongo_client.flask_db
classification = db.classify

try:
    mongo_client.admin.command('ismaster')
    print("Connected to MongoDB")
except Exception as e:
    print("MongoDB connection error:", str(e))

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('index.html'))

    if flask.request.method == 'POST':
        text = flask.request.form['text']
        result = predict(text)
        classification.insert_one({'text':text,"sentiment":result})
        all_sentiments = classification.find()
        return flask.render_template('index.html', result=all_sentiments)


if __name__ == '__main__':
    app.run()
