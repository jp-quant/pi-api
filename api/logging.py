import os
import json
from datetime import datetime

LOG_DIR = "logs/"

def log_request(request, response):
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    log_file = os.path.join(LOG_DIR, f"{timestamp}.log")
    log_data = {
        "timestamp": timestamp,
        "remote_addr": request.remote_addr,
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "json_body": request.get_json(),
        "response": response.json,
    }
    with open(log_file, "w") as f:
        f.write(json.dumps(log_data, indent=2))

def get_logs(start_date=None, end_date=None):
    log_files = os.listdir(LOG_DIR)
    logs = []

    for log_file in log_files:
        with open(os.path.join(LOG_DIR, log_file), "r") as f:
            log_data = json.load(f)

        log_timestamp = datetime.strptime(log_data["timestamp"], "%Y%m%d%H%M%S")

        if start_date and end_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

            if start_date <= log_timestamp <= end_date:
                logs.append(log_data)
        elif start_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")

            if start_date <= log_timestamp:
                logs.append(log_data)
        elif end_date:
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

            if log_timestamp <= end_date:
                logs.append(log_data)
        else:
            logs.append(log_data)

    return logs
