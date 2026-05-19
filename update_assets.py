import os
import re

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return

    original_content = content
    
    regex = re.compile(r'((?:href|src)\s*=\s*["\']|url\(\s*[\'"]?)(ugc\.production\.linktr\.ee|assets\.production\.linktr\.ee|assets|ugc)(/)')
    
    new_content = regex.sub(r'\1./\2\3', content)
    
    if new_content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.css', '.js', '.json', '.txt', '.php')):
            process_file(os.path.join(root, file))
