import os
import glob
import re

directory = r"c:\Users\kings\AppData\Roaming\Microsoft\Windows\Libraries\Downloads\K53PrepApp\K53PrepApp\frontend"
html_files = glob.glob(os.path.join(directory, "*.html"))
pattern = re.compile(r'<div class="w-10 h-10 bg-primary flex items-center justify-center[^>]*>K</div>')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = pattern.sub(r'<img src="img/logo.png" alt="Godu Godu Logo" class="h-10 w-auto object-contain rounded-custom" />', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
