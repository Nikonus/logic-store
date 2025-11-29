import os
import datetime
import random
import subprocess

# -------------------------
# Configuration
# -------------------------
LANG_OPTIONS = {
    "python": {
        "branch": "python-daily",
        "folder": "python",
        "ext": "py"
    },
    "js": {
        "branch": "js-daily",
        "folder": "js",
        "ext": "js"
    },
    "cpp": {
        "branch": "cpp-daily",
        "folder": "cpp",
        "ext": "cpp"
    }
}

print("Which language do you want to generate?")
print("1. Python\n2. JavaScript\n3. C++")
choice = input("Enter (1/2/3): ")

if choice == "1":
    lang = "python"
elif choice == "2":
    lang = "js"
elif choice == "3":
    lang = "cpp"
else:
    print("Invalid choice")
    exit()

config = LANG_OPTIONS[lang]

branch = config["branch"]
folder = config["folder"]
ext = config["ext"]

# -------------------------
# Generate file name
# -------------------------
date = datetime.datetime.now().strftime("%Y_%m_%d")
token = hex(random.getrandbits(32))[2:]   # unique token
filename = f"{folder}/logic_{date}_{token}.{ext}"

# -------------------------
# Switch branch
# -------------------------
subprocess.run(["git", "checkout", branch])

# -------------------------
# Create logic file
# -------------------------

if lang == "python":
    content = f"""# Auto-generated logic file
# Date: {date}
# Token: {token}

def unique_logic(x):
    v = x
    for i in range(len('{token}')):
        v = (v * 3 + i) ^ ord('{token}'[i % len('{token}')])
    return v

print(unique_logic(10))
"""

elif lang == "js":
    content = f"""// Auto-generated logic file
// Date: {date}
// Token: {token}

function uniqueLogic(n) {{
    let v = n;
    const token = "{token}";
    for (let i = 0; i < token.length; i++) {{
        v = (v * 5 + token.charCodeAt(i)) ^ i;
    }}
    return v;
}}

console.log(uniqueLogic(10));
"""

else:  # C++
    content = f"""// Auto-generated logic file
// Date: {date}
// Token: {token}

#include <bits/stdc++.h>
using namespace std;

int uniqueLogic(int n) {{
    int v = n;
    string token = "{token}";
    for (int i = 0; i < token.size(); i++) {{
        v = (v * 7 + token[i]) ^ i;
    }}
    return v;
}}

int main() {{
    cout << uniqueLogic(10);
}}
"""

# -------------------------
# Save file
# -------------------------
with open(filename, "w") as f:
    f.write(content)

# -------------------------
# Commit & push
# -------------------------
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Auto: {lang} logic {date} {token}"])
subprocess.run(["git", "push"])

print(f"\n✔ Logic file created: {filename}")
print("✔ Commit & push complete.")
