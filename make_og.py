#!/usr/bin/env python3
"""og.png 1200×630 — charcoal×ember grill-slat art for Blacksheep Korean BBQ & Hotpot. Shop identity only, zero builder tokens."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "og.png")

def font(path_names, size):
    bases = ["/System/Library/Fonts/Supplemental/", "/System/Library/Fonts/"]
    for b in bases:
        for n in path_names:
            p = b + n
            if os.path.exists(p):
                try:
                    return ImageFont.truetype(p, size)
                except Exception:
                    pass
    return ImageFont.load_default()

f_word = font(["Arial Bold.ttf", "Helvetica.ttc"], 118)
f_sub  = font(["Arial Bold.ttf", "Helvetica.ttc"], 40)
f_line = font(["Arial.ttf", "Helvetica.ttc"], 26)
f_tag  = font(["Georgia Italic.ttf", "Georgia.ttf"], 34)

img = Image.new("RGB", (W, H), "#141110")
d = ImageDraw.Draw(img, "RGBA")

# vertical gradient wash toward ember at bottom-right
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(20 + 14 * t), int(17 + 8 * t), int(16 + 6 * t)))

# grill slats
for y in range(24, H, 26):
    d.line([(0, y), (W, y)], fill=(255, 90, 31, 14), width=3)

# ember radial glow top-right (concentric alpha ellipses)
for r, a in [(330, 26), (260, 34), (190, 44), (130, 56), (80, 70)]:
    d.ellipse((W - 120 - r, -r // 2 - 40, W - 120 + r, -r // 2 - 40 + 2 * r), fill=(255, 90, 31, a))

# gold broth line bottom-left glow
for r, a in [(240, 14), (160, 20), (90, 26)]:
    d.ellipse((-40 - r // 2, H - 90 - r, -40 + r * 2, H - 90 + r), fill=(239, 174, 58, a))

CREAM = (246, 239, 228, 255); MIST = (205, 194, 180, 255); EMBER = (255, 90, 31, 255); GOLD = (239, 174, 58, 255)

# ember dot + wordmark
d.ellipse((72, 150, 108, 186), fill=EMBER)
d.text((126, 96), "BLACKSHEEP", font=f_word, fill=CREAM)
d.text((76, 246), "KOREAN BBQ \u00b7 HOT POT", font=f_sub, fill=GOLD)

# tagline (their published slogan words)
d.text((76, 336), "\u201cSizzling grills. Bubbling broth.\nGood times around the table.\u201d", font=f_tag, fill=(246, 239, 228, 210))

# bottom facts line
d.line([(76, 520), (1124, 520)], fill=(246, 239, 228, 60), width=2)
d.text((76, 546), "All-you-can-eat  ·  Cottonwood Mall  ·  Albuquerque, NM  ·  (505) 407-2915", font=f_line, fill=MIST)

img.save(OUT, "PNG")
print("wrote", OUT, os.path.getsize(OUT), "bytes")
