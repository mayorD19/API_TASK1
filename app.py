from flask import *
import json
from datetime import datetime


# initialization of an instance of the flask object
app = Flask(__name__)


@app.route("/api", methods=["GET"])
def home_page():
    # Getting the query parameters from the request
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    data_set = {"slack_name": slack_name,
                "current_day": datetime.utcnow().strftime('%A'),
                "utc_time": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC'),
                "Track": track,
                "github_file_url": "https://github.com/mayorD19/API_TASK1/blob/main/app.py",
                "github_repo_url": "https://github.com/mayorD19/API_TASK1",
                "status_code": 200}
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == "__main__":
    app.run()

