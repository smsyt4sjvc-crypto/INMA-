"""INMA mailer BACK v2 — full-bleed, two-column layout that reserves a clean
right-hand zone for USPS postage + address, and uses the left column well."""
from PIL import Image, ImageDraw, ImageFont
import os

OUTFIT = 'Outfit-Regular.ttf'   # variable font (weight axis)
DMSERIF = 'DMSerif-Regular.ttf'

DARK    = '#1C1A17'
CREAM   = '#F5F2ED'
GOLD    = '#B8941F'
GOLD_LT = '#D4A843'
WHITE   = '#FFFFFF'
DIM     = '#9A958E'
BODY    = '#E4DED2'

W, H = 2700, 1800
SPLIT = 1560            # left dark panel width (~58%)

def font(path, size, weight=None):
    f = ImageFont.truetype(path, size)
    try:
        if f.get_variation_axes() and weight is not None:
            f.set_variation_by_axes([weight])
    except (AttributeError, OSError):
        pass
    return f

def wrap(draw, text, fnt, maxw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

img = Image.new('RGB', (W, H), CREAM)
draw = ImageDraw.Draw(img)

# Left dark panel
draw.rectangle((0, 0, SPLIT, H), fill=DARK)
# Seam: gold rule
draw.rectangle((SPLIT, 0, SPLIT + 8, H), fill=GOLD)

MX = 130                 # left margin
CW = SPLIT - MX - 110    # content width inside dark panel (~1320)

# --- Logo + wordmark ---
try:
    logo = Image.open('/home/user/INMA-/bear-logo.jpg').convert('RGB')
    s = min(logo.size)
    logo = logo.crop(((logo.width-s)//2, (logo.height-s)//2,
                      (logo.width-s)//2+s, (logo.height-s)//2+s)).resize((230, 230), Image.LANCZOS)
    mask = Image.new('L', (230, 230), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, 230, 230), radius=30, fill=255)
    img.paste(logo, (MX, 120), mask)
except Exception as e:
    print('logo skip:', e)

f_brand = font(DMSERIF, 150)
draw.text((MX + 270, 150), 'INMA', font=f_brand, fill=GOLD)
f_tag = font(OUTFIT, 27, weight=600)
draw.text((MX + 276, 320), 'Y O U R   P E R S O N A L   A D V O C A T E', font=f_tag, fill=DIM)

# --- Divider ---
y = 420
draw.line((MX, y, MX + CW, y), fill='#3a352e', width=3)
y += 56

# --- Headline ---
f_head = font(OUTFIT, 86, weight=700)
draw.text((MX, y), 'Hire the right guy.', font=f_head, fill=WHITE); y += 100
draw.text((MX, y), 'The first time.', font=f_head, fill=GOLD); y += 128

# --- Body ---
f_body = font(OUTFIT, 35, weight=500)
body = ("I'm not a contractor — I'm your personal homeowner advocate. Like a buyer's "
        "agent for your project, I work for you, not the crew. Vetted local crews, "
        "fair-market pricing, no kickbacks. My fee comes out of the contract — "
        "deducted in front of you, never added on top.")
for line in wrap(draw, body, f_body, CW):
    draw.text((MX, y), line, font=f_body, fill=BODY); y += 52
y += 40

# --- QR + offer block (bottom of left panel) ---
qr_y = 1230
qr_size = 330
try:
    qr = Image.open('/home/user/INMA-/qr-welcome.png').convert('RGB').resize((qr_size, qr_size), Image.LANCZOS)
    pad = 22
    bg = Image.new('RGB', (qr_size+pad*2, qr_size+pad*2), WHITE)
    bg.paste(qr, (pad, pad))
    img.paste(bg, (MX, qr_y))
except Exception as e:
    print('qr skip:', e)

# Offer text to the right of the QR
ox = MX + qr_size + pad*2 + 46
f_scan = font(OUTFIT, 30, weight=600)
draw.text((ox, qr_y + 18), 'SCAN THIS CARD FOR', font=f_scan, fill=DIM)
f_off = font(OUTFIT, 96, weight=700)
draw.text((ox - 2, qr_y + 58), '20% OFF', font=f_off, fill=GOLD_LT)
f_off2 = font(OUTFIT, 44, weight=600)
draw.text((ox, qr_y + 172), 'a Home Tune-Up', font=f_off2, fill=WHITE)
f_inspect = font(OUTFIT, 28, weight=500)
draw.text((ox, qr_y + 238), 'Inspect · Seal · Clean · Report', font=f_inspect, fill=DIM)

# --- Footer contact (bottom of dark panel) ---
f_foot = font(OUTFIT, 38, weight=600)
draw.text((MX, H - 130), 'inmagent.com', font=f_foot, fill=WHITE)
pw = draw.textlength('(509) 251-7792', font=f_foot)
draw.text((MX + CW - pw, H - 130), '(509) 251-7792', font=f_foot, fill=GOLD)

# Right panel stays clean cream for POSTAGE INDICIA + RETURN + RECIPIENT ADDRESS + BARCODE.

img.save('back-v2.png', 'PNG', optimize=True)
print('saved back-v2.png', img.size)
