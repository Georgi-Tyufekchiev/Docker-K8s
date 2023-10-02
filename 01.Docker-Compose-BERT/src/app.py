import flask
from bert_model import predict
from pymongo import MongoClient
from sentiment_classifier import SentimentClassifier
from transformers import BertTokenizer
import torch
app = flask.Flask(__name__, template_folder='templates')

mongo_client = MongoClient("db",27017)  
db = mongo_client.flask_db
classification = db.classify

MODEL_NAME = 'bert-base-cased'
tokenizer = BertTokenizer.from_pretrained("bert-base-cased")
MAX_LEN = 400
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = SentimentClassifier(2)
model = model.to(device)

class_names = ['positive', 'negative']
model.load_state_dict(torch.load("model/best_model_state.bin", map_location=torch.device(device)))
model.eval()

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
        result = predict(text,tokenizer,MAX_LEN,device,model,class_names)
        classification.insert_one({'text':text,"sentiment":result})
        return flask.render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()
