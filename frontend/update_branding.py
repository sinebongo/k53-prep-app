import os
import glob
import re

directory = r"c:\Users\kings\AppData\Roaming\Microsoft\Windows\Libraries\Downloads\K53PrepApp\K53PrepApp\frontend"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace texts
    content = content.replace("K53 Prep Assistant", "Godu Godu Driving School")
    content = content.replace("K53 Learners License Prep", "Godu Godu Driving School")
    
    # Replace primary color
    content = content.replace("#144bb8", "#c1272d")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} HTML files.")
