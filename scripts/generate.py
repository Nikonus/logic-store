from google import genai
import os
import subprocess
import datetime


client = genai.Client(api_key="YOUR_API_KEY")

# ------------------------------------------
# CONFIGURE GEMINI CLIENT
# ------------------------------------------
# Option 1 (recommended): Use environment variable GEMINI_API_KEY
# client = genai.Client()

# Option 2: Put API key directly here
client = genai.Client(api_key="AIzaSyAaBZkIP-qtsjnakKzTC3D8OCWfPfN6rbQ")


# ------------------------------------------
# AI LOGIC GENERATION FUNCTION
# ------------------------------------------
def ai_logic(lang):
    prompt = f"""
    Generate a complete {lang} program with a function named 'logic(n)'.
    Requirements:
    - logic(n) must transform the number in a unique, creative way.
    - Do NOT write explanations.
    - Output ONLY valid {lang} code.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()


# ------------------------------------------
# LANGUAGE CONFIGURATION
# ------------------------------------------
date = datetime.datetime.now().strftime("%Y_%m_%d")

langs = {
    "python": {"branch": "python-daily", "folder": "python", "ext": "py"},
    "js":     {"branch": "js-daily",     "folder": "js",     "ext": "js"},
    "cpp":    {"branch": "cpp-daily",    "folder": "cpp",    "ext": "cpp"},
}


# ------------------------------------------
# MAIN LOGIC LOOP
# ------------------------------------------
for lang, cfg in langs.items():

    code = ai_logic(lang)

    folder = cfg["folder"]
    ext = cfg["ext"]
    filename = f"{folder}/logic_{date}.{ext}"

    # Create folder if missing
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Save AI-generated code
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    # Git operations
    subprocess.run(f"git checkout {cfg['branch']}", shell=True)
    subprocess.run("git add .", shell=True)
    subprocess.run(f'git commit -m "AI auto {lang} logic {date}"', shell=True)
    subprocess.run("git push", shell=True)


print("\n✔ All AI logic generated with Gemini 2.5 Flash & pushed successfully!\n")
