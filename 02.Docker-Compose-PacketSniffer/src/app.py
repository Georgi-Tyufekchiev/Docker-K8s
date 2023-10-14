import flask
from sniffer_start import capture_packets
import cfg

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=["GET"])
def index():
    return flask.render_template('index.html')

@app.route('/start_sniffing', methods=['POST'])
def start_sniffing():
    cfg.stop_capture_signal = False
    global captured_packets
    captured_packets = capture_packets()  
    return flask.redirect(flask.url_for('index'))

@app.route('/stop_sniffing', methods=['POST'])
def stop_sniffing():
    cfg.stop_capture_signal = True
    return flask.redirect(flask.url_for('index'))

@app.route('/view_results')
def view_results():
    return flask.render_template('results.html', packets=captured_packets)

@app.route('/clear_packets', methods=['POST'])
def clear_packets_route():
    global captured_packets
    captured_packets = []
    return flask.redirect(flask.url_for('index'))

if __name__ == '__main__':
    app.run()

