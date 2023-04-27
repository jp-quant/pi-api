from flask import Flask, request, jsonify
from api import shell, logging

app = Flask(__name__)

@app.route('/shell', methods=['POST'])
def execute_shell_command():
    json_body = request.get_json()
    response = shell.execute_shell_command(json_body)
    logging.log_request(request, response)
    return response

@app.route('/logs', methods=['GET'])
def get_logs():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    logs = logging.get_logs(start_date, end_date)
    return jsonify(logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
