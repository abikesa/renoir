import os
from flask import Flask, jsonify, render_template
import pandas as pd
import random

# local: flask, remote: gunicorn
app = Flask(__name__)

# more dynamic data reading
DATA_DIR = os.path.join(os.path.dirname(__file__), "heritage/data")

def load_data(source):
    try:
        return pd.read_csv(os.path.join(DATA_DIR, source))
    except FileNotFoundError:
        return pd.read_csv(os.path.join(DATA_DIR, "sim.csv"))  # fallback

# routes to support source
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def index():
    source = request.args.get("source", "sim.csv")
    sources = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
    return render_template('index.html', sources=sources, current_source=source)

@app.route('/frame/<int:frame_id>')
def frame(frame_id):
    source = request.args.get("source", "sim.csv")
    data = load_data(source)
    row = data.iloc[frame_id % len(data)]
    return jsonify(row.to_dict())

@app.route('/random')
def random_frame():
    source = request.args.get("source", "sim.csv")
    data = load_data(source)
    row = data.sample(1).to_dict(orient='records')[0]
    return jsonify(row)

@app.route('/mode/<mode>')
def mode_view(mode):
    source = request.args.get("source", "sim.csv")
    data = load_data(source)
    filtered = data[data['mode'] == mode].sample(1).to_dict(orient='records')[0]
    return jsonify(filtered)

@app.route('/scenario/<int:start_id>')
def scenario(start_id):
    source = request.args.get("source", "sim.csv")
    data = load_data(source)
    frames = data.iloc[start_id:start_id + 5].to_dict(orient='records')
    return render_template('scenario.html', frames=frames)
