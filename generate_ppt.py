"""
Data Visualization Seminar - PowerPoint Generator
Generates a professional, white-based PPTX with images, animations, and all topics.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt
from pptx.enum.dml import MSO_THEME_COLOR
import os

# ─── Path Setup ──────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR  = os.path.join(BASE_DIR, "assets", "images")
OUT_FILE = os.path.join(BASE_DIR, "Data_Visualization_Seminar.pptx")

def img(name):
    p1 = os.path.join(IMG_DIR, name)
    if os.path.exists(p1):
        return p1
    p2 = os.path.join(BASE_DIR, "video_assets", name)
    if os.path.exists(p2):
        return p2
    return None

# ─── Color Palette ────────────────────────────────────────────────────────────
WHITE       = RGBColor(0xFF, 0xFF, 0xFF)
OFF_WHITE   = RGBColor(0xF8, 0xFA, 0xFC)
LIGHT_BLUE  = RGBColor(0xEF, 0xF6, 0xFF)
LIGHT_PURPLE= RGBColor(0xF5, 0xF3, 0xFF)
LIGHT_TEAL  = RGBColor(0xF0, 0xFD, 0xFA)
LIGHT_ROSE  = RGBColor(0xFF, 0xF1, 0xF2)

BLUE        = RGBColor(0x25, 0x63, 0xEB)
PURPLE      = RGBColor(0x7C, 0x3A, 0xED)
TEAL        = RGBColor(0x0D, 0x94, 0x88)
ROSE        = RGBColor(0xE1, 0x1D, 0x48)
AMBER       = RGBColor(0xD9, 0x77, 0x06)
DARK        = RGBColor(0x0F, 0x17, 0x2A)
GRAY        = RGBColor(0x47, 0x55, 0x69)
LIGHT_GRAY  = RGBColor(0xE2, 0xE8, 0xF0)
MID_GRAY    = RGBColor(0x94, 0xA3, 0xB8)

# ─── Slide Dimensions (16:9 Widescreen) ──────────────────────────────────────
prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)

W = prs.slide_width
H = prs.slide_height

# ─── Helpers ─────────────────────────────────────────────────────────────────

def blank_slide():
    layout = prs.slide_layouts[6]  # blank
    return prs.slides.add_slide(layout)

def add_rect(slide, x, y, w, h, fill=WHITE, alpha=None, line_color=None, line_width=None):
    shape = slide.shapes.add_shape(1, x, y, w, h)  # MSO_SHAPE_TYPE.RECTANGLE = 1
    shape.line.fill.background() if line_color is None else None
    fill_elem = shape.fill
    fill_elem.solid()
    fill_elem.fore_color.rgb = fill
    if line_color:
        shape.line.color.rgb = line_color
        if line_width:
            shape.line.width = line_width
    else:
        shape.line.fill.background()
    return shape

def add_text(slide, text, x, y, w, h, size=20, bold=False, italic=False,
             color=DARK, align=PP_ALIGN.LEFT, font="Calibri", wrap=True):
    txb = slide.shapes.add_textbox(x, y, w, h)
    tf  = txb.text_frame
    tf.word_wrap = wrap
    p   = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txb

def add_title_block(slide, title, subtitle=None,
                    title_color=DARK, sub_color=GRAY,
                    x=Inches(0.6), y=Inches(1.2),
                    w=Inches(8), title_size=32, sub_size=16):
    add_text(slide, title, x, y, w, Inches(1.2),
             size=title_size, bold=True, color=title_color, font="Calibri Light")
    if subtitle:
        add_text(slide, subtitle, x, y + Inches(1.1), w, Inches(1.0),
                 size=sub_size, color=sub_color, font="Calibri")

def add_image_safe(slide, path, x, y, w, h=None):
    if path and os.path.exists(path):
        try:
            if h:
                slide.shapes.add_picture(path, x, y, w, h)
            else:
                slide.shapes.add_picture(path, x, y, w)
            return True
        except Exception as e:
            print(f"  [WARN] Could not add image {os.path.basename(path)}: {e}")
    return False

def add_accent_bar(slide, color, x=Inches(0), y=Inches(0), w=Inches(0.12), h=None):
    h = h or H
    add_rect(slide, x, y, w, h, fill=color)

def add_slide_number(slide, num, total, color=MID_GRAY):
    add_text(slide, f"{num:02d} / {total:02d}",
             W - Inches(1.4), H - Inches(0.45), Inches(1.2), Inches(0.35),
             size=10, color=color, align=PP_ALIGN.RIGHT, font="Calibri")

def add_footer_tag(slide, tag, color=BLUE, bg=LIGHT_BLUE):
    r = add_rect(slide, Inches(0.6), H - Inches(0.55), Inches(2.8), Inches(0.32), fill=bg)
    add_text(slide, tag,
             Inches(0.6), H - Inches(0.58), Inches(2.8), Inches(0.35),
             size=9, color=color, font="Calibri", bold=True, align=PP_ALIGN.CENTER)

def add_bullet_card(slide, x, y, w, h, header, bullets, accent=BLUE, bg=OFF_WHITE):
    add_rect(slide, x, y, w, h, fill=bg, line_color=LIGHT_GRAY, line_width=Pt(0.5))
    add_rect(slide, x, y, Inches(0.07), h, fill=accent)
    add_text(slide, header,
             x + Inches(0.2), y + Inches(0.18), w - Inches(0.3), Inches(0.4),
             size=13, bold=True, color=DARK, font="Calibri Light")
    ty = y + Inches(0.62)
    for b in bullets:
        add_text(slide, f"• {b}",
                 x + Inches(0.2), ty, w - Inches(0.3), Inches(0.35),
                 size=11, color=GRAY, font="Calibri")
        ty += Inches(0.32)

def add_code_box(slide, code, x, y, w, h):
    add_rect(slide, x, y, w, h, fill=DARK)
    add_text(slide, code, x + Inches(0.15), y + Inches(0.12),
             w - Inches(0.3), h - Inches(0.24),
             size=9.5, color=RGBColor(0xA5, 0xF3, 0xFC), font="Courier New")

def section_divider(slide, topic_num, topic_label, topic_title, accent):
    """Full-bleed colored section divider slide."""
    # Background gradient simulation with two rects
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    # Large colored square right side
    add_rect(slide, Inches(8.5), 0, Inches(4.83), H, fill=accent)
    # Topic pill
    # (tag_bg not used further, removed unused computation)
    add_text(slide, f"TOPIC {topic_num:02d}",
             Inches(0.7), Inches(2.3), Inches(2), Inches(0.45),
             size=11, bold=True, color=accent, font="Calibri", align=PP_ALIGN.LEFT)
    add_text(slide, topic_label,
             Inches(0.7), Inches(2.8), Inches(7.5), Inches(0.6),
             size=14, color=GRAY, font="Calibri Light")
    add_text(slide, topic_title,
             Inches(0.7), Inches(3.4), Inches(7.5), Inches(1.6),
             size=36, bold=True, color=DARK, font="Calibri Light")
    # Decorative circles on right panel - use semi-transparent white-ish ovals via light fill
    light_accent = RGBColor(
        min(255, int.from_bytes(bytes.fromhex(str(accent)[1:]), 'big') >> 16 & 0xFF | 0x60),
        min(255, int.from_bytes(bytes.fromhex(str(accent)[1:]), 'big') >> 8 & 0xFF | 0x60),
        min(255, int.from_bytes(bytes.fromhex(str(accent)[1:]), 'big') & 0xFF | 0x60),
    ) if False else RGBColor(0xE0, 0xE8, 0xFF)  # simpler approach below

    circle_positions = [
        (Inches(10.5), Inches(1.5), Inches(1.8)),
        (Inches(11.8), Inches(4.2), Inches(2.5)),
        (Inches(9.8),  Inches(5.8), Inches(1.2)),
    ]
    # Determine a lighter tint of the accent color by mixing with white
    from lxml import etree
    ns = 'http://schemas.openxmlformats.org/drawingml/2006/main'
    for cx, cy, cr in circle_positions:
        circ = slide.shapes.add_shape(9, cx - cr/2, cy - cr/2, cr, cr)  # oval
        circ.line.fill.background()
        # Use direct XML to set a white fill with alpha transparency
        sp_pr = circ._element.spPr
        # Remove existing fill
        for child in list(sp_pr):
            tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag
            if tag in ('solidFill', 'noFill', 'gradFill', 'pattFill'):
                sp_pr.remove(child)
        # Build: <a:solidFill><a:srgbClr val="FFFFFF"><a:alpha val="20000"/></a:srgbClr></a:solidFill>
        solid_el = etree.SubElement(sp_pr, f'{{{ns}}}solidFill')
        srgb_el  = etree.SubElement(solid_el, f'{{{ns}}}srgbClr')
        srgb_el.set('val', 'FFFFFF')
        alpha_el = etree.SubElement(srgb_el, f'{{{ns}}}alpha')
        alpha_el.set('val', '20000')   # 20% opacity → 80% transparent


# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE CONTENT DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════════════

TOTAL_SLIDES = 35

slides_data = []

def make_slide(builder_fn):
    slides_data.append(builder_fn)
    return builder_fn

def add_speaker_notes(slide, notes):
    try:
        slide.notes_slide.notes_text_frame.text = notes
    except Exception as e:
        pass

# ─── SLIDE 1 — Cover / Title ──────────────────────────────────────────────────
def build_cover(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    # Top accent strip
    add_rect(slide, 0, 0, W, Inches(0.08), fill=BLUE)
    # Dark panel on right
    add_rect(slide, Inches(8.5), 0, Inches(4.83), H, fill=DARK)

    # Presenter Info Card Box on right panel
    add_rect(slide, Inches(8.8), Inches(1.2), Inches(4.2), Inches(5.0), fill=WHITE, line_color=BLUE, line_width=Pt(1.5))
    add_text(slide, "SEMINAR PRESENTATION",
             Inches(9.0), Inches(1.5), Inches(3.8), Inches(0.4),
             size=10, bold=True, color=BLUE, font="Calibri", align=PP_ALIGN.CENTER)
    add_text(slide, "Subject: Essential of Data Science\nTopic: Data Visualization",
             Inches(9.0), Inches(2.0), Inches(3.8), Inches(0.8),
             size=13, bold=True, color=DARK, font="Calibri", align=PP_ALIGN.CENTER)
    add_text(slide, "Presented By:\nGuru Prakash A\nReg No: 25322011\nClass: II MCA\nDept of Computer Science & Applications",
             Inches(9.0), Inches(3.0), Inches(3.8), Inches(2.6),
             size=12, color=GRAY, font="Calibri", align=PP_ALIGN.CENTER)

    # Left content
    add_text(slide, "DATA SCIENCE SEMINAR PRESENTATION",
             Inches(0.7), Inches(1.4), Inches(7.5), Inches(0.5),
             size=11, bold=True, color=BLUE, font="Calibri", align=PP_ALIGN.LEFT)
    add_text(slide, "Mastering Advanced\nData Visualization\nin Python",
             Inches(0.7), Inches(2.0), Inches(7.5), Inches(2.2),
             size=40, bold=True, color=DARK, font="Calibri Light")
    add_text(slide, "Three-Dimensional Plotting  •  Geographic Data with Basemap  •  Visualization with Seaborn",
             Inches(0.7), Inches(4.5), Inches(7.5), Inches(0.6),
             size=12, color=GRAY, font="Calibri Light")

    # Topic badges
    badges = [("Topic 01", "3D Plotting", PURPLE, LIGHT_PURPLE),
              ("Topic 02", "Basemap", TEAL, LIGHT_TEAL),
              ("Topic 03", "Seaborn", ROSE, LIGHT_ROSE)]
    for i, (lbl, name, col, bg) in enumerate(badges):
        bx = Inches(0.7 + i * 2.55)
        add_rect(slide, bx, Inches(5.5), Inches(2.3), Inches(0.8), fill=bg,
                 line_color=col, line_width=Pt(0.75))
        add_text(slide, lbl, bx, Inches(5.52), Inches(2.3), Inches(0.28),
                 size=8, bold=True, color=col, font="Calibri", align=PP_ALIGN.CENTER)
        add_text(slide, name, bx, Inches(5.82), Inches(2.3), Inches(0.32),
                 size=11, bold=True, color=col, font="Calibri Light", align=PP_ALIGN.CENTER)

    add_slide_number(slide, n, TOTAL_SLIDES, color=WHITE)
    add_speaker_notes(slide, "Welcome to the seminar on Data Visualization presented by Guru Prakash A, Reg No: 25322011, II MCA.")

# ─── SLIDE 2 — Table of Contents ─────────────────────────────────────────────
def build_toc(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_rect(slide, 0, 0, W, Inches(0.06), fill=BLUE)
    add_text(slide, "Table of Contents",
             Inches(0.7), Inches(0.5), Inches(8), Inches(0.7),
             size=28, bold=True, color=DARK, font="Calibri Light")
    add_rect(slide, Inches(0.7), Inches(1.25), Inches(0.45), Inches(0.04), fill=BLUE)

    toc_items = [
        ("01", "Cover & Introduction", BLUE, "Slide 1"),
        ("02", "Datasets Used", BLUE, "Slides 3–4"),
        ("03", "Three-Dimensional Plotting in Matplotlib", PURPLE, "Slides 5–14"),
        ("04", "Geographic Data with Basemap", TEAL, "Slides 15–22"),
        ("05", "Visualization with Seaborn", ROSE, "Slides 23–33"),
        ("06", "Seaborn vs Matplotlib Comparison", AMBER, "Slides 34–35"),
    ]
    for i, (num, title, color, pages) in enumerate(toc_items):
        y = Inches(1.5 + i * 0.87)
        add_rect(slide, Inches(0.7), y, Inches(11.9), Inches(0.72),
                 fill=OFF_WHITE, line_color=LIGHT_GRAY, line_width=Pt(0.5))
        add_rect(slide, Inches(0.7), y, Inches(0.06), Inches(0.72), fill=color)
        add_text(slide, num, Inches(0.85), y + Inches(0.15), Inches(0.5), Inches(0.42),
                 size=16, bold=True, color=color, font="Calibri Light")
        add_text(slide, title, Inches(1.5), y + Inches(0.18), Inches(9.0), Inches(0.38),
                 size=13, bold=True, color=DARK, font="Calibri")
        add_text(slide, pages, Inches(10.8), y + Inches(0.18), Inches(1.8), Inches(0.38),
                 size=11, color=MID_GRAY, align=PP_ALIGN.RIGHT)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Data Visualization Seminar")

# ─── SLIDE 3 — Datasets Overview ─────────────────────────────────────────────
def build_datasets_overview(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_rect(slide, 0, 0, W, Inches(0.06), fill=BLUE)
    add_text(slide, "Datasets Used in This Seminar",
             Inches(0.7), Inches(0.5), Inches(10), Inches(0.65),
             size=26, bold=True, color=DARK, font="Calibri Light")
    add_text(slide, "Three real-world benchmark datasets are used across all visualizations:",
             Inches(0.7), Inches(1.2), Inches(10), Inches(0.5),
             size=13, color=GRAY, font="Calibri Light")

    cards = [
        ("🌸 Iris Dataset", PURPLE, LIGHT_PURPLE,
         "150 rows × 5 columns",
         ["sepal_length, sepal_width", "petal_length, petal_width", "species (setosa/versicolor/virginica)",
          "Source: R.A. Fisher, 1936", "Used in: Seaborn pairplots, 3D scatter"]),
        ("🍽️ Tips Dataset", TEAL, LIGHT_TEAL,
         "244 rows × 7 columns",
         ["total_bill, tip, sex", "smoker (Yes/No), day", "time (Lunch/Dinner)", "size (party size)",
          "Used in: Seaborn catplot, lmplot"]),
        ("✈️ Flights Dataset", ROSE, LIGHT_ROSE,
         "144 rows × 3 columns",
         ["year (1949–1960)", "month (Jan–Dec)", "passengers (count)",
          "Used in: Seaborn heatmap", "Used in: 3D surface plot"]),
    ]
    for i, (title, color, bg, subtitle, bullets) in enumerate(cards):
        x = Inches(0.6 + i * 4.25)
        add_rect(slide, x, Inches(1.85), Inches(4.0), Inches(5.0),
                 fill=bg, line_color=color, line_width=Pt(1.0))
        add_rect(slide, x, Inches(1.85), Inches(4.0), Inches(0.06), fill=color)
        add_text(slide, title, x + Inches(0.18), Inches(1.98), Inches(3.6), Inches(0.45),
                 size=14, bold=True, color=color, font="Calibri Light")
        add_text(slide, subtitle, x + Inches(0.18), Inches(2.48), Inches(3.6), Inches(0.35),
                 size=10, bold=True, color=DARK, font="Calibri")
        ty = Inches(2.9)
        for b in bullets:
            add_text(slide, f"▸  {b}", x + Inches(0.18), ty, Inches(3.6), Inches(0.32),
                     size=10, color=GRAY, font="Calibri")
            ty += Inches(0.38)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Datasets Overview", color=BLUE, bg=LIGHT_BLUE)

# ─── SLIDE 4 — Dataset Sample Values ─────────────────────────────────────────
def build_dataset_samples(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_rect(slide, 0, 0, W, Inches(0.06), fill=BLUE)
    add_text(slide, "Dataset Sample Values (First 5 Rows)",
             Inches(0.7), Inches(0.5), Inches(10), Inches(0.65),
             size=26, bold=True, color=DARK, font="Calibri Light")

    # Iris table
    add_text(slide, "🌸 Iris Dataset", Inches(0.7), Inches(1.3), Inches(5), Inches(0.4),
             size=13, bold=True, color=PURPLE, font="Calibri")
    iris_headers = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
    iris_rows = [
        ["5.1", "3.5", "1.4", "0.2", "setosa"],
        ["4.9", "3.0", "1.4", "0.2", "setosa"],
        ["4.7", "3.2", "1.3", "0.2", "setosa"],
        ["4.6", "3.1", "1.5", "0.2", "setosa"],
        ["5.0", "3.6", "1.4", "0.2", "setosa"],
    ]
    col_w = Inches(1.15)
    tx = Inches(0.7)
    ty = Inches(1.75)
    for j, h in enumerate(iris_headers):
        add_rect(slide, tx + j*col_w, ty, col_w, Inches(0.35), fill=PURPLE)
        add_text(slide, h, tx + j*col_w + Inches(0.05), ty + Inches(0.05),
                 col_w - Inches(0.1), Inches(0.28), size=9, bold=True,
                 color=WHITE, font="Calibri", align=PP_ALIGN.CENTER)
    for r, row in enumerate(iris_rows):
        bg = OFF_WHITE if r % 2 == 0 else WHITE
        for j, val in enumerate(row):
            add_rect(slide, tx + j*col_w, ty + (r+1)*Inches(0.32), col_w, Inches(0.32),
                     fill=bg, line_color=LIGHT_GRAY, line_width=Pt(0.3))
            add_text(slide, val, tx + j*col_w + Inches(0.05),
                     ty + (r+1)*Inches(0.32) + Inches(0.04),
                     col_w - Inches(0.1), Inches(0.25), size=9, color=DARK,
                     font="Calibri", align=PP_ALIGN.CENTER)

    # Tips mini-table (right side)
    add_text(slide, "🍽️ Tips Dataset (sample)", Inches(7.0), Inches(1.3), Inches(5.8), Inches(0.4),
             size=13, bold=True, color=TEAL, font="Calibri")
    tips_headers = ["total_bill", "tip", "sex", "smoker", "day", "time", "size"]
    tips_rows = [
        ["16.99", "1.01", "Female", "No", "Sun", "Dinner", "2"],
        ["10.34", "1.66", "Male", "No", "Sun", "Dinner", "3"],
        ["21.01", "3.50", "Male", "No", "Sun", "Dinner", "3"],
        ["23.68", "3.31", "Male", "No", "Sun", "Dinner", "2"],
        ["24.59", "3.61", "Female", "No", "Sun", "Dinner", "4"],
    ]
    col_w2 = Inches(0.82)
    tx2 = Inches(7.0)
    for j, h in enumerate(tips_headers):
        add_rect(slide, tx2 + j*col_w2, ty, col_w2, Inches(0.35), fill=TEAL)
        add_text(slide, h, tx2 + j*col_w2 + Inches(0.04), ty + Inches(0.05),
                 col_w2 - Inches(0.08), Inches(0.28), size=8, bold=True,
                 color=WHITE, font="Calibri", align=PP_ALIGN.CENTER)
    for r, row in enumerate(tips_rows):
        bg = OFF_WHITE if r % 2 == 0 else WHITE
        for j, val in enumerate(row):
            add_rect(slide, tx2 + j*col_w2, ty + (r+1)*Inches(0.32), col_w2, Inches(0.32),
                     fill=bg, line_color=LIGHT_GRAY, line_width=Pt(0.3))
            add_text(slide, val, tx2 + j*col_w2 + Inches(0.04),
                     ty + (r+1)*Inches(0.32) + Inches(0.04),
                     col_w2 - Inches(0.08), Inches(0.25), size=8, color=DARK,
                     font="Calibri", align=PP_ALIGN.CENTER)

    # Flights mini-table
    add_text(slide, "✈️ Flights Dataset (sample)", Inches(0.7), Inches(4.7), Inches(6), Inches(0.4),
             size=13, bold=True, color=ROSE, font="Calibri")
    fl_headers = ["year", "month", "passengers"]
    fl_rows = [("1949","January","112"), ("1949","February","118"),
               ("1949","March","132"), ("1949","April","129"), ("1949","May","121")]
    col_wf = Inches(1.5)
    txf = Inches(0.7)
    tyf = Inches(5.15)
    for j, h in enumerate(fl_headers):
        add_rect(slide, txf + j*col_wf, tyf, col_wf, Inches(0.35), fill=ROSE)
        add_text(slide, h, txf + j*col_wf + Inches(0.05), tyf + Inches(0.05),
                 col_wf - Inches(0.1), Inches(0.28), size=10, bold=True,
                 color=WHITE, font="Calibri", align=PP_ALIGN.CENTER)
    for r, row in enumerate(fl_rows):
        bg = OFF_WHITE if r % 2 == 0 else WHITE
        for j, val in enumerate(row):
            add_rect(slide, txf + j*col_wf, tyf + (r+1)*Inches(0.32), col_wf, Inches(0.32),
                     fill=bg, line_color=LIGHT_GRAY, line_width=Pt(0.3))
            add_text(slide, val, txf + j*col_wf + Inches(0.05),
                     tyf + (r+1)*Inches(0.32) + Inches(0.04),
                     col_wf - Inches(0.1), Inches(0.25), size=10, color=DARK,
                     font="Calibri", align=PP_ALIGN.CENTER)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Dataset Samples", color=BLUE, bg=LIGHT_BLUE)

# ─── SLIDE 5 — Section Divider: 3D Plotting ──────────────────────────────────
def build_3d_divider(slide, n):
    section_divider(slide, 1, "mpl_toolkits.mplot3d",
                    "Three-Dimensional\nPlotting in Matplotlib", PURPLE)
    add_slide_number(slide, n, TOTAL_SLIDES, color=WHITE)

# ─── SLIDE 6 — 3D Axes & Definitions ─────────────────────────────────────────
def build_3d_axes(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, PURPLE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=PURPLE)
    add_title_block(slide, "3D Axes & Coordinate Systems",
                    "Section 3.1 — mpl_toolkits.mplot3d projection registration",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    add_bullet_card(slide, Inches(0.7), Inches(2.2), Inches(5.5), Inches(4.2),
                    "Core Definitions",
                    ["mplot3d: Standard Matplotlib 3D toolkit (no pip install needed)",
                     "Registers 3D projection axes via fig.add_subplot(projection='3d')",
                     "Maps (x, y, z) data triples through rotation matrices",
                     "Supports elevation (elev) and azimuth (azim) camera angles",
                     "ax.set_xlabel / ylabel / zlabel for 3-axis labels"],
                    accent=PURPLE, bg=LIGHT_PURPLE)
    path = img("3d_axes.png")
    if not add_image_safe(slide, path, Inches(6.5), Inches(1.8), Inches(6.0), Inches(4.8)):
        add_rect(slide, Inches(6.5), Inches(1.8), Inches(6.0), Inches(4.8), fill=LIGHT_PURPLE)
        add_text(slide, "[3D Axes Output Image]", Inches(6.5), Inches(3.8), Inches(6.0), Inches(0.5),
                 size=12, color=PURPLE, align=PP_ALIGN.CENTER)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 01 · 3D Plotting", color=PURPLE, bg=LIGHT_PURPLE)

# ─── SLIDE 7 — Helix Scatter & Line Plot ─────────────────────────────────────
def build_3d_helix(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, PURPLE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=PURPLE)
    add_title_block(slide, "3D Helix — Scatter & Line Plot",
                    "Section 3.2 — ax.plot3D() and ax.scatter3D() with trigonometric spiral data",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    code = """import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(-4*np.pi, 4*np.pi, 150)
z = np.linspace(-2, 2, 150)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax = plt.axes(projection='3d')
ax.plot3D(x, y, z, 'grey')          # line
ax.scatter3D(x, y, z, c=z,         # scatter
             cmap='Blues')
plt.show()"""
    add_code_box(slide, code, Inches(0.7), Inches(2.2), Inches(5.8), Inches(4.4))
    path = img("3d_helix.png")
    if not add_image_safe(slide, path, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0)):
        add_rect(slide, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0), fill=LIGHT_PURPLE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 01 · 3D Plotting", color=PURPLE, bg=LIGHT_PURPLE)

# ─── SLIDE 8 — 3D Contour Plot ────────────────────────────────────────────────
def build_3d_contour(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, PURPLE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=PURPLE)
    add_title_block(slide, "3D Contour Plots (contour3D / contourf3D)",
                    "Section 3.3 — Sinusoidal surface projection with filled contours",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    add_bullet_card(slide, Inches(0.7), Inches(2.2), Inches(5.5), Inches(3.5),
                    "Key Points",
                    ["ax.contour3D() — Wireframe-style contour levels",
                     "ax.contourf3D() — Filled smooth gradient contours",
                     "Z = f(X,Y) — Must be a meshgrid-shaped 2D array",
                     "cmap param: 'viridis', 'plasma', 'coolwarm'",
                     "levels=40 controls number of contour bands"],
                    accent=PURPLE, bg=LIGHT_PURPLE)
    path = img("3d_contour.png")
    if not add_image_safe(slide, path, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0)):
        add_rect(slide, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0), fill=LIGHT_PURPLE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 01 · 3D Plotting", color=PURPLE, bg=LIGHT_PURPLE)

# ─── SLIDE 9 — Wireframe & Surface ───────────────────────────────────────────
def build_3d_wireframe(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, PURPLE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=PURPLE)
    add_title_block(slide, "Wireframe & Surface Plots",
                    "Section 3.4 — plot_wireframe() and plot_surface() with colormaps",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    code = """X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Wireframe
ax.plot_wireframe(X, Y, Z, color='black')

# Surface
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')"""
    add_code_box(slide, code, Inches(0.7), Inches(2.2), Inches(5.8), Inches(4.0))
    path = img("3d_wireframe_surface.png")
    if not add_image_safe(slide, path, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0)):
        add_rect(slide, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0), fill=LIGHT_PURPLE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 01 · 3D Plotting", color=PURPLE, bg=LIGHT_PURPLE)

# ─── SLIDE 10 — view_init Camera Control ─────────────────────────────────────
def build_3d_viewinit(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, PURPLE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=PURPLE)
    add_title_block(slide, "Camera Angle Control — view_init()",
                    "Section 3.5 — Elevation and Azimuth for perspective control",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    add_bullet_card(slide, Inches(0.7), Inches(2.2), Inches(5.5), Inches(4.2),
                    "view_init() Parameters",
                    ["ax.view_init(elev=30, azim=60)",
                     "elev: degrees above xy-plane (0° = flat, 90° = top-down)",
                     "azim: horizontal rotation angle (0°–360°)",
                     "Useful for creating animated GIFs by looping azim",
                     "Can be called in a loop for rotation animations",
                     "Default: elev=30, azim=-60 in most 3D plots"],
                    accent=PURPLE, bg=LIGHT_PURPLE)
    path = img("3d_view_init.png")
    if not add_image_safe(slide, path, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0)):
        add_rect(slide, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0), fill=LIGHT_PURPLE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 01 · 3D Plotting", color=PURPLE, bg=LIGHT_PURPLE)

# ─── SLIDE 11 — 3D Bar Chart ─────────────────────────────────────────────────
def build_3d_bar(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, PURPLE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=PURPLE)
    add_title_block(slide, "3D Bar Charts — bar3d()",
                    "Section 3.6 — Plotting categorical frequency data in 3D",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    code = """fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 1, 2, 3]
y = [1, 1, 1, 2, 2, 2]
z = [0, 0, 0, 0, 0, 0]
dx = dy = [0.5]*6
dz = [20, 35, 15, 10, 25, 30]

ax.bar3d(x, y, z, dx, dy, dz,
         color='royalblue', alpha=0.7)
ax.set_xlabel('X'); ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()"""
    add_code_box(slide, code, Inches(0.7), Inches(2.2), Inches(5.8), Inches(4.4))
    path = img("3d_bar.png")
    if not add_image_safe(slide, path, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0)):
        add_rect(slide, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0), fill=LIGHT_PURPLE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 01 · 3D Plotting", color=PURPLE, bg=LIGHT_PURPLE)

# ─── SLIDE 12 — 3D Triangulation ─────────────────────────────────────────────
def build_3d_triangulation(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, PURPLE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=PURPLE)
    add_title_block(slide, "3D Triangulated Surface — plot_trisurf()",
                    "Section 3.7 — Unstructured point-cloud surface rendering",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    add_bullet_card(slide, Inches(0.7), Inches(2.2), Inches(5.5), Inches(4.0),
                    "Triangulation Concepts",
                    ["plot_trisurf() — renders surface from scattered (x, y, z) points",
                     "Internally applies Delaunay triangulation algorithm",
                     "Ideal for non-uniform / irregular grid data",
                     "cmap controls color gradient along Z-axis",
                     "linewidth=0.2 adds subtle triangle edge lines",
                     "antialiased=False improves performance on large datasets"],
                    accent=PURPLE, bg=LIGHT_PURPLE)
    path = img("3d_triangulation.png")
    if not add_image_safe(slide, path, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0)):
        add_rect(slide, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0), fill=LIGHT_PURPLE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 01 · 3D Plotting", color=PURPLE, bg=LIGHT_PURPLE)

# ─── SLIDE 13 — 3D Iris Scatter ───────────────────────────────────────────────
def build_3d_iris(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, PURPLE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=PURPLE)
    add_title_block(slide, "3D Iris Species Scatter Plot",
                    "Section 3.8 — Dataset: Iris (150 rows) — 3 species in 3D feature space",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    code = """from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

iris = sns.load_dataset('iris')
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

species = iris['species'].unique()
colors = ['#4f46e5', '#0d9488', '#e11d48']
for sp, col in zip(species, colors):
    df = iris[iris['species'] == sp]
    ax.scatter(df['sepal_length'],
               df['petal_length'],
               df['petal_width'],
               c=col, label=sp, s=40)
ax.legend()
plt.show()"""
    add_code_box(slide, code, Inches(0.7), Inches(2.2), Inches(5.8), Inches(4.5))
    path = img("3d_iris.png")
    if not add_image_safe(slide, path, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0)):
        add_rect(slide, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0), fill=LIGHT_PURPLE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 01 · 3D Plotting", color=PURPLE, bg=LIGHT_PURPLE)

# ─── SLIDE 14 — 3D Flights Surface ────────────────────────────────────────────
def build_3d_flights(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, PURPLE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=PURPLE)
    add_title_block(slide, "3D Surface — Flights Passenger Traffic",
                    "Dataset: Flights (144 rows) — Year × Month passenger heatmap in 3D",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    code = """flights = sns.load_dataset('flights')
pivot = flights.pivot('month','year','passengers')

X = np.arange(len(pivot.columns))
Y = np.arange(len(pivot.index))
X, Y = np.meshgrid(X, Y)
Z = pivot.values

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z,
                cmap='plasma',
                edgecolor='none')
ax.set_xlabel('Year')
ax.set_ylabel('Month')
ax.set_zlabel('Passengers')
plt.show()"""
    add_code_box(slide, code, Inches(0.7), Inches(2.2), Inches(5.8), Inches(4.5))
    path = img("3d_flights_surface.png")
    if not add_image_safe(slide, path, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0)):
        add_rect(slide, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0), fill=LIGHT_PURPLE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 01 · 3D Plotting", color=PURPLE, bg=LIGHT_PURPLE)

# ─── SLIDE 15 — Section Divider: Basemap ─────────────────────────────────────
def build_basemap_divider(slide, n):
    section_divider(slide, 2, "mpl_toolkits.basemap / Cartopy",
                    "Geographic Data\nwith Basemap", TEAL)
    add_slide_number(slide, n, TOTAL_SLIDES, color=WHITE)

# ─── SLIDE 16 — What is Basemap? ─────────────────────────────────────────────
def build_basemap_intro(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, TEAL, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=TEAL)
    add_title_block(slide, "What is Basemap?",
                    "Section 4.1 — Geographic projections and map overlay for Python",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    add_bullet_card(slide, Inches(0.7), Inches(2.2), Inches(5.5), Inches(4.5),
                    "Definition & Purpose",
                    ["Basemap is a Matplotlib toolkit for geographic maps",
                     "Supports 25+ map projections (Mercator, Orthographic, Mollweide...)",
                     "Draws coastlines, country borders, rivers, parallels, meridians",
                     "Can overlay data points, filled regions, and contour lines",
                     "Installation: pip install basemap basemap-data-hires",
                     "Modern Alternative: Cartopy (actively maintained by Met Office)"],
                    accent=TEAL, bg=LIGHT_TEAL)
    # Show projection types
    projs = ["mill / Millerd Cylindrical", "ortho / Orthographic Globe",
             "moll / Mollweide Equal-Area", "lcc / Lambert Conformal Conic",
             "merc / Mercator (Web Standard)"]
    for i, p in enumerate(projs):
        add_text(slide, f"▸ {p}", Inches(6.8), Inches(2.5 + i*0.55), Inches(6.0), Inches(0.4),
                 size=11, color=TEAL, font="Calibri")
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 02 · Basemap", color=TEAL, bg=LIGHT_TEAL)

# ─── SLIDE 17 — Basemap Setup & Installation ─────────────────────────────────
def build_basemap_setup(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, TEAL, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=TEAL)
    add_title_block(slide, "Basemap Installation & Setup",
                    "Section 4.2 — Google Colab environment setup commands",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    code = """# Google Colab setup
!apt-get install -y libgeos-dev
!pip install basemap basemap-data-hires

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Create a basic world map
fig = plt.figure(figsize=(12, 8))
m = Basemap(projection='mill',
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180,
            resolution='c')

m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral',
                  lake_color='aqua')
m.drawparallels(np.arange(-90,90,30))
m.drawmeridians(np.arange(-180,180,60))
plt.title('World Map - Miller Cylindrical')
plt.show()"""
    add_code_box(slide, code, Inches(0.7), Inches(2.0), Inches(12.0), Inches(4.7))
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 02 · Basemap", color=TEAL, bg=LIGHT_TEAL)

# ─── SLIDE 18 — World Cities Map ─────────────────────────────────────────────
def build_basemap_cities(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, TEAL, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=TEAL)
    add_title_block(slide, "World Cities Population Map",
                    "Section 4.3 — Plotting city coordinates with population-scaled markers",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    add_bullet_card(slide, Inches(0.7), Inches(2.2), Inches(5.5), Inches(3.8),
                    "Cities Dataset Structure",
                    ["Latitude, Longitude coordinates for 20+ major cities",
                     "Population data (2020 estimates in millions)",
                     "m(lon, lat) → converts geographic to projected coords",
                     "plt.scatter(x, y, s=pop*10) → size ∝ population",
                     "plt.annotate() adds city name labels",
                     "Orthographic projection gives globe 3D effect"],
                    accent=TEAL, bg=LIGHT_TEAL)
    path = img("basemap_cities.png")
    if not add_image_safe(slide, path, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0)):
        add_rect(slide, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0), fill=LIGHT_TEAL)
        add_text(slide, "[World Cities Map Output]", Inches(6.5), Inches(3.8), Inches(6.3), Inches(0.5),
                 size=12, color=TEAL, align=PP_ALIGN.CENTER)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 02 · Basemap", color=TEAL, bg=LIGHT_TEAL)

# ─── SLIDE 19 — Great Circle Routes ──────────────────────────────────────────
def build_basemap_greatcircles(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, TEAL, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=TEAL)
    add_title_block(slide, "Great Circle Flight Routes",
                    "Section 4.4 — Shortest-path arcs on spherical Earth surface",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    code = """m = Basemap(projection='robin',
            lon_0=0, resolution='c')
m.drawcoastlines(linewidth=0.5)
m.fillcontinents(color='lightgray')
m.drawmapboundary(fill_color='#d0e8f8')

# Great Circle: NYC → London
m.drawgreatcircle(-74.0, 40.7,   # New York
                  -0.12, 51.5,   # London
                  linewidth=2, color='red',
                  label='NYC → LON')

# NYC → Tokyo
m.drawgreatcircle(-74.0, 40.7,
                  139.7, 35.7,
                  linewidth=2, color='blue',
                  label='NYC → TYO')
plt.legend()
plt.show()"""
    add_code_box(slide, code, Inches(0.7), Inches(2.2), Inches(5.8), Inches(4.5))
    path = img("basemap_greatcircles.png")
    if not add_image_safe(slide, path, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0)):
        add_rect(slide, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0), fill=LIGHT_TEAL)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 02 · Basemap", color=TEAL, bg=LIGHT_TEAL)

# ─── SLIDE 20 — Map Projections Explained ────────────────────────────────────
def build_basemap_projections(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, TEAL, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=TEAL)
    add_title_block(slide, "Map Projections Comparison",
                    "Section 4.5 — Tradeoffs between area, shape, and distance",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    projs = [
        ("Mercator (merc)", "Preserves angles/shapes. Area distortion near poles.", TEAL),
        ("Orthographic (ortho)", "Globe perspective view. Cannot show full sphere.", BLUE),
        ("Mollweide (moll)", "Equal-area. Distorts shapes but preserves areas.", PURPLE),
        ("Robinson (robin)", "Compromise — moderate area and shape distortion.", AMBER),
        ("Lambert Conformal (lcc)", "Used for regional maps. Preserves shape locally.", ROSE),
    ]
    for i, (name, desc, color) in enumerate(projs):
        y = Inches(2.2 + i * 0.95)
        add_rect(slide, Inches(0.7), y, Inches(12.0), Inches(0.82),
                 fill=LIGHT_TEAL if i % 2 == 0 else OFF_WHITE,
                 line_color=LIGHT_GRAY, line_width=Pt(0.5))
        add_rect(slide, Inches(0.7), y, Inches(0.06), Inches(0.82), fill=color)
        add_text(slide, name, Inches(0.85), y + Inches(0.1), Inches(3.5), Inches(0.35),
                 size=12, bold=True, color=color, font="Calibri")
        add_text(slide, desc, Inches(4.5), y + Inches(0.1), Inches(8.0), Inches(0.65),
                 size=11, color=GRAY, font="Calibri Light")
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 02 · Basemap", color=TEAL, bg=LIGHT_TEAL)

# ─── SLIDE 21 — Cartopy Alternative ──────────────────────────────────────────
def build_cartopy(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, TEAL, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=TEAL)
    add_title_block(slide, "Cartopy — Modern Basemap Alternative",
                    "Section 4.6 — Actively maintained library from the UK Met Office",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    code = """import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 1, 1,
     projection=ccrs.PlateCarree())

ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS,
               linestyle=':')
ax.add_feature(cfeature.OCEAN,
               facecolor='lightblue')
ax.add_feature(cfeature.LAND,
               facecolor='wheat')
ax.set_global()
ax.gridlines()
plt.title('World Map with Cartopy')
plt.show()"""
    add_code_box(slide, code, Inches(0.7), Inches(2.2), Inches(6.0), Inches(4.5))

    # Comparison table
    headers = ["Feature", "Basemap", "Cartopy"]
    rows = [("Status", "Deprecated (2020+)", "Actively Maintained"),
            ("Backend", "mpl_toolkits", "Shapely + Proj"),
            ("CRS Support", "25 projections", "Full EPSG registry"),
            ("OGC Services", "No", "Yes (WMS/WFS)")]
    col_ws = [Inches(2.2), Inches(1.8), Inches(1.8)]
    tx = Inches(7.2)
    ty = Inches(2.2)
    for j, h in enumerate(headers):
        x = tx + sum(col_ws[:j])
        add_rect(slide, x, ty, col_ws[j], Inches(0.38), fill=TEAL)
        add_text(slide, h, x + Inches(0.05), ty + Inches(0.06), col_ws[j] - Inches(0.1),
                 Inches(0.28), size=10, bold=True, color=WHITE, font="Calibri", align=PP_ALIGN.CENTER)
    for r, row in enumerate(rows):
        bg = LIGHT_TEAL if r % 2 == 0 else OFF_WHITE
        for j, val in enumerate(row):
            x = tx + sum(col_ws[:j])
            add_rect(slide, x, ty + (r+1)*Inches(0.5), col_ws[j], Inches(0.5),
                     fill=bg, line_color=LIGHT_GRAY, line_width=Pt(0.3))
            add_text(slide, val, x + Inches(0.05), ty + (r+1)*Inches(0.5) + Inches(0.1),
                     col_ws[j] - Inches(0.1), Inches(0.35), size=9, color=DARK, font="Calibri",
                     align=PP_ALIGN.CENTER)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 02 · Basemap", color=TEAL, bg=LIGHT_TEAL)

# ─── SLIDE 22 — Basemap Summary ───────────────────────────────────────────────
def build_basemap_summary(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, TEAL, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=TEAL)
    add_title_block(slide, "Basemap Topic Summary",
                    "Key takeaways from Geographic Data visualization",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    items = [
        ("🗺️ Projections", "25+ projections available; each has tradeoffs between area, shape, and distance preservation.", TEAL),
        ("📍 Data Overlay", "Convert lat/lon to projected (x,y) using m(lon, lat) before plotting.", BLUE),
        ("✈️ Great Circles", "drawgreatcircle() plots geodesic shortest paths on the spherical surface.", PURPLE),
        ("🌍 Cartopy", "Use Cartopy for modern projects — better OGC support and active maintenance.", ROSE),
    ]
    for i, (title, desc, color) in enumerate(items):
        y = Inches(2.3 + i * 1.15)
        add_rect(slide, Inches(0.7), y, Inches(12.0), Inches(1.0),
                 fill=LIGHT_TEAL if i % 2 == 0 else OFF_WHITE,
                 line_color=LIGHT_GRAY, line_width=Pt(0.5))
        add_rect(slide, Inches(0.7), y, Inches(0.06), Inches(1.0), fill=color)
        add_text(slide, title, Inches(0.85), y + Inches(0.12), Inches(2.5), Inches(0.4),
                 size=13, bold=True, color=color, font="Calibri Light")
        add_text(slide, desc, Inches(3.4), y + Inches(0.18), Inches(9.0), Inches(0.65),
                 size=12, color=GRAY, font="Calibri Light")
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 02 · Basemap", color=TEAL, bg=LIGHT_TEAL)

# ─── SLIDE 23 — Section Divider: Seaborn ─────────────────────────────────────
def build_seaborn_divider(slide, n):
    section_divider(slide, 3, "Statistical Data Visualization",
                    "Visualization with\nSeaborn", ROSE)
    add_slide_number(slide, n, TOTAL_SLIDES, color=WHITE)

# ─── SLIDE 24 — Seaborn Introduction ─────────────────────────────────────────
def build_seaborn_intro(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, ROSE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=ROSE)
    add_title_block(slide, "What is Seaborn?",
                    "Section 5.1 — High-level statistical data visualization built on Matplotlib",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    add_bullet_card(slide, Inches(0.7), Inches(2.2), Inches(5.5), Inches(4.5),
                    "Core Features",
                    ["Built on top of Matplotlib; uses Axes internally",
                     "Native Pandas DataFrame integration (x='col', hue='group')",
                     "Automatic KDE, regression lines, and confidence intervals",
                     "Beautiful default color palettes (muted, deep, pastel...)",
                     "Grid-level plots: FacetGrid, PairGrid for multi-panel figures",
                     "Functions: histplot, kdeplot, scatterplot, jointplot, pairplot"],
                    accent=ROSE, bg=LIGHT_ROSE)
    # Quick comparison
    add_text(slide, "sns.histplot() vs plt.hist()",
             Inches(6.8), Inches(2.2), Inches(6.0), Inches(0.45),
             size=13, bold=True, color=ROSE, font="Calibri Light")
    snippets = [
        ("Matplotlib (manual KDE):",
         "plt.hist(data, bins=30, density=True)\nfrom scipy.stats import gaussian_kde\nkde = gaussian_kde(data)\n..."),
        ("Seaborn (one line!):",
         "sns.histplot(data, kde=True, bins=30)"),
    ]
    ty = Inches(2.75)
    for label, code in snippets:
        add_text(slide, label, Inches(6.8), ty, Inches(6.0), Inches(0.3),
                 size=10, bold=True, color=GRAY, font="Calibri")
        add_code_box(slide, code, Inches(6.8), ty + Inches(0.32), Inches(6.0), Inches(0.85))
        ty += Inches(1.4)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 03 · Seaborn", color=ROSE, bg=LIGHT_ROSE)

# ─── SLIDE 25 — Histogram & KDE ──────────────────────────────────────────────
def build_seaborn_hist_kde(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, ROSE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=ROSE)
    add_title_block(slide, "histplot & kdeplot — Distributions",
                    "Section 5.2 — Dataset: Tips (244 rows) — total_bill distribution",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    code = """import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# Histogram with KDE overlay
fig, axes = plt.subplots(1, 2,
                          figsize=(12, 5))

# histplot with KDE
sns.histplot(data=tips, x='total_bill',
             kde=True, bins=30,
             color='#e11d48',
             ax=axes[0])
axes[0].set_title('Histogram + KDE')

# Pure KDE plot
sns.kdeplot(data=tips, x='total_bill',
            hue='sex', fill=True,
            ax=axes[1])
axes[1].set_title('KDE by Sex')

plt.tight_layout()
plt.show()"""
    add_code_box(slide, code, Inches(0.7), Inches(2.2), Inches(5.8), Inches(4.5))
    path = img("seaborn_histplot_kde.png")
    if not add_image_safe(slide, path, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0)):
        add_rect(slide, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0), fill=LIGHT_ROSE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 03 · Seaborn", color=ROSE, bg=LIGHT_ROSE)

# ─── SLIDE 26 — Jointplot ─────────────────────────────────────────────────────
def build_seaborn_jointplot(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, ROSE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=ROSE)
    add_title_block(slide, "jointplot — Bivariate Distribution",
                    "Section 5.3 — Dataset: Tips — total_bill vs tip with marginal plots",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    add_bullet_card(slide, Inches(0.7), Inches(2.2), Inches(5.5), Inches(4.0),
                    "jointplot() Parameters",
                    ["kind='scatter' — default scatter with marginal histograms",
                     "kind='kde' — kernel density contours + marginal KDE",
                     "kind='hex' — hexbin density heatmap",
                     "kind='reg' — regression line with confidence band",
                     "kind='resid' — regression residuals",
                     "hue='col' — color-codes by category (adds legend)"],
                    accent=ROSE, bg=LIGHT_ROSE)
    path = img("seaborn_jointplot.png")
    if not add_image_safe(slide, path, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0)):
        add_rect(slide, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0), fill=LIGHT_ROSE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 03 · Seaborn", color=ROSE, bg=LIGHT_ROSE)

# ─── SLIDE 27 — Pairplot ─────────────────────────────────────────────────────
def build_seaborn_pairplot(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, ROSE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=ROSE)
    add_title_block(slide, "pairplot — Multi-Variable Grid",
                    "Section 5.4 — Dataset: Iris (150 rows) — 4×4 feature relationship matrix",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    code = """iris = sns.load_dataset('iris')

sns.pairplot(iris,
             hue='species',
             diag_kind='kde',
             plot_kws={'alpha': 0.6},
             palette='tab10')
plt.suptitle('Iris Pairplot Matrix',
              y=1.02)
plt.show()

# Custom pairplot
g = sns.PairGrid(iris,
                  hue='species')
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot)
g.add_legend()"""
    add_code_box(slide, code, Inches(0.7), Inches(2.2), Inches(5.8), Inches(4.5))
    path = img("seaborn_pairplot.png")
    if not add_image_safe(slide, path, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0)):
        add_rect(slide, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0), fill=LIGHT_ROSE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 03 · Seaborn", color=ROSE, bg=LIGHT_ROSE)

# ─── SLIDE 28 — Catplot ───────────────────────────────────────────────────────
def build_seaborn_catplot(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, ROSE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=ROSE)
    add_title_block(slide, "catplot — Categorical Distributions",
                    "Section 5.5 — Dataset: Tips — tip by day and sex",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    add_bullet_card(slide, Inches(0.7), Inches(2.2), Inches(5.5), Inches(4.2),
                    "catplot() kind Options",
                    ["kind='strip' — individual data points (default)",
                     "kind='swarm' — non-overlapping strip plot",
                     "kind='box' — box-and-whisker with quartiles",
                     "kind='violin' — KDE of distribution shape",
                     "kind='bar' — aggregated bar with CI",
                     "kind='point' — mean with error bars"],
                    accent=ROSE, bg=LIGHT_ROSE)
    path = img("seaborn_catplot.png")
    if not add_image_safe(slide, path, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0)):
        add_rect(slide, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0), fill=LIGHT_ROSE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 03 · Seaborn", color=ROSE, bg=LIGHT_ROSE)

# ─── SLIDE 29 — Heatmap ───────────────────────────────────────────────────────
def build_seaborn_heatmap(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, ROSE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=ROSE)
    add_title_block(slide, "Heatmap — Flights Passenger Traffic",
                    "Section 5.6 — Dataset: Flights (144 rows) — year vs month matrix",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    code = """flights = sns.load_dataset('flights')

# Pivot to matrix format
pivot = flights.pivot(
    index='month',
    columns='year',
    values='passengers'
)

plt.figure(figsize=(12, 7))
sns.heatmap(
    pivot,
    annot=True,        # show numbers
    fmt='d',           # integer format
    cmap='YlOrRd',     # Yellow-Orange-Red
    linewidths=0.5,    # cell borders
    linecolor='white'
)
plt.title('Monthly Airline Passengers (1949-1960)')
plt.tight_layout()
plt.show()"""
    add_code_box(slide, code, Inches(0.7), Inches(2.2), Inches(5.8), Inches(4.5))
    path = img("seaborn_heatmap.png")
    if not add_image_safe(slide, path, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0)):
        add_rect(slide, Inches(6.8), Inches(1.8), Inches(6.0), Inches(5.0), fill=LIGHT_ROSE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 03 · Seaborn", color=ROSE, bg=LIGHT_ROSE)

# ─── SLIDE 30 — lmplot ────────────────────────────────────────────────────────
def build_seaborn_lmplot(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, ROSE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=ROSE)
    add_title_block(slide, "lmplot — Linear Regression Visualization",
                    "Section 5.7 — Dataset: Tips — linear trend of total_bill vs tip",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    add_bullet_card(slide, Inches(0.7), Inches(2.2), Inches(5.5), Inches(4.0),
                    "lmplot() Key Parameters",
                    ["x, y — column names from DataFrame",
                     "hue='col' — separate lines per category with colors",
                     "col='col' — create facet columns per category",
                     "row='col' — create facet rows per category",
                     "order=2 — polynomial regression (quadratic)",
                     "ci=95 — 95% confidence interval shading",
                     "scatter_kws={'alpha': 0.5} — control point transparency"],
                    accent=ROSE, bg=LIGHT_ROSE)
    path = img("seaborn_lmplot.png")
    if not add_image_safe(slide, path, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0)):
        add_rect(slide, Inches(6.5), Inches(1.8), Inches(6.3), Inches(5.0), fill=LIGHT_ROSE)
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 03 · Seaborn", color=ROSE, bg=LIGHT_ROSE)

# ─── SLIDE 31 — Seaborn Color Palettes ───────────────────────────────────────
def build_seaborn_palettes(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, ROSE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=ROSE)
    add_title_block(slide, "Seaborn Color Palettes",
                    "Section 5.8 — Categorical, sequential, and diverging palettes",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    palettes = [
        ("Categorical Palettes", ["deep", "muted", "pastel", "bright", "dark", "colorblind"], ROSE),
        ("Sequential Palettes", ["Blues", "Greens", "Oranges", "Purples", "YlOrRd", "viridis"], BLUE),
        ("Diverging Palettes", ["coolwarm", "RdBu", "seismic", "bwr", "PiYG", "PRGn"], PURPLE),
    ]
    for i, (title, items, color) in enumerate(palettes):
        y = Inches(2.2 + i * 1.55)
        add_text(slide, title, Inches(0.7), y, Inches(5), Inches(0.4),
                 size=13, bold=True, color=color, font="Calibri Light")
        for j, p in enumerate(items):
            bx = Inches(0.7 + j * 2.0)
            add_rect(slide, bx, y + Inches(0.45), Inches(1.8), Inches(0.7),
                     fill=OFF_WHITE, line_color=color, line_width=Pt(0.5))
            add_text(slide, p, bx, y + Inches(0.55), Inches(1.8), Inches(0.5),
                     size=10, color=color, font="Calibri", align=PP_ALIGN.CENTER)
    code = """# Setting a palette
sns.set_palette('muted')
sns.set_style('whitegrid')
with sns.color_palette('pastel'):
    sns.scatterplot(...)"""
    add_code_box(slide, code, Inches(0.7), Inches(6.4), Inches(12.0), Inches(0.85))
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 03 · Seaborn", color=ROSE, bg=LIGHT_ROSE)

# ─── SLIDE 32 — Seaborn Plot Types Gallery ────────────────────────────────────
def build_seaborn_gallery(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, ROSE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=ROSE)
    add_title_block(slide, "Seaborn Plot Types Reference",
                    "Section 5.9 — Complete function taxonomy",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    categories = [
        ("Distribution Plots", ["histplot", "kdeplot", "ecdfplot", "rugplot"], ROSE),
        ("Relational Plots", ["scatterplot", "lineplot", "relplot"], BLUE),
        ("Categorical Plots", ["stripplot", "swarmplot", "boxplot", "violinplot", "barplot"], PURPLE),
        ("Regression Plots", ["lmplot", "regplot", "residplot"], AMBER),
        ("Matrix Plots", ["heatmap", "clustermap"], TEAL),
        ("Grid Plots", ["pairplot", "jointplot", "FacetGrid", "PairGrid"], DARK),
    ]
    for i, (cat, funcs, color) in enumerate(categories):
        col = i % 2
        row = i // 2
        x = Inches(0.7 + col * 6.3)
        y = Inches(2.2 + row * 1.6)
        add_rect(slide, x, y, Inches(6.0), Inches(1.45),
                 fill=OFF_WHITE, line_color=color, line_width=Pt(0.75))
        add_rect(slide, x, y, Inches(0.06), Inches(1.45), fill=color)
        add_text(slide, cat, x + Inches(0.15), y + Inches(0.1), Inches(5.7), Inches(0.35),
                 size=11, bold=True, color=color, font="Calibri Light")
        add_text(slide, "  ·  ".join(funcs), x + Inches(0.15), y + Inches(0.5), Inches(5.7), Inches(0.85),
                 size=10, color=GRAY, font="Calibri")
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 03 · Seaborn", color=ROSE, bg=LIGHT_ROSE)

# ─── SLIDE 33 — Seaborn Summary ───────────────────────────────────────────────
def build_seaborn_summary(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_accent_bar(slide, ROSE, w=Inches(0.12))
    add_rect(slide, 0, 0, W, Inches(0.06), fill=ROSE)
    add_title_block(slide, "Seaborn — Key Takeaways",
                    "Topic 03 Summary",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7))
    takeaways = [
        ("📊 High-Level API", "One-liner statistical charts with Pandas column names as arguments.", ROSE),
        ("🎨 Beautiful Defaults", "muted, deep, pastel palettes and whitegrid style work out-of-the-box.", BLUE),
        ("📈 Statistical Intelligence", "Automatic KDE, confidence intervals, and regression without extra code.", PURPLE),
        ("🔗 Grid Systems", "FacetGrid, PairGrid, and jointplot for publication-ready multi-panel figures.", TEAL),
        ("🏗️ Matplotlib Extensible", "Every Seaborn plot returns Matplotlib Axes — full low-level customization possible.", AMBER),
    ]
    for i, (title, desc, color) in enumerate(takeaways):
        y = Inches(2.2 + i * 0.95)
        add_rect(slide, Inches(0.7), y, Inches(12.0), Inches(0.82),
                 fill=LIGHT_ROSE if i % 2 == 0 else OFF_WHITE,
                 line_color=LIGHT_GRAY, line_width=Pt(0.5))
        add_rect(slide, Inches(0.7), y, Inches(0.06), Inches(0.82), fill=color)
        add_text(slide, title, Inches(0.85), y + Inches(0.1), Inches(3.0), Inches(0.38),
                 size=12, bold=True, color=color, font="Calibri Light")
        add_text(slide, desc, Inches(3.8), y + Inches(0.1), Inches(8.6), Inches(0.65),
                 size=11, color=GRAY, font="Calibri Light")
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Topic 03 · Seaborn", color=ROSE, bg=LIGHT_ROSE)

# ─── SLIDE 34 — Seaborn vs Matplotlib Table ──────────────────────────────────
def build_comparison_table(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_rect(slide, 0, 0, W, Inches(0.06), fill=AMBER)
    add_title_block(slide, "Seaborn vs Matplotlib — Full Comparison",
                    "Why choose Seaborn? When to use Matplotlib directly?",
                    title_color=DARK, sub_color=GRAY, x=Inches(0.7),
                    title_size=24)
    headers = ["Feature", "Matplotlib", "Seaborn"]
    rows = [
        ("Abstraction Level", "Low-level (full manual control)", "High-level (declarative)"),
        ("Lines of Code", "10–30 lines for a styled plot", "1–3 lines for same plot"),
        ("DataFrame Support", "Indirect (via .values, .to_numpy)", "Native (x='col', data=df)"),
        ("Statistical Estimators", "Manual calculation required", "Built-in KDE, CI, regression"),
        ("Color Palettes", "Manual color arrays", "Named palettes (muted, deep...)"),
        ("Multi-Panel Grids", "plt.subplots() + manual sizing", "FacetGrid, PairGrid (auto)"),
        ("Plot Types", "Universal (any plot type)", "Statistical charts only"),
        ("Customization", "Unlimited fine-grained control", "Limited; falls back to Matplotlib"),
        ("Performance", "Faster for large custom plots", "Slightly slower overhead"),
        ("Deprecation Risk", "None (active development)", "Some functions deprecated (distplot → histplot)"),
    ]
    col_ws = [Inches(2.8), Inches(4.5), Inches(4.5)]
    tx = Inches(0.6)
    ty = Inches(1.9)
    for j, h in enumerate(headers):
        x = tx + sum(col_ws[:j])
        bg = DARK if j == 0 else (BLUE if j == 1 else ROSE)
        add_rect(slide, x, ty, col_ws[j], Inches(0.4), fill=bg)
        add_text(slide, h, x + Inches(0.08), ty + Inches(0.07), col_ws[j] - Inches(0.16),
                 Inches(0.3), size=11, bold=True, color=WHITE, font="Calibri", align=PP_ALIGN.CENTER)
    for r, row in enumerate(rows):
        bg = OFF_WHITE if r % 2 == 0 else WHITE
        for j, val in enumerate(row):
            x = tx + sum(col_ws[:j])
            add_rect(slide, x, ty + (r+1)*Inches(0.47), col_ws[j], Inches(0.47),
                     fill=bg, line_color=LIGHT_GRAY, line_width=Pt(0.3))
            add_text(slide, val, x + Inches(0.08), ty + (r+1)*Inches(0.47) + Inches(0.07),
                     col_ws[j] - Inches(0.16), Inches(0.36),
                     size=9, color=DARK if j == 0 else GRAY, font="Calibri",
                     bold=(j == 0))
    add_slide_number(slide, n, TOTAL_SLIDES)
    add_footer_tag(slide, "Comparison · Seaborn vs Matplotlib", color=AMBER, bg=RGBColor(0xFF, 0xF7, 0xED))

# ─── SLIDE 35 — Final / Thank You ────────────────────────────────────────────
def build_final(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    # Gradient panel
    add_rect(slide, 0, 0, W, Inches(0.08), fill=BLUE)
    add_rect(slide, Inches(8.5), 0, Inches(4.83), H, fill=DARK)
    # Left content
    add_text(slide, "THANK YOU",
             Inches(0.7), Inches(1.6), Inches(7.5), Inches(1.2),
             size=52, bold=True, color=DARK, font="Calibri Light")
    add_text(slide, "Data Visualization Seminar",
             Inches(0.7), Inches(2.9), Inches(7.5), Inches(0.55),
             size=16, color=BLUE, font="Calibri Light", bold=True)
    add_text(slide, "Three-Dimensional Plotting  •  Geographic Data with Basemap  •  Visualization with Seaborn",
             Inches(0.7), Inches(3.55), Inches(7.5), Inches(0.6),
             size=11, color=GRAY, font="Calibri Light")
    # Summary stats on right dark panel
    stats = [("3", "Topics Covered"), ("17", "Visualization Types"),
             ("3", "Datasets Used"), ("35", "Total Slides")]
    for i, (num, label) in enumerate(stats):
        y = Inches(1.5 + i * 1.3)
        add_text(slide, num, Inches(9.0), y, Inches(2.0), Inches(0.9),
                 size=40, bold=True, color=WHITE, font="Calibri Light", align=PP_ALIGN.CENTER)
        add_text(slide, label, Inches(9.0), y + Inches(0.85), Inches(2.0), Inches(0.4),
                 size=11, color=MID_GRAY, font="Calibri Light", align=PP_ALIGN.CENTER)
    add_text(slide, "Questions & Discussion",
             Inches(0.7), Inches(5.8), Inches(7.5), Inches(0.5),
             size=18, bold=True, color=BLUE, font="Calibri Light")
    add_slide_number(slide, n, TOTAL_SLIDES, color=WHITE)

def build_qr_code_slide(slide, n):
    add_rect(slide, 0, 0, W, H, fill=WHITE)
    add_title_block(slide, "Scan QR Codes for Videos, Slides & PPT Download", "Live public links hosted 24/7 on GitHub Pages — scan with any smartphone camera")
    
    # 4 QR Code cards side-by-side
    qrs = [
        ("qr_tanglish_video.png", "Tanglish Video", "Stream Full Video in Tanglish"),
        ("qr_english_video.png", "English Video", "Full 7-min HD 3D Presentation"),
        ("qr_interactive_deck.png", "Web Presentation", "Interactive 3D Deck on Mobile"),
        ("qr_ppt_download.png", "Download PPT", "PowerPoint Presentation (.pptx)")
    ]
    
    for i, (filename, title, desc) in enumerate(qrs):
        x = Inches(0.5 + i * 3.1)
        y = Inches(1.8)
        w = Inches(2.9)
        h = Inches(5.0)
        
        card = add_rect(slide, x, y, w, h, fill=OFF_WHITE, line_color=LIGHT_GRAY, line_width=Pt(0.5))
        
        img_p = img(filename)
        if img_p:
            slide.shapes.add_picture(img_p, x + Inches(0.15), y + Inches(0.15), Inches(2.6), Inches(3.9))
            
        add_text(slide, title, x + Inches(0.1), y + Inches(4.15), Inches(2.7), Inches(0.35),
                 size=13, bold=True, color=DARK, align=PP_ALIGN.CENTER)
        add_text(slide, desc, x + Inches(0.1), y + Inches(4.5), Inches(2.7), Inches(0.35),
                 size=8.5, color=GRAY, align=PP_ALIGN.CENTER)
                 
    add_slide_number(slide, n, TOTAL_SLIDES)

# ═══════════════════════════════════════════════════════════════════════════════
# BUILD ALL SLIDES
# ═══════════════════════════════════════════════════════════════════════════════

builders = [
    build_cover,              # 1
    build_toc,                # 2
    build_datasets_overview,  # 3
    build_dataset_samples,    # 4
    build_3d_divider,         # 5
    build_3d_axes,            # 6
    build_3d_helix,           # 7
    build_3d_contour,         # 8
    build_3d_wireframe,       # 9
    build_3d_viewinit,        # 10
    build_3d_bar,             # 11
    build_3d_triangulation,   # 12
    build_3d_iris,            # 13
    build_3d_flights,         # 14
    build_basemap_divider,    # 15
    build_basemap_intro,      # 16
    build_basemap_setup,      # 17
    build_basemap_cities,     # 18
    build_basemap_greatcircles,# 19
    build_basemap_projections, # 20
    build_cartopy,            # 21
    build_basemap_summary,    # 22
    build_seaborn_divider,    # 23
    build_seaborn_intro,      # 24
    build_seaborn_hist_kde,   # 25
    build_seaborn_jointplot,  # 26
    build_seaborn_pairplot,   # 27
    build_seaborn_catplot,    # 28
    build_seaborn_heatmap,    # 29
    build_seaborn_lmplot,     # 30
    build_seaborn_palettes,   # 31
    build_seaborn_gallery,    # 32
    build_seaborn_summary,    # 33
    build_comparison_table,   # 34
    build_qr_code_slide,      # 35
    build_final,              # 36
]

print(f"Building {len(builders)} slides...")
for i, builder in enumerate(builders, 1):
    sl = blank_slide()
    builder(sl, i)
    print(f"  [OK] Slide {i:02d}/{len(builders):02d}: {builder.__name__}")

enhanced_file = os.path.join(BASE_DIR, "Data_Visualization_Seminar_Enhanced.pptx")
try:
    prs.save(OUT_FILE)
    print(f"\nDone! Presentation saved to:\n   {OUT_FILE}")
except Exception as e:
    prs.save(enhanced_file)
    print(f"\nDone! Presentation saved to:\n   {enhanced_file}")
prs.save(enhanced_file)
print(f"   Enhanced file saved to: {enhanced_file}")
print(f"   Total slides: {len(prs.slides)}")
