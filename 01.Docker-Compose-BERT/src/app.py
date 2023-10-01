import flask
from bert_model import predict
from pymongo import MongoClient

app = flask.Flask(__name__, template_folder='templates')

mongo_client = MongoClient("db",27017,username="admin",password="password",authSource="admin",authMechanism="SCRAM-SHA-256")  
db = mongo_client["admin"] 
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
        return flask.render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()
