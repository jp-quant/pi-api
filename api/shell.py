import subprocess
from flask import request, jsonify

def execute_shell_command(json_body):
    command = json_body.get('command')
    if not command:
        return jsonify({"error": "Command not provided"}), 400

    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return jsonify({"output": output})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Command execution failed: {str(e)}"}), 500
