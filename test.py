import os
import re

# 📂 Current working directory
folder = "./questions"

# 🔍 Pattern: remove everything before "MIT18_02SC_"
pattern = re.compile(r"^[a-f0-9]+_MIT18_02SC_(.+)$", re.IGNORECASE)

for filename in os.listdir(folder):
    if not filename.lower().endswith(".pdf"):
        continue

    match = pattern.match(filename)
    if match:
        new_name = match.group(1)
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)

        # 🪄 Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")
