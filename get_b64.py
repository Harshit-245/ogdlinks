import base64

svg = "<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'><filter id='noiseFilter'><feTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(#noiseFilter)'/></svg>"
encoded = base64.b64encode(svg.encode('utf-8')).decode('utf-8')

with open("b64.txt", "w") as f:
    f.write(encoded)
print("Base64 generated successfully")
