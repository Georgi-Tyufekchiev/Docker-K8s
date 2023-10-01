import flask
from bert_model import predict

app = flask.Flask(__name__, template_folder='templates')


# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        text = flask.request.form['text']
        result = predict(text)
        return flask.render_template('main.html', result=result)


if __name__ == '__main__':
    app.run()
