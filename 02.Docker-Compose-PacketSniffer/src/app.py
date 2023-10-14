import flask
from sniffer_start import capture_packets
import cfg
import mysql.connector 

class DBManager:
    def __init__(self, database='results', host="db", user="root", password_file=None):
        pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user, 
            password=pf.read(),
            host=host, # name of the mysql service as set in the docker compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        pf.close()
        self.cursor = self.connection.cursor()
    
    def populate_db(self,data):
        self.cursor.execute('DROP TABLE IF EXISTS results')
        self.cursor.execute('CREATE TABLE results (srcIP VARCHAR(20), dstIP VARCHAR(20), srcMAC VARCHAR(20), dstMAC VARCHAR(20))')
        sql = "INSERT INTO results (srcIP, dstIP, srcMAC, dstMAC) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (data['srcIP'], data['dstIP'], data['srcMAC'], data["dstMAC"]))
        self.connection.commit()
    
    def query_results(self):
        self.cursor.execute('SELECT * FROM results')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec
    
    def close_conn(self):
        self.connection.close()

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

@app.route('/insert_data', methods=["POST"])
def insert_data():
    conn = DBManager("/run/secrets/db-password")
    conn.populate_db(captured_packets)
    conn.close_conn()
    

if __name__ == '__main__':
    app.run()

