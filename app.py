from flask import Flask, jsonify, request, render_template
import requests
import json
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-comments')
def get_comments():
    yid = request.args.get("youtube-id")
    response = requests.get(f"https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResult=200&order=orderUnspecified&videoId={yid}&key=AIzaSyDCGCR-1-raEtVJ_5wzfo71pihzaLO09jE")
    response = response.json()
    return json.dumps(response)

    
if __name__ == '__main__':
    app.run(debug= True)