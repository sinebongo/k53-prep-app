import glob
import os

directory = r"c:\Users\kings\AppData\Roaming\Microsoft\Windows\Libraries\Downloads\K53PrepApp\K53PrepApp\frontend"
html_files = glob.glob(os.path.join(directory, "*.html"))

changes = 0
for file in html_files:
    # Read with utf-8-sig to handle BOM
    for enc in ['utf-8-sig', 'utf-8', 'latin-1']:
        try:
            with open(file, 'r', encoding=enc) as f:
                content = f.read()
            break
        except:
            continue

    original = content

    content = content.replace("K53 Prep Assistant", "Godu Godu Driving School")
    content = content.replace("K53 Learners License Prep", "Godu Godu Driving School")
    content = content.replace("#144bb8", "#c1272d")
    content = content.replace("'#144bb8'", "'#c1272d'")
    content = content.replace('"#144bb8"', '"#c1272d"')

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        changes += 1
        print(f"Updated: {os.path.basename(file)}")

print(f"\nTotal files changed: {changes}")

# Verify
for file in html_files:
    with open(file, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    if "#144bb8" in content or "K53 Prep Assistant" in content or "K53 Learners License Prep" in content:
        print(f"WARN: old branding still in {os.path.basename(file)}")
    if "Godu Godu" in content:
        print(f"OK: {os.path.basename(file)} has Godu Godu branding")
