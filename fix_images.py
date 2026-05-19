import os

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix UGC paths that weren't base64 encoded
html = html.replace('ugc.production.linktr.ee/', './ugc.production.linktr.ee/')

# Force background image by injecting style
if 'background-image: url(' not in html:
    style_injection = "\n<style>body { background-image: url('./background.jpg') !important; background-size: cover; background-position: center; background-attachment: fixed; }</style>\n</head>"
    html = html.replace('</head>', style_injection)

# Ensure head_image.png is correct
# We already checked it was skipped, so it should be in there. 
# Just in case, replace any weird paths.
html = html.replace('assets/head_image.png', './assets/head_image.png')
html = html.replace('././assets', './assets')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed image links.")
