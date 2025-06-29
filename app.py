import os
from flask import Flask, jsonify, render_template, request
import pandas as pd
import random

app = Flask(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), "heritage/data")

# Define expected columns in your app's internal schema:
EXPECTED_COLS = [
    "subject",
    "gesture",
    "color_palette",
    "emotion",
    "scene_subtext",
    "class_tension",
    "mode"
]

# Map each CSV file's columns to your internal expected columns
COLUMN_MAPS = {
    "sim.csv": {
        "subject": "subject",
        "gesture": "gesture",
        "color_palette": "color_palette",
        "emotion": "emotion",
        "scene_subtext": "scene_subtext",
        "class_tension": "class_tension",
        "mode": "mode"
    },
    "inheritance.csv": {
        "subject": "subject",
        "gesture": "gesture",
        "color_palette": "color_palette",
        "emotion": "emotion",
        "scene_subtext": "scene_subtext",
        "class_tension": "class_tension",
        "mode": "mode"
    },
    "casablanca.csv": {
        "subject": "character",
        "gesture": "gesture",
        "color_palette": "aesthetic_palette",
        "emotion": "emotional_tone",
        "scene_subtext": "subtext",
        "class_tension": "social_tension_score",
        # no 'mode' column, will be filled as filename
    },
    "la-regle.csv": {
        "subject": "character",
        "gesture": "gesture",
        "color_palette": "aesthetic_palette",
        "emotion": "emotional_tone",
        "scene_subtext": "subtext",
        "class_tension": "social_tension_score",
    },
    "tokyo-story.csv": {
        "subject": "character",
        "gesture": "gesture",
        "color_palette": "aesthetic_palette",
        "emotion": "emotional_tone",
        "scene_subtext": "subtext",
        "class_tension": "social_tension_score",
    },
    # Add more CSVs here similarly
}


def load_data(source):
    path = os.path.join(DATA_DIR, source)
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        df = pd.read_csv(os.path.join(DATA_DIR, "sim.csv"))  # fallback

    mapping = COLUMN_MAPS.get(source, None)
    if mapping:
        # Rename columns from CSV names to your internal names
        rename_map = {v: k for k, v in mapping.items() if v in df.columns}
        df = df.rename(columns=rename_map)

        # Add missing expected columns with default values if not present
        for col in EXPECTED_COLS:
            if col not in df.columns:
                # For mode, default to filename without .csv
                if col == "mode":
                    df[col] = source.replace(".csv", "")
                else:
                    df[col] = ""  # empty string default for others

        # Keep only expected columns in correct order
        df = df[EXPECTED_COLS]
    else:
        # If no mapping, assume CSV already matches expected cols or fallback
        for col in EXPECTED_COLS:
            if col not in df.columns:
                if col == "mode":
                    df[col] = source.replace(".csv", "")
                else:
                    df[col] = ""
        df = df[EXPECTED_COLS]

    return df

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

if __name__ == '__main__':
    app.run(debug=True)
