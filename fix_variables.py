import os

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the background CSS variable.
# Since the CSS was inlined, the --profileBackground variable might be pointing to a broken relative path.
# We override it at the :root level so it correctly loads background.jpg.
if '--profileBackground: url(' not in html or 'background.jpg' not in html:
    style_injection = "\n<style>:root { --profileBackground: url('./background.jpg') !important; }</style>\n</head>"
    html = html.replace('</head>', style_injection)

# 2. Fix adblocker blocking the YouTube thumbnail.
# The folder "ugc.production.linktr.ee" triggers some adblockers because it has "production.linktr.ee" in it.
# We change it to just point to the "ugc" folder we made earlier.
html = html.replace('./ugc.production.linktr.ee/', './ugc/')
html = html.replace('https://./ugc.production.linktr.ee/', './ugc/') # Fix the typo from earlier diff

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Applied variable and path fixes!")
