
## 🌀 RENDER DEPLOYMENT CHEATSHEET (Fractal Stack)

---

### 🌊 `.csv` — **Commons / Simulation**

**What to include in your repo** (your working directory = dataset)

✅ Files needed:

```txt
app.py
requirements.txt
render.yaml
inheritance.csv
/templates/
  ├── index.html
  └── scenario.html
```

❌ **ERROR**: *“TemplateNotFound” or file not read*

* **Fix**: Always place HTML files under `/templates`
* Use absolute-safe CSV loading:

  ```python
  import os
  pd.read_csv(os.path.join(os.path.dirname(__file__), "inheritance.csv"))
  ```

---

### ❤️ `.py` — **Methods / Boundaries**

✅ Your `app.py` must have:

* `Flask` routes
* Jinja rendering via `render_template()`
* `if __name__ == "__main__"` only for **local testing**

❌ **ERROR**: *“flask run” works locally, but breaks on Render*

* **Fix**: Render uses `gunicorn`. You need a `startCommand`.

---

### 🌀 `.jinja` — **Scenarios / Game Engine**

✅ Your app must include:

```bash
templates/
  scenario.html  ← includes {% for %}, {% if %}, etc.
```

* Use `/scenario/<int:id>` route to demonstrate recursion (Ukusoma)
* Render 3–5 frames at a time for loop effect

❌ **ERROR**: *“TemplateNotFound” or no dynamic HTML*

* **Fix**: Template folder MUST be named `templates/`
* Use `render_template('scenario.html', frames=frames)`

---

### 🐬 `.html` — **Results / Interface**

✅ `index.html` should:

* Call `/random`, `/mode/static`, `/mode/dynamic`
* Link to `/scenario/0` for full recursive experience

✅ Add gentle UI touches (font, spacing, emoji, warm palette)

❌ **ERROR**: *HTML shows but JS breaks*

* **Fix**: Ensure you're using `<script>` tags in the right place
* Check JS fetch paths (`/random`, `/mode/<mode>`) match routes

---

### 🔁 `.yaml` — **Render Deployment / Monopoly**

✅ `render.yaml`:

```yaml
services:
  - type: web
    name: renoir-engine
    env: python
    plan: free
    branch: main
    buildCommand: "pip install -r requirements.txt"
    startCommand: "gunicorn app:app"
    autoDeploy: true
```

✅ `requirements.txt`:

```txt
flask
pandas
gunicorn
```

❌ **ERROR**: *“App fails to build” or “no web service found”*

* **Fix**: You *must* include both `gunicorn` and a valid `render.yaml`
* App must expose `app = Flask(__name__)` and not wrap Flask in weird logic

---

## 📡 Mental Mnemonic: “YAML is the Remote CLI”

> Like a `.bashrc` for Render — encode your intentions once, never click again.

---

## 🧠 Optional Add-Ons

| Feature        | File                 | Fractal | Comment                        |
| -------------- | -------------------- | ------- | ------------------------------ |
| `/health`      | `app.py`             | ❤️      | Add a quick health check route |
| `/export.yaml` | scenario.js          | 🔁      | Export user sessions           |
| Dark Mode      | `index.html`         | 🐬      | Easier on the eyes             |
| Postgres       | `render.yaml`        | 🔁      | Add DB in 2 lines              |
| 404 page       | `templates/404.html` | ��      | Handle dead loops elegantly    |

---

## 🧪 Final Deploy Test

```bash
git init
git add .
git commit -m "deploy to Render"
git remote add origin https://github.com/your/repo
git push -u origin main
```

Then just go to [https://render.com](https://render.com) → connect repo → deploy 🎯

---

## Want Me To…

* Zip up the whole structure for drag-and-drop?
* Add error logging / exception handling?
* Turn this into a 2-player turn-based Renoir simulation?

Just say the word.

Until then:
🔁 **Deploy the illusion. Fork the inheritance. Push the recursion.**

