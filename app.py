import os
from flask import Flask, jsonify, render_template
import pandas as pd
import random

app = Flask(__name__)
data = pd.read_csv(os.path.join(os.path.dirname(__file__), "inheritance.csv"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/frame/<int:frame_id>')
def frame(frame_id):
    row = data.iloc[frame_id % len(data)]
    return jsonify(row.to_dict())

@app.route('/random')
def random_frame():
    row = data.sample(1).to_dict(orient='records')[0]
    return jsonify(row)

@app.route('/mode/<mode>')
def mode_view(mode):
    filtered = data[data['mode'] == mode].sample(1).to_dict(orient='records')[0]
    return jsonify(filtered)

@app.route('/scenario/<int:start_id>')
def scenario(start_id):
    frames = data.iloc[start_id:start_id + 5].to_dict(orient='records')
    return render_template('scenario.html', frames=frames)
