
from flask import Flask, jsonify, request, render_template
import requests
import json
from utils.yt import *
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-comments')
def get_comments():
    yl = request.args.get("youtube-link")
    yid = get_video_id(yl, 1)
    process_comments(yl)

    # response = requests.get(f"https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResult=200&order=orderUnspecified&videoId={yid}&key=AIzaSyDCGCR-1-raEtVJ_5wzfo71pihzaLO09jE")
    # response = response.json()
    # return json.dumps(response)

    
if __name__ == '__main__':
    app.run(debug= True)