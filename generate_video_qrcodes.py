import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"E:\sem3\data science\seminar"
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "images")
os.makedirs(ASSETS_DIR, exist_ok=True)

# GitHub Repository Public Base URLs
GITHUB_USER = "gurup7029-coder"
REPO_NAME = "data-visualization-seminar"
PAGES_BASE = f"https://{GITHUB_USER}.github.io/{REPO_NAME}"

QR_DATA = [
    {
        "id": "qr_english_video",
        "title": "3D Cartoon English Video",
        "subtitle": "Scan to Watch Full 3D Presentation (English)",
        "url": f"{PAGES_BASE}/video-english.html",
        "filename": "qr_english_video.png",
        "fill_color": "#0f172a"
    },
    {
        "id": "qr_tanglish_video",
        "title": "Cartoon Tanglish Video",
        "subtitle": "Scan to Watch Seminar Video (Tanglish)",
        "url": f"{PAGES_BASE}/video-tanglish.html",
        "filename": "qr_tanglish_video.png",
        "fill_color": "#0f172a"
    },
    {
        "id": "qr_interactive_deck",
        "title": "Interactive Web Presentation",
        "subtitle": "Scan to Open Interactive Slide Deck on Mobile",
        "url": f"{PAGES_BASE}/",
        "filename": "qr_interactive_deck.png",
        "fill_color": "#0f172a"
    },
    {
        "id": "qr_ppt_download",
        "title": "PowerPoint File (.pptx)",
        "subtitle": "Scan to Download Full Seminar PPT Presentation",
        "url": f"{PAGES_BASE}/download-ppt.html",
        "filename": "qr_ppt_download.png",
        "fill_color": "#0f172a"
    },
    {
        "id": "qr_quiz",
        "title": "Interactive Seminar Quiz & QA",
        "subtitle": "Scan to Test Your Knowledge & View Live Score",
        "url": f"{PAGES_BASE}/quiz.html",
        "filename": "qr_quiz.png",
        "fill_color": "#0f172a"
    }
]

def generate_clean_qrcode(item):
    """
    Generates a pure, high-contrast, standards-compliant QR code with standard 4-module
    quiet zone. Decodable instantly by 100% of smartphone camera apps and QR scanners.
    """
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=12,
        border=4,
    )
    qr.add_data(item["url"])
    qr.make(fit=True)
    
    # Pure deep dark slate on clean white background for maximum contrast ratio (>15:1)
    qr_img = qr.make_image(fill_color=item["fill_color"], back_color="white").convert("RGB")
    
    output_path = os.path.join(ASSETS_DIR, item["filename"])
    qr_img.save(output_path, "PNG")
    print(f"[OK] Generated Clean QR Code ({qr_img.size[0]}x{qr_img.size[1]}px): {output_path} -> {item['url']}")

def main():
    print("--- Generating High-Contrast Standards-Compliant QR Codes ---")
    for item in QR_DATA:
        generate_clean_qrcode(item)
    print("All QR Codes generated successfully!")

if __name__ == "__main__":
    main()
