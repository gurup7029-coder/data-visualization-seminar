import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"E:\sem3\data science\seminar"
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "images")
os.makedirs(ASSETS_DIR, exist_ok=True)

# GitHub Repository Public Base URLs
GITHUB_USER = "gurup7029-coder"
REPO_NAME = "data-visualization-seminar"
RAW_BASE = f"https://github.com/{GITHUB_USER}/{REPO_NAME}/raw/main"
PAGES_BASE = f"https://{GITHUB_USER}.github.io/{REPO_NAME}"

QR_DATA = [
    {
        "id": "qr_english_video",
        "title": "3D Cartoon English Video",
        "subtitle": "Scan to Watch Full 3D Cartoon Seminar (English)",
        "url": f"{PAGES_BASE}/video-english.html",
        "filename": "qr_english_video.png",
        "color": "#2563eb"  # Royal Blue
    },
    {
        "id": "qr_tanglish_video",
        "title": "Cartoon Tanglish Video",
        "subtitle": "Scan to Watch Seminar Video (Tanglish)",
        "url": f"{PAGES_BASE}/video-tanglish.html",
        "filename": "qr_tanglish_video.png",
        "color": "#7c3aed"  # Purple
    },
    {
        "id": "qr_interactive_deck",
        "title": "Interactive Web Presentation",
        "subtitle": "Scan to Open Interactive Slide Deck on Mobile",
        "url": f"{PAGES_BASE}/",
        "filename": "qr_interactive_deck.png",
        "color": "#0d9488"  # Teal
    },
    {
        "id": "qr_ppt_download",
        "title": "PowerPoint File (.pptx)",
        "subtitle": "Scan to Download Full Seminar PPT Presentation",
        "url": f"{PAGES_BASE}/download-ppt.html",
        "filename": "qr_ppt_download.png",
        "color": "#d97706"  # Amber
    }
]

def create_card_qrcode(item):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(item["url"])
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color=item["color"], back_color="white").convert("RGBA")
    qr_w, qr_h = qr_img.size

    # Card layout (600x720)
    card_w = 600
    card_h = 720
    card = Image.new("RGBA", (card_w, card_h), (255, 255, 255, 255))
    draw = ImageDraw.Draw(card)

    draw.rectangle([0, 0, card_w-1, card_h-1], outline=(226, 232, 240), width=4)
    draw.rectangle([0, 0, card_w, 16], fill=item["color"])

    try:
        title_font = ImageFont.truetype("arialbd.ttf", 30)
        sub_font = ImageFont.truetype("arial.ttf", 19)
        url_font = ImageFont.truetype("arial.ttf", 14)
    except:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
        url_font = ImageFont.load_default()

    draw.text((card_w // 2, 55), item["title"], fill=(15, 23, 42), font=title_font, anchor="mm")
    draw.text((card_w // 2, 98), item["subtitle"], fill=(100, 116, 139), font=sub_font, anchor="mm")

    qr_x = (card_w - qr_w) // 2
    qr_y = 140
    card.paste(qr_img, (qr_x, qr_y), qr_img)

    draw.rectangle([25, card_h - 90, card_w - 25, card_h - 35], fill=(241, 245, 249), outline=(203, 213, 225), width=1)
    
    # Display short URL label
    display_url = item["url"]
    if len(display_url) > 55:
        display_url = display_url[:52] + "..."
    draw.text((card_w // 2, card_h - 62), display_url, fill=(51, 65, 85), font=url_font, anchor="mm")

    output_path = os.path.join(ASSETS_DIR, item["filename"])
    card.convert("RGB").save(output_path, "PNG")
    print(f"[OK] Generated QR Code Card: {output_path}")

def main():
    print("--- Generating GitHub QR Codes for Videos, Web Deck & PPT ---")
    for item in QR_DATA:
        create_card_qrcode(item)
    print("All GitHub QR Code Cards generated successfully!")

if __name__ == "__main__":
    main()
