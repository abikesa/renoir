Love the energy! Here’s a sharp, polished README draft for your project that captures the vibe and the tech:

---

# Ukusoma Scenario Loop — The Inheritance Engine

> 🎥 **Explore cinematic narratives as living data**
> A dynamic Flask-powered storytelling dashboard driven by curated CSV “frames” from classic films.

---

## Overview

Ukusoma Scenario Loop is a lightweight but powerful storytelling engine that lets you **dive deep into cinematic worlds** via structured data. Each movie or scenario is represented as a CSV data source containing key “frames” — moments layered with mood, color palettes, tension, and narrative beats.

* Switch fluidly between multiple movies and story datasets
* Explore frames by mode (static/dynamic), grab random moments, or run scenario loops
* Visualize cinematic emotion, palette, gestures, and tension in a clean, elegant interface

The project’s name *Ukusoma* nods to recursive reading and immersive narrative looping — fitting for an app that redefines how you consume stories.

---

## Features

* **Multi-source CSV loading:** Easily add new films/scenarios as CSV files, all normalized to a shared schema
* **RESTful JSON API:** Fetch frames by ID, mode, or at random for frontend consumption
* **Dynamic Jinja templates:** Render frame details with mood palettes and emotional cues
* **Interactive UI:** Choose your film, load frames dynamically, and follow scenario loops seamlessly
* **Fallback logic:** Graceful handling of missing or invalid data sources with defaults

---

## Data Schema

All CSV data sources **must** adhere to this structure:

| Column          | Description                           |
| --------------- | ------------------------------------- |
| `id`            | Integer frame identifier              |
| `timestamp`     | Scene timestamp (HH\:MM\:SS)          |
| `mode`          | Narrative mode (`static`, `dynamic`)  |
| `subject`       | Key subject/character                 |
| `gesture`       | Action or gesture description         |
| `color_palette` | Color theme representing scene mood   |
| `emotion`       | Emotional tone                        |
| `scene_subtext` | Descriptive subtext or narrative note |
| `class_tension` | Numeric tension score (0.0 to 1.0)    |

---

## Installation

```bash
git clone https://github.com/abikesa/renoir.git
cd renoir
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## Usage

* Use the dropdown menu to select a film dataset (CSV)
* Click buttons to load static or dynamic frames or random scenes
* Follow links to scenario loops presenting recursive narrative frames

---

## Adding New Films / Data Sources

1. Create a new CSV in `heritage/data/` following the data schema above
2. The app automatically detects new `.csv` files
3. Select your new film from the dropdown to explore its frames

---

## Roadmap & Future Work

* Add richer UI animations & transitions
* Integrate soundscapes or music per scene
* Build AI-powered narrative branching and recommendations
* Support additional metadata fields & visualization options

---

## Credits

Built by Ikeremiba Elazum — blending cinematic art and data science to craft new narrative experiences.

 