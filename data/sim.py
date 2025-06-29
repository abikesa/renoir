import csv
import random

# Parameters
N = 100  # number of rows to generate

# Define column headers
headers = [
    "id", "timestamp", "mode", "subject", "gesture", 
    "color_palette", "emotion", "scene_subtext", "class_tension"
]

# Sample options for random generation
modes = ["static", "dynamic"]
subjects = ["soldier", "mechanic", "lover", "hunter", "waitress", "actor", "dancer",
            "philosopher", "mother", "child", "bather", "aristocrat", "painter", "gardener", "servant"]
gestures = ["wait", "nod", "glance", "smile", "dance", "pause", "step", "stare", 
            "reach", "collapse", "turn", "kiss", "laugh", "sigh", "gesture"]
color_palettes = ["pink+white", "lavender+ivory", "gray+navy", "blue+grey", 
                  "olive+brown", "red+charcoal", "white+emerald", "marble+ash", 
                  "gold+coral", "teal+ochre", "copper+sky", "sepia+black", 
                  "yellow+cream", "rose+peach", "indigo+bronze"]
emotions = ["serenity", "love", "awe", "discomfort", "hope", "melancholy", 
            "tension", "despair", "bliss", "fatigue", "restlessness", 
            "tenderness", "contempt", "resentment", "joy"]
scene_subtexts = [
    "truth in disguise", "caressing the ordinary", "eyeing invisible lines", 
    "pretending to care", "waiting for permission", "the world still soft", 
    "performing charm", "spinning under sunlight", "serving without being seen", 
    "eternal joy", "time isn’t yours", "duty without love", "beauty hiding decay", 
    "bound by rules", "caught in breathless grace"
]

# Generate CSV rows
rows = []
for i in range(N):
    timestamp = f"{i//60:02}:{i%60:02}:00"
    row = [
        i,
        timestamp,
        random.choice(modes),
        random.choice(subjects),
        random.choice(gestures),
        random.choice(color_palettes),
        random.choice(emotions),
        random.choice(scene_subtexts),
        round(random.uniform(0.0, 1.0), 2)
    ]
    rows.append(row)

# Save to CSV
output_file = "sim.csv"
with open(output_file, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

output_file

