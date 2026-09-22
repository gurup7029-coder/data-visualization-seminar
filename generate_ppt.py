"""
Data Visualization Seminar - PowerPoint Generator
Enhanced AI Dark-Tech Theme with Definition, Code, Output Image, and Real-World Use Case on every slide.
Smooth PowerPoint transitions/animations included.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml import parse_xml
from pptx.oxml.ns import nsdecls
import os

# ─── Path Setup ──────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR  = os.path.join(BASE_DIR, "assets", "images")
OUT_FILE = os.path.join(BASE_DIR, "Data_Visualization_Seminar.pptx")
ENHANCED_FILE = os.path.join(BASE_DIR, "Data_Visualization_Seminar_Enhanced.pptx")

def img(name):
    p1 = os.path.join(IMG_DIR, name)
    if os.path.exists(p1):
        return p1
    p2 = os.path.join(BASE_DIR, "video_assets", name)
    if os.path.exists(p2):
        return p2
    return None

# ─── Color Palette (AI Dark-Tech Theme) ───────────────────────────────────────
BG_DARK         = RGBColor(0x0B, 0x0F, 0x19)  # Deep Obsidian Slate
CARD_BG         = RGBColor(0x13, 0x1B, 0x2E)  # Neural Panel Card
CARD_BORDER     = RGBColor(0x23, 0x32, 0x4D)  # Tech Border
CODE_BG         = RGBColor(0x06, 0x09, 0x13)  # Pure Dark Terminal
TEXT_WHITE      = RGBColor(0xF8, 0xFA, 0xFC)  # Crisp White
TEXT_MUTED      = RGBColor(0x94, 0xA3, 0xB8)  # Slate Gray
TEXT_SUBTLE     = RGBColor(0x64, 0x74, 0x8B)  # Muted Dark Slate

# Topic Accents
VIOLET_PRIMARY  = RGBColor(0x8B, 0x5C, 0xF6)  # 3D Plotting Neon Violet
VIOLET_BG       = RGBColor(0x23, 0x17, 0x42)  # Dark Violet Glow
CYAN_PRIMARY    = RGBColor(0x06, 0xB6, 0xD4)  # Basemap Cyan
CYAN_BG         = RGBColor(0x08, 0x2B, 0x36)  # Dark Cyan Glow
ROSE_PRIMARY    = RGBColor(0xF4, 0x3F, 0x5E)  # Seaborn Rose
ROSE_BG         = RGBColor(0x38, 0x10, 0x1E)  # Dark Rose Glow
AMBER_ACCENT    = RGBColor(0xF5, 0x9E, 0x0B)  # Solar Amber
EMERALD_ACCENT  = RGBColor(0x10, 0xB9, 0x81)  # Emerald Success
BLUE_ACCENT     = RGBColor(0x3B, 0x82, 0xF6)  # AI Blue

# ─── Slide Dimensions (16:9 Widescreen) ──────────────────────────────────────
prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)

W = prs.slide_width
H = prs.slide_height
TOTAL_SLIDES = 36

# ─── Core Helpers ────────────────────────────────────────────────────────────

def blank_slide(transition_type="fade"):
    """Creates a blank slide with deep obsidian background and smooth transition."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Set background fill
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = BG_DARK
    
    # Add PowerPoint transition animation
    try:
        trans_xml = parse_xml(f'<p:transition {nsdecls("p")} spd="med"><p:{transition_type}/></p:transition>')
        slide._element.append(trans_xml)
    except Exception:
        pass
        
    return slide

def add_rect(slide, x, y, w, h, fill=None, line_color=None, line_width=Pt(1)):
    """Draws a rectangular container with fill and border."""
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    if fill:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill
    else:
        shape.fill.background()
        
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = line_width
    else:
        shape.line.fill.background()
    return shape

def add_rounded_card(slide, x, y, w, h, fill=CARD_BG, line_color=CARD_BORDER, line_width=Pt(1)):
    """Draws a modern rounded-corner card."""
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = line_width
    else:
        shape.line.fill.background()
    return shape

def add_text_box(slide, text, x, y, w, h, size=14, bold=False, italic=False,
                 color=TEXT_WHITE, align=PP_ALIGN.LEFT, font="Segoe UI", wrap=True):
    """Creates a text box with precise typography."""
    txb = slide.shapes.add_textbox(x, y, w, h)
    tf = txb.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = str(text)
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txb

def add_slide_header(slide, badge_text, title_text, subtitle_text, slide_num, accent=VIOLET_PRIMARY):
    """Draws the unified top header with badge, title, subtitle, and slide counter."""
    # Top luminous accent strip
    add_rect(slide, Inches(0.55), Inches(0.35), Inches(0.8), Inches(0.04), fill=accent)
    
    # Topic Badge
    add_rounded_card(slide, Inches(0.55), Inches(0.48), Inches(2.2), Inches(0.28), fill=CARD_BG, line_color=accent, line_width=Pt(0.75))
    add_text_box(slide, badge_text, Inches(0.6), Inches(0.51), Inches(2.1), Inches(0.22),
                 size=9, bold=True, color=accent, align=PP_ALIGN.CENTER, font="Segoe UI")
                 
    # Title
    add_text_box(slide, title_text, Inches(0.55), Inches(0.80), Inches(10.5), Inches(0.42),
                 size=21, bold=True, color=TEXT_WHITE, font="Segoe UI")
                 
    # Subtitle
    add_text_box(slide, subtitle_text, Inches(0.55), Inches(1.22), Inches(10.5), Inches(0.26),
                 size=10.5, color=TEXT_MUTED, font="Segoe UI")
                 
    # Slide Counter Badge in top right
    add_rounded_card(slide, Inches(11.6), Inches(0.48), Inches(1.15), Inches(0.30), fill=CARD_BG, line_color=CARD_BORDER)
    add_text_box(slide, f"{slide_num:02d} / {TOTAL_SLIDES:02d}", Inches(11.6), Inches(0.53), Inches(1.15), Inches(0.22),
                 size=9.5, bold=True, color=TEXT_MUTED, align=PP_ALIGN.CENTER, font="Consolas")

def add_image_fit(slide, path, x, y, max_w, max_h):
    """Adds an image keeping its aspect ratio within max_w and max_h."""
    if not path or not os.path.exists(path):
        return None
    try:
        from PIL import Image
        with Image.open(path) as im:
            iw, ih = im.size
        aspect = iw / ih
        box_aspect = max_w / max_h
        if aspect > box_aspect:
            w = max_w
            h = max_w / aspect
            y_pos = y + (max_h - h) / 2
            x_pos = x
        else:
            h = max_h
            w = max_h * aspect
            x_pos = x + (max_w - w) / 2
            y_pos = y
        return slide.shapes.add_picture(path, x_pos, y_pos, w, h)
    except Exception:
        return slide.shapes.add_picture(path, x, y, max_w, max_h)

def add_definition_card(slide, x, y, w, h, title, bullets, accent=VIOLET_PRIMARY):
    """Draws a concept & definition card."""
    card = add_rounded_card(slide, x, y, w, h, fill=CARD_BG, line_color=CARD_BORDER)
    
    # Left accent vertical indicator
    add_rect(slide, x, y + Inches(0.12), Inches(0.05), h - Inches(0.24), fill=accent)
    
    # Card Header
    add_text_box(slide, f"📖  {title}", x + Inches(0.2), y + Inches(0.12), w - Inches(0.3), Inches(0.28),
                 size=11, bold=True, color=accent, font="Segoe UI")
                 
    # Bullets
    tf_box = slide.shapes.add_textbox(x + Inches(0.2), y + Inches(0.42), w - Inches(0.35), h - Inches(0.5))
    tf = tf_box.text_frame
    tf.word_wrap = True
    for i, b in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(4)
        run = p.add_run()
        run.text = f"•  {b}"
        run.font.name = "Segoe UI"
        run.font.size = Pt(9.2)
        run.font.color.rgb = TEXT_WHITE if i == 0 else TEXT_MUTED

def add_code_card(slide, x, y, w, h, code, accent=VIOLET_PRIMARY):
    """Draws a dark-themed terminal code block."""
    card = add_rounded_card(slide, x, y, w, h, fill=CODE_BG, line_color=CARD_BORDER)
    
    # Header bar
    header = add_rect(slide, x, y, w, Inches(0.30), fill=RGBColor(0x0E, 0x14, 0x22))
    add_text_box(slide, "💻  [In]: Python 3.12 (Colab / Jupyter)", x + Inches(0.15), y + Inches(0.05), w - Inches(0.3), Inches(0.22),
                 size=8.5, bold=True, color=accent, font="Consolas")
                 
    # Code content
    tf_box = slide.shapes.add_textbox(x + Inches(0.18), y + Inches(0.34), w - Inches(0.36), h - Inches(0.40))
    tf = tf_box.text_frame
    tf.word_wrap = True
    lines = code.strip().split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(1.5)
        run = p.add_run()
        run.text = line
        run.font.name = "Consolas"
        run.font.size = Pt(8.5)
        if line.strip().startswith("#"):
            run.font.color.rgb = RGBColor(0x10, 0xB9, 0x81)  # Green comments
        elif any(line.strip().startswith(kw) for kw in ["import", "from", "def ", "for ", "while", "return", "if "]):
            run.font.color.rgb = RGBColor(0x38, 0xBD, 0xF8)  # Cyan keywords
        else:
            run.font.color.rgb = TEXT_WHITE

def add_output_card(slide, x, y, w, h, img_name, label="Matplotlib Real Execution Output", accent=VIOLET_PRIMARY):
    """Draws an output visualization card containing the rendered plot image."""
    card = add_rounded_card(slide, x, y, w, h, fill=CARD_BG, line_color=CARD_BORDER)
    
    # Header badge
    add_text_box(slide, f"📊  {label}", x + Inches(0.2), y + Inches(0.10), w - Inches(0.4), Inches(0.24),
                 size=9.5, bold=True, color=accent, font="Segoe UI")
                 
    # Image frame inside card
    img_pad = Inches(0.15)
    img_y = y + Inches(0.36)
    img_w = w - (img_pad * 2)
    img_h = h - Inches(0.45)
    
    path = img(img_name)
    if path:
        add_image_fit(slide, path, x + img_pad, img_y, img_w, img_h)
    else:
        add_rect(slide, x + img_pad, img_y, img_w, img_h, fill=RGBColor(0x1A, 0x24, 0x38))
        add_text_box(slide, f"[Preview: {img_name}]", x, img_y + img_h/2 - Inches(0.2), w, Inches(0.4),
                     size=10, color=TEXT_MUTED, align=PP_ALIGN.CENTER)

def add_usecase_card(slide, x, y, w, h, industry, scenario, value, accent=EMERALD_ACCENT):
    """Draws the Real-World Use Case & Industry Application card."""
    card = add_rounded_card(slide, x, y, w, h, fill=CARD_BG, line_color=CARD_BORDER)
    
    # Glowing top accent strip
    add_rect(slide, x, y, w, Inches(0.04), fill=accent)
    
    # Header
    add_text_box(slide, "🌐  Real-World Use Case & Industry Application", x + Inches(0.2), y + Inches(0.10), w - Inches(0.4), Inches(0.24),
                 size=10, bold=True, color=accent, font="Segoe UI")
                 
    tf_box = slide.shapes.add_textbox(x + Inches(0.2), y + Inches(0.36), w - Inches(0.4), h - Inches(0.42))
    tf = tf_box.text_frame
    tf.word_wrap = True
    
    # Industry
    p1 = tf.paragraphs[0]
    p1.space_after = Pt(2.5)
    r1a = p1.add_run()
    r1a.text = "🏢 Industry: "
    r1a.font.bold = True
    r1a.font.size = Pt(8.8)
    r1a.font.color.rgb = accent
    r1b = p1.add_run()
    r1b.text = industry
    r1b.font.size = Pt(8.8)
    r1b.font.color.rgb = TEXT_WHITE
    
    # Scenario
    p2 = tf.add_paragraph()
    p2.space_after = Pt(2.5)
    r2a = p2.add_run()
    r2a.text = "💡 Application: "
    r2a.font.bold = True
    r2a.font.size = Pt(8.8)
    r2a.font.color.rgb = AMBER_ACCENT
    r2b = p2.add_run()
    r2b.text = scenario
    r2b.font.size = Pt(8.8)
    r2b.font.color.rgb = TEXT_MUTED
    
    # Value
    p3 = tf.add_paragraph()
    r3a = p3.add_run()
    r3a.text = "🎯 Key Impact: "
    r3a.font.bold = True
    r3a.font.size = Pt(8.8)
    r3a.font.color.rgb = BLUE_ACCENT
    r3b = p3.add_run()
    r3b.text = value
    r3b.font.size = Pt(8.8)
    r3b.font.color.rgb = TEXT_MUTED

# ═══════════════════════════════════════════════════════════════════════════════
# 36 SLIDE BUILDERS (AI DARK TECH THEME WITH ALL 4 COMPONENTS)
# ═══════════════════════════════════════════════════════════════════════════════

def build_cover(slide, n):
    """Slide 1: AI Tech Cover."""
    # Ambient grid / gradient accents
    add_rounded_card(slide, Inches(0.8), Inches(0.8), Inches(11.73), Inches(5.9), fill=RGBColor(0x0E, 0x15, 0x26), line_color=RGBColor(0x1E, 0x29, 0x3B), line_width=Pt(1.5))
    
    # Glowing top line
    add_rect(slide, Inches(1.5), Inches(0.8), Inches(10.33), Inches(0.06), fill=VIOLET_PRIMARY)
    
    # Topic pill
    add_rounded_card(slide, Inches(1.5), Inches(1.4), Inches(3.2), Inches(0.35), fill=CARD_BG, line_color=VIOLET_PRIMARY)
    add_text_box(slide, "⚡ DATA SCIENCE SEMINAR • 2026", Inches(1.6), Inches(1.47), Inches(3.0), Inches(0.25),
                 size=10, bold=True, color=VIOLET_PRIMARY, font="Segoe UI")
                 
    # Seminar Main Title
    add_text_box(slide, "Data Visualization in Python", Inches(1.5), Inches(1.95), Inches(10.0), Inches(0.85),
                 size=38, bold=True, color=TEXT_WHITE, font="Segoe UI")
    add_text_box(slide, "3D Matplotlib Plotting  •  Geospatial Basemap GIS  •  Statistical Seaborn", Inches(1.5), Inches(2.85), Inches(10.0), Inches(0.4),
                 size=15, bold=True, color=CYAN_PRIMARY, font="Segoe UI")
                 
    # Divider line
    add_rect(slide, Inches(1.5), Inches(3.4), Inches(10.33), Inches(0.02), fill=CARD_BORDER)
    
    # Presenter Information Card
    add_rounded_card(slide, Inches(1.5), Inches(3.7), Inches(6.0), Inches(2.4), fill=CARD_BG, line_color=CARD_BORDER)
    add_text_box(slide, "👤  PRESENTER CREDENTIALS", Inches(1.8), Inches(3.9), Inches(5.4), Inches(0.3),
                 size=11, bold=True, color=VIOLET_PRIMARY, font="Segoe UI")
                 
    p_info = [
        ("Student Name:", "GURUPRASATH B"),
        ("Register Number:", "7376242AD131"),
        ("Department:", "Artificial Intelligence & Data Science"),
        ("Institution:", "Bannari Amman Institute of Technology (BIT)")
    ]
    for idx, (lbl, val) in enumerate(p_info):
        y_pos = Inches(4.3 + idx * 0.38)
        add_text_box(slide, lbl, Inches(1.8), y_pos, Inches(2.2), Inches(0.3), size=9.5, color=TEXT_MUTED)
        add_text_box(slide, val, Inches(3.8), y_pos, Inches(3.5), Inches(0.3), size=10, bold=True, color=TEXT_WHITE)
        
    # Seminar Overview Badge Card
    add_rounded_card(slide, Inches(7.8), Inches(3.7), Inches(4.0), Inches(2.4), fill=CARD_BG, line_color=CARD_BORDER)
    add_text_box(slide, "🎯  SEMINAR HIGHLIGHTS", Inches(8.0), Inches(3.9), Inches(3.6), Inches(0.3),
                 size=11, bold=True, color=EMERALD_ACCENT, font="Segoe UI")
    badges = [
        "✓ 36 Comprehensive Multi-Dimensional Slides",
        "✓ Interactive 3D WebGL Live Demonstrations",
        "✓ Real-World Satellite & GIS Mapping (Basemap)",
        "✓ Advanced Statistical Distributions (Seaborn)",
        "✓ End-to-End Google Colab Executable Code"
    ]
    for idx, b in enumerate(badges):
        add_text_box(slide, b, Inches(8.0), Inches(4.3 + idx * 0.32), Inches(3.6), Inches(0.28),
                     size=9, color=TEXT_MUTED)

def build_toc(slide, n):
    """Slide 2: Table of Contents / Agenda."""
    add_slide_header(slide, "🗺️ AGENDA & CURRICULUM", "Seminar Table of Contents", "Systematic journey across modern Python visualization paradigms", n, CYAN_PRIMARY)
    
    modules = [
        ("MODULE 01", "Three-Dimensional Plotting", "Matplotlib mplot3d Toolkit",
         ["• 3D Axes Registration & Projections",
          "• Parametric Curves & Scatter Spirals (Helix)",
          "• Sinusoidal Surface & Contour Projections",
          "• Wireframe Meshgrids & Lighting Shading",
          "• Dynamic View Angles (elev & azim)",
          "• 3D Bar Frequency & Delaunay Triangulation"], VIOLET_PRIMARY),
        ("MODULE 02", "Geographic Data with Basemap", "Geospatial Cartography & GIS",
         ["• Cartographic Basemap Toolkit Setup",
          "• Projection Systems: Cylindrical to Orthographic",
          "• Coastlines, Rivers & Shaded Relief Layers",
          "• Global Population & Urban Density Mapping",
          "• Great Circle Trans-Oceanic Flight Trajectories",
          "• Modern Transition: Cartopy & GeoPandas"], CYAN_PRIMARY),
        ("MODULE 03", "Statistical Seaborn Visuals", "High-Level Grammar of Graphics",
         ["• Seaborn Design Philosophy & Declarative API",
          "• Kernel Density Estimation (KDE) & Histograms",
          "• Multi-Variable Pairplots & Feature Matrices",
          "• Categorical Box, Violin & Strip Plots",
          "• Correlation Matrices & Clustered Heatmaps",
          "• Linear Regression & Residual Modeling"], ROSE_PRIMARY),
    ]
    
    for i, (tag, title, sub, points, accent) in enumerate(modules):
        x = Inches(0.55 + i * 4.15)
        w = Inches(3.9)
        h = Inches(5.3)
        y = Inches(1.6)
        
        card = add_rounded_card(slide, x, y, w, h, fill=CARD_BG, line_color=CARD_BORDER)
        add_rect(slide, x, y, w, Inches(0.06), fill=accent)
        
        add_rounded_card(slide, x + Inches(0.2), y + Inches(0.2), Inches(1.3), Inches(0.28), fill=RGBColor(0x1B, 0x25, 0x3D), line_color=accent)
        add_text_box(slide, tag, x + Inches(0.2), y + Inches(0.24), Inches(1.3), Inches(0.2), size=9, bold=True, color=accent, align=PP_ALIGN.CENTER)
        
        add_text_box(slide, title, x + Inches(0.2), y + Inches(0.60), w - Inches(0.4), Inches(0.35), size=14, bold=True, color=TEXT_WHITE)
        add_text_box(slide, sub, x + Inches(0.2), y + Inches(0.95), w - Inches(0.4), Inches(0.25), size=9.5, color=accent)
        
        add_rect(slide, x + Inches(0.2), y + Inches(1.3), w - Inches(0.4), Inches(0.01), fill=CARD_BORDER)
        
        for idx, pt in enumerate(points):
            add_text_box(slide, pt, x + Inches(0.2), y + Inches(1.45 + idx * 0.58), w - Inches(0.4), Inches(0.48),
                         size=9.2, color=TEXT_MUTED)

def build_datasets_overview(slide, n):
    """Slide 3: Datasets & Environment Setup."""
    add_slide_header(slide, "⚙️ ENVIRONMENT & DATA", "Datasets & Computing Environment", "Curated benchmark datasets used throughout the practical demonstrations", n, EMERALD_ACCENT)
    
    datasets = [
        ("🌸 Iris Flower Morphometrics", "Fisher (1936)", "150 samples across 3 species (Setosa, Versicolor, Virginica) with 4 biometric continuous features.", "Used for 3D multi-class clustering and Seaborn pairplot feature separation.", VIOLET_PRIMARY),
        ("✈️ US Commercial Flights", "BTS Open Data", "Decade-long records of airline passenger counts, routes, seasonality, and monthly delays.", "Used for 3D trajectory surface interpolation and Seaborn categorical heatmap grids.", CYAN_PRIMARY),
        ("🪐 Extrasolar Planetary Systems", "NASA Exoplanet Archive", "1,000+ confirmed exoplanets with orbital periods, masses, and astronomical detection methods.", "Used for logarithmic scatter regressions and joint hexbin distribution mapping.", ROSE_PRIMARY),
        ("🌍 Global Metropolises & GIS", "Natural Earth / USGS", "Geographical latitude/longitude coordinates, elevation, and population counts for 10,000+ cities.", "Used for Basemap cartographic scatter bubbles and geodesic great-circle flight arcs.", AMBER_ACCENT),
    ]
    
    for i, (name, src, desc, app, accent) in enumerate(datasets):
        row = i // 2
        col = i % 2
        x = Inches(0.55 + col * 6.2)
        y = Inches(1.6 + row * 2.7)
        w = Inches(5.95)
        h = Inches(2.45)
        
        card = add_rounded_card(slide, x, y, w, h, fill=CARD_BG, line_color=CARD_BORDER)
        add_rect(slide, x, y, Inches(0.05), h, fill=accent)
        
        add_text_box(slide, name, x + Inches(0.2), y + Inches(0.15), w - Inches(0.4), Inches(0.32), size=12, bold=True, color=TEXT_WHITE)
        add_text_box(slide, f"Source: {src}", x + Inches(0.2), y + Inches(0.48), w - Inches(0.4), Inches(0.22), size=9, color=accent)
        
        add_text_box(slide, desc, x + Inches(0.2), y + Inches(0.80), w - Inches(0.4), Inches(0.7), size=9.5, color=TEXT_MUTED)
        
        add_rounded_card(slide, x + Inches(0.2), y + Inches(1.6), w - Inches(0.4), Inches(0.65), fill=RGBColor(0x0C, 0x12, 0x20), line_color=CARD_BORDER)
        add_text_box(slide, f"🎯 Seminar Application: {app}", x + Inches(0.3), y + Inches(1.68), w - Inches(0.6), Inches(0.5), size=8.8, color=TEXT_WHITE)

def build_dataset_samples(slide, n):
    """Slide 4: Dataset Samples & Environment Code."""
    add_slide_header(slide, "💻 PYTHON STACK", "Software Environment & Dependency Matrix", "Modern scientific Python dependencies and environment initialization", n, BLUE_ACCENT)
    
    code = """# Core Scientific Python Stack Initialization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import seaborn as sns
from mpl_toolkits.basemap import Basemap

# Configure High-DPI Display Settings
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.family'] = 'sans-serif'
sns.set_theme(style='darkgrid', palette='deep')

# Load Standard Seminar Benchmark Datasets
iris     = sns.load_dataset('iris')
flights  = sns.load_dataset('flights')
planets  = sns.load_dataset('planets')
print("Environment successfully initialized with GPU/WebGL accelerators.")"""

    add_code_card(slide, Inches(0.55), Inches(1.6), Inches(6.4), Inches(5.3), code, accent=BLUE_ACCENT)
    
    # Right side stack overview
    stack = [
        ("Python 3.12 Engine", "C-Optimized interpreter with JIT compilation & vector execution.", BLUE_ACCENT),
        ("NumPy & Pandas", "Memory-efficient N-dimensional arrays & structured DataFrame queries.", EMERALD_ACCENT),
        ("Matplotlib 3.8 & mplot3d", "Foundational plotting engine with 3D projection transformations.", VIOLET_PRIMARY),
        ("Seaborn 0.13", "Statistical visualization with automated aggregation & error bands.", ROSE_PRIMARY),
        ("Basemap & Cartopy", "Geodesic cartographic transforms with PROJ4 & GEOS topology.", CYAN_PRIMARY),
    ]
    for i, (title, desc, accent) in enumerate(stack):
        y = Inches(1.6 + i * 1.05)
        add_rounded_card(slide, Inches(7.2), y, Inches(5.55), Inches(0.92), fill=CARD_BG, line_color=CARD_BORDER)
        add_rect(slide, Inches(7.2), y, Inches(0.06), Inches(0.92), fill=accent)
        add_text_box(slide, title, Inches(7.45), y + Inches(0.12), Inches(5.1), Inches(0.28), size=11, bold=True, color=TEXT_WHITE)
        add_text_box(slide, desc, Inches(7.45), y + Inches(0.42), Inches(5.1), Inches(0.40), size=9, color=TEXT_MUTED)

def build_3d_divider(slide, n):
    """Slide 5: Module 1 Divider."""
    add_rounded_card(slide, Inches(1.0), Inches(1.0), Inches(11.33), Inches(5.5), fill=CARD_BG, line_color=VIOLET_PRIMARY, line_width=Pt(1.5))
    add_rect(slide, Inches(1.0), Inches(1.0), Inches(11.33), Inches(0.08), fill=VIOLET_PRIMARY)
    
    add_rounded_card(slide, Inches(1.8), Inches(1.8), Inches(2.2), Inches(0.35), fill=VIOLET_BG, line_color=VIOLET_PRIMARY)
    add_text_box(slide, "MODULE 01 • SECTION 3.1", Inches(1.8), Inches(1.86), Inches(2.2), Inches(0.24), size=10, bold=True, color=VIOLET_PRIMARY, align=PP_ALIGN.CENTER)
    
    add_text_box(slide, "Three-Dimensional Plotting\nin Matplotlib", Inches(1.8), Inches(2.4), Inches(9.5), Inches(1.4),
                 size=38, bold=True, color=TEXT_WHITE, font="Segoe UI")
                 
    add_text_box(slide, "Mastering the mplot3d toolkit: from basic 3D point clouds and spirals to complex topographical contour surfaces, wireframes, camera angle manipulation, and Delaunay triangulations.", Inches(1.8), Inches(4.0), Inches(9.5), Inches(0.9),
                 size=13, color=TEXT_MUTED, font="Segoe UI")
                 
    add_rect(slide, Inches(1.8), Inches(5.1), Inches(9.5), Inches(0.02), fill=CARD_BORDER)
    add_text_box(slide, "Key Functions: ax.plot3D • ax.scatter3D • ax.contour3D • ax.plot_wireframe • ax.plot_surface • ax.view_init • ax.plot_trisurf", Inches(1.8), Inches(5.3), Inches(9.5), Inches(0.4),
                 size=10, bold=True, color=CYAN_PRIMARY, font="Consolas")

def build_3d_axes(slide, n):
    """Slide 6: 3D Axes Setup."""
    add_slide_header(slide, "🧊 TOPIC 01 • SECTION 1.1", "3D Axes Creation & Projection Registration", "Activating spatial 3D coordinate space using Matplotlib's mplot3d toolkit", n, VIOLET_PRIMARY)
    
    code = """import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Method 1: Subplot with 3D projection
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Method 2: Direct axes instantiation
# ax = plt.axes(projection='3d')

ax.set_xlabel('X Spatial Axis')
ax.set_ylabel('Y Spatial Axis')
ax.set_zlabel('Z Elevation Axis')
ax.set_title('Initialized 3D Spatial Canvas')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "3D Coordinate Projection Registration",
                        ["The mplot3d toolkit ships with Matplotlib and registers the '3d' projection string.",
                         "Passing projection='3d' instantiates an Axes3D object instead of standard 2D cartesian axes.",
                         "Enables a three-dimensional bounding cube with X, Y, and Z axes.",
                         "Supports interactive mouse panning, rotation, and elevation zoom by default."],
                        VIOLET_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, VIOLET_PRIMARY)
    
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "3d_axes.png", "3D Bounding Cube Initialization", VIOLET_PRIMARY)
    
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Scientific Instrument Design & Simulation",
                     "Initializing 3D volumetric bounding test chambers for wind tunnel aerodynamics and magnetic resonance imaging (MRI) coordinate calibration.",
                     "Provides the required 3D geometric frame of reference before streaming physical sensor coordinates.")

def build_3d_helix(slide, n):
    """Slide 7: 3D Helix."""
    add_slide_header(slide, "🧊 TOPIC 01 • SECTION 1.2", "Parametric 3D Helix — Lines & Scatter", "Visualizing continuous spiral curves and multi-dimensional coordinate triples", n, VIOLET_PRIMARY)
    
    code = """import numpy as np
import matplotlib.pyplot as plt

# Generate 3D Parametric Spiral Data
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)

# Scattered noisy points along the trajectory
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)

ax = plt.axes(projection='3d')
ax.plot3D(xline, yline, zline, color='#7c3aed', lw=2)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='viridis')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Parametric Lines (plot3D) & Scatter (scatter3D)",
                        ["The most fundamental 3D visual created from sets of (x, y, z) coordinate triples.",
                         "ax.plot3D(): Connects sequentially sampled points into a continuous spatial curve.",
                         "ax.scatter3D(): Projects discrete particles with independent size, opacity, and color mapping.",
                         "Depth cueing: Matplotlib adjusts marker transparency based on z-order distance."],
                        VIOLET_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, VIOLET_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "3d_helix.png", "Parametric Spiral Curve Output", VIOLET_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Biophysics & High-Energy Particle Physics (CERN)",
                     "Tracking charged subatomic particle trajectories inside magnetic cloud chambers and modeling helical DNA/protein macromolecular foldings.",
                     "2D projections fail to reveal spiral pitch and chirality; 3D rotation reveals spatial orbital drift.")

def build_3d_contour(slide, n):
    """Slide 8: 3D Contour."""
    add_slide_header(slide, "🧊 TOPIC 01 • SECTION 1.3", "Three-Dimensional Contour Plots", "Projecting elevation isolines and topographic gradients across 2D regular grids", n, VIOLET_PRIMARY)
    
    code = """def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure(figsize=(8, 6))
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Topographic Relief Contours (ax.contour3D)",
                        ["Requires input data as regular 2D grids generated by numpy.meshgrid().",
                         "ax.contour3D(X, Y, Z, levels, cmap): Connects points of identical elevation.",
                         "levels=50: High density of isolines produces a continuous relief illusion.",
                         "Ideal for potential energy fields, gravitational wells, and acoustic surfaces."],
                        VIOLET_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, VIOLET_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "3d_contour.png", "3D Sinusoidal Contour Field", VIOLET_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Meteorology & Seismic Geophysics",
                     "Mapping atmospheric isobaric pressure ridges for hurricane intensity forecasting and acoustic seismic reflection boundaries.",
                     "Enables engineers to instantly pinpoint elevation gradients and steep potential drop-offs.")

def build_3d_wireframe(slide, n):
    """Slide 9: Wireframe & Surface."""
    add_slide_header(slide, "🧊 TOPIC 01 • SECTION 1.4", "Wireframe and Surface Plots", "Generating mesh grids and continuous colored polygons with colormaps", n, VIOLET_PRIMARY)
    
    code = """fig = plt.figure(figsize=(10, 5))

# Wireframe Subplot
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_wireframe(X, Y, Z, color='black', rstride=2, cstride=2)
ax1.set_title('Wireframe Mesh')

# Filled Surface Subplot
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z, rstride=1, cstride=1,
                 cmap='viridis', edgecolor='none')
ax2.set_title('Continuous Colored Surface')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "plot_wireframe() vs plot_surface()",
                        ["ax.plot_wireframe(): Draws grid line connections without filling polygonal faces.",
                         "ax.plot_surface(): Fills polygonal faces with smooth colormapped gradients.",
                         "rstride & cstride: Control row and column step sampling density.",
                         "edgecolor='none' eliminates black boundary grid artifacts on dense surfaces."],
                        VIOLET_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, VIOLET_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "3d_wireframe_surface.png", "Wireframe vs Surface Comparison", VIOLET_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Aerospace CFD & Structural Mechanics",
                     "Modeling aerodynamic lift & drag pressure distributions over airplane wings and structural mechanical stress loads across bridge surfaces.",
                     "Wireframes allow seeing through the geometry; surface plots highlight critical stress peaks.")

def build_3d_viewinit(slide, n):
    """Slide 10: View Init."""
    add_slide_header(slide, "🧊 TOPIC 01 • SECTION 1.5", "Camera Angle Control — ax.view_init()", "Manipulating elevation and azimuthal rotation angles for optimal perspective", n, VIOLET_PRIMARY)
    
    code = """ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')

# Elevation: angle above XY plane (degrees)
# Azimuth: rotation around Z axis (degrees)
ax.view_init(elev=60, azim=35)

ax.set_title('Custom View: elev=60°, azim=35°')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Camera Perspective Manipulation (view_init)",
                        ["Default Matplotlib 3D viewing angle is elev=30°, azim=-60°.",
                         "elev (Elevation): Vertical pitch angle in degrees (0° = side view, 90° = bird's eye view).",
                         "azim (Azimuth): Horizontal rotation angle in degrees around the vertical z-axis.",
                         "Essential for eliminating occlusions where tall peaks hide valley datapoints."],
                        VIOLET_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, VIOLET_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "3d_view_init.png", "Camera Perspective Comparison", VIOLET_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Architectural Solar Studies & Defense Radar",
                     "Calibrating satellite ground station line-of-sight angles and evaluating solar panel incidence angles across urban rooftops throughout the day.",
                     "Automating view_init() loops produces animated rotation videos for executive client presentations.")

def build_3d_bar(slide, n):
    """Slide 11: 3D Bar Chart."""
    add_slide_header(slide, "🧊 TOPIC 01 • SECTION 1.6", "Three-Dimensional Bar Charts — ax.bar3d()", "Rendering volumetric columns for multi-category frequency comparisons", n, VIOLET_PRIMARY)
    
    code = """fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Anchor positions (x, y, z base)
x = [1, 2, 3, 1, 2, 3]
y = [1, 1, 1, 2, 2, 2]
z = [0, 0, 0, 0, 0, 0]

# Bar dimensions (width, depth, height)
dx = dy = [0.5] * 6
dz = [20, 35, 15, 10, 25, 30]

ax.bar3d(x, y, z, dx, dy, dz, color='#3b82f6', alpha=0.8)
ax.set_xlabel('Department'); ax.set_ylabel('Quarter')
ax.set_zlabel('Revenue ($K)')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Volumetric Column Plots (ax.bar3d)",
                        ["Requires 6 dimensional vectors: anchor (x, y, z) and spans (dx, dy, dz).",
                         "Enables comparing discrete metrics across two simultaneous categorical axes.",
                         "alpha parameter ensures behind-standing bars remain partially visible.",
                         "Colormaps can be dynamically assigned based on height (dz) values."],
                        VIOLET_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, VIOLET_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "3d_bar.png", "Volumetric Bar3D Output", VIOLET_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Financial Risk Management & Corporate Portfolios",
                     "Visualizing credit risk exposure across both industry sectors (X) and maturity years (Y) simultaneously.",
                     "Replaces complex multi-page tables with a single intuitive 3D landscape of capital risk.")

def build_3d_triangulation(slide, n):
    """Slide 12: 3D Triangulation."""
    add_slide_header(slide, "🧊 TOPIC 01 • SECTION 1.7", "Surface Triangulation — ax.plot_trisurf()", "Delaunay triangular mesh generation from unstructured spatial point clouds", n, VIOLET_PRIMARY)
    
    code = """theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))
z = np.sin(np.sqrt(x**2 + y**2))

ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z, cmap='viridis',
                edgecolor='none', linewidth=0.2)
ax.set_title('Delaunay Triangulated Surface')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Unstructured Meshing via Delaunay Triangulation",
                        ["Solves the limitation where data is not sampled on a uniform rectangular grid.",
                         "Applies the Delaunay triangulation algorithm to automatically connect nearest neighbors.",
                         "Maximizes minimum interior angles, preventing distorted sliver triangles.",
                         "Works directly with raw uneven point sets without requiring interpolation pre-processing."],
                        VIOLET_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, VIOLET_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "3d_triangulation.png", "Triangulated Mesh Surface", VIOLET_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Airborne Drone LiDAR & Autonomous Vehicle Perception",
                     "Converting unstructured point clouds from LiDAR scanners into real-time 3D terrain elevation models.",
                     "Crucial for mining volume estimation, autonomous off-road navigation, and civil land surveying.")

def build_3d_iris(slide, n):
    """Slide 13: 3D Iris Clustering."""
    add_slide_header(slide, "🧊 TOPIC 01 • SECTION 1.8", "3D Multi-Class Feature Clustering — Iris", "Separating complex multi-dimensional botanical morphometrics in 3D space", n, VIOLET_PRIMARY)
    
    code = """import seaborn as sns
iris = sns.load_dataset('iris')

ax = plt.axes(projection='3d')
colors = {'setosa': '#2563eb', 'versicolor': '#059669', 'virginica': '#dc2626'}

for species, group in iris.groupby('species'):
    ax.scatter3D(group['sepal_length'],
                 group['sepal_width'],
                 group['petal_length'],
                 c=colors[species], label=species, s=40)

ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Petal Length')
ax.legend()
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "High-Dimensional Feature Projections",
                        ["Visualizing 3 continuous features simultaneously to evaluate class separability.",
                         "Identifies linear and non-linear classification decision boundaries.",
                         "Demonstrates that Setosa is linearly separable, while Versicolor and Virginica overlap.",
                         "Directly validates feature importance before training classification algorithms."],
                        VIOLET_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, VIOLET_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "3d_iris.png", "Iris 3D Feature Clusters", VIOLET_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Biomarker Discovery & Cancer Cytology",
                     "Classifying malignant vs benign tumor cell clusters based on nuclear radius, perimeter, and texture dimensions.",
                     "Allows oncologists and ML researchers to visually confirm cluster segregation before deploying clinical AI diagnostic models.")

def build_3d_flights(slide, n):
    """Slide 14: 3D Flights."""
    add_slide_header(slide, "🧊 TOPIC 01 • SECTION 1.9", "Spatio-Temporal Surface — Flight Volumes", "Modeling airline passenger seasonality trends as a continuous 3D surface landscape", n, VIOLET_PRIMARY)
    
    code = """flights = sns.load_dataset('flights')
pivot = flights.pivot(index='month', columns='year', values='passengers')

# Month index (1-12) vs Years (1949-1960)
X, Y = np.meshgrid(np.arange(1949, 1961), np.arange(1, 13))
Z = pivot.values

ax = plt.axes(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none')
ax.set_xlabel('Year')
ax.set_ylabel('Month')
ax.set_zlabel('Passengers (1000s)')
plt.colorbar(surf, shrink=0.6)
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Spatio-Temporal Matrix Surfaces",
                        ["Transforms 2D tabular pivot matrices into continuous 3D topographic surfaces.",
                         "Reveals dual temporal trends: long-term yearly growth and repeating seasonal cycles.",
                         "Elevated ridges highlight consistent summer holiday travel surges across every decade.",
                         "Eliminates the cognitive clutter of plotting 12 separate overlapping line graphs."],
                        VIOLET_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, VIOLET_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "3d_flights_surface.png", "Seasonal Flight Surface Landscape", VIOLET_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Airline Fleet Optimization & Hotel Capacity Planning",
                     "Dynamic demand forecasting and dynamic airfare pricing based on multi-decade holiday surges.",
                     "Enables airline network planners to reposition aircraft fleets months ahead of peak demand.")

def build_basemap_divider(slide, n):
    """Slide 15: Module 2 Divider."""
    add_rounded_card(slide, Inches(1.0), Inches(1.0), Inches(11.33), Inches(5.5), fill=CARD_BG, line_color=CYAN_PRIMARY, line_width=Pt(1.5))
    add_rect(slide, Inches(1.0), Inches(1.0), Inches(11.33), Inches(0.08), fill=CYAN_PRIMARY)
    
    add_rounded_card(slide, Inches(1.8), Inches(1.8), Inches(2.2), Inches(0.35), fill=CYAN_BG, line_color=CYAN_PRIMARY)
    add_text_box(slide, "MODULE 02 • SECTION 4.1", Inches(1.8), Inches(1.86), Inches(2.2), Inches(0.24), size=10, bold=True, color=CYAN_PRIMARY, align=PP_ALIGN.CENTER)
    
    add_text_box(slide, "Geographic Data with\nBasemap & Cartopy", Inches(1.8), Inches(2.4), Inches(9.5), Inches(1.4),
                 size=38, bold=True, color=TEXT_WHITE, font="Segoe UI")
                 
    add_text_box(slide, "Exploration of planetary cartographic projection systems, geopolitical boundary layers, urban demographic scatter plots, great-circle flight navigation geodesic arcs, and modern Cartopy alternatives.", Inches(1.8), Inches(4.0), Inches(9.5), Inches(0.9),
                 size=13, color=TEXT_MUTED, font="Segoe UI")
                 
    add_rect(slide, Inches(1.8), Inches(5.1), Inches(9.5), Inches(0.02), fill=CARD_BORDER)
    add_text_box(slide, "Key Functions: Basemap • drawcoastlines • drawcountries • drawgreatcircle • Cylindrical • Mollweide • Orthographic", Inches(1.8), Inches(5.3), Inches(9.5), Inches(0.4),
                 size=10, bold=True, color=EMERALD_ACCENT, font="Consolas")

def build_basemap_intro(slide, n):
    """Slide 16: Basemap Intro."""
    add_slide_header(slide, "🗺️ TOPIC 02 • SECTION 2.1", "Geospatial Cartography Introduction", "Foundational principles of mapping latitude/longitude coordinates onto 2D projections", n, CYAN_PRIMARY)
    
    code = """from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))
# Instantiate cylindrical equidistant projection
m = Basemap(projection='cyl',
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180,
            resolution='c')

m.drawcoastlines(linewidth=0.5, color='#334155')
m.drawcountries(linewidth=0.3, color='#64748b')
m.fillcontinents(color='#1e293b', lake_color='#0b0f19')
m.drawmapboundary(fill_color='#0b0f19')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "The Geospatial Mapping Challenge",
                        ["Earth is an oblate spheroid; projecting it onto a flat 2D plane inherently introduces distortion.",
                         "Distortion trade-offs: Area vs. Shape vs. Distance vs. Direction (Tissot's Indicatrix).",
                         "Basemap wraps GEOS (geometry engine) and PROJ4 (cartographic projections).",
                         "Provides high-level layer drawing primitives: coastlines, borders, parallels, and meridians."],
                        CYAN_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, CYAN_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "basemap_cylindrical.png", "Cylindrical Projection Base Layer", CYAN_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Global Maritime Fleet Tracking & Marine Logistics",
                     "Displaying real-time AIS transponder coordinates of international cargo container vessels across shipping lanes.",
                     "Provides the geo-referenced boundary canvas required to detect vessel proximity to exclusive economic zones.")

def build_basemap_setup(slide, n):
    """Slide 17: Basemap Setup."""
    add_slide_header(slide, "🗺️ TOPIC 02 • SECTION 2.2", "Geographic Layer Composition & Topography", "Assembling geological, hydrological, and political feature boundaries", n, CYAN_PRIMARY)
    
    code = """m = Basemap(projection='mill', resolution='l')

# Vector Boundary Layers
m.drawcoastlines(linewidth=0.8, color='#06b6d4')
m.drawcountries(linewidth=0.5, color='#94a3b8')
m.drawstates(linewidth=0.3, color='#475569')
m.drawrivers(linewidth=0.4, color='#38bdf8')

# Coordinate Grids
m.drawparallels(np.arange(-90, 91, 30), labels=[1,0,0,0])
m.drawmeridians(np.arange(-180, 181, 60), labels=[0,0,0,1])

# High-Res Shaded Physical Relief
m.shadedrelief(scale=0.5)
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Layered Cartographic Composition",
                        ["resolution='c' (crude), 'l' (low), 'i' (intermediate), 'h' (high), 'f' (full).",
                         "drawparallels() & drawmeridians(): Overlays latitude and longitude reference gridlines.",
                         "shadedrelief(): Downloads and textures NASA Blue Marble elevation relief topography.",
                         "etopo(): Renders 1-arc-minute continental elevation and seafloor bathymetry."],
                        CYAN_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, CYAN_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "basemap_background_features.png", "Multi-Layer Physical Topography", CYAN_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Disaster Response & Flood Inundation Modeling",
                     "Correlating real-time river water levels and radar precipitation maps against high-resolution terrain basins.",
                     "Crucial for emergency relief agencies to identify cut-off infrastructure and deploy flood barriers.")

def build_basemap_cities(slide, n):
    """Slide 18: Basemap Cities."""
    add_slide_header(slide, "🗺️ TOPIC 02 • SECTION 2.3", "Geospatial Scatter — Global Urban Populations", "Transforming GPS geographic coordinates into projected screen pixels", n, CYAN_PRIMARY)
    
    code = """# Extracting City GPS Coordinates
lat = cities['latitude'].values
lon = cities['longitude'].values
population = cities['population'].values

# Transform GPS (lon, lat) to projection screen coordinates (x, y)
x, y = m(lon, lat)

# Scatter plot with size scaled to population
m.scatter(x, y, s=population/50000,
          c=population, cmap='YlOrRd',
          alpha=0.75, zorder=5)

plt.colorbar(label='Urban Population')
plt.title('Global Megacities Demographics')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Coordinate Transformation Engine: m(lon, lat)",
                        ["GPS coordinates use Spherical WGS84 Datum (Degrees Longitude & Latitude).",
                         "Calling m(lon, lat) computes the exact 2D projection plane coordinates (x, y) in meters.",
                         "Once transformed, standard Matplotlib commands (scatter, plot, text) overlay seamlessly.",
                         "zorder parameter controls layer stacking order above continental fills."],
                        CYAN_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, CYAN_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "basemap_cities.png", "Global Urban Population Density", CYAN_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Telecommunications & Cloud Datacenter Site Selection",
                     "Analyzing global customer density clusters to determine latency-optimal cloud server regions.",
                     "Overlays undersea fiber optic cable landing zones directly with high-density population nodes.")

def build_basemap_greatcircles(slide, n):
    """Slide 19: Basemap Great Circles."""
    add_slide_header(slide, "🗺️ TOPIC 02 • SECTION 2.4", "Great Circle Geodesic Navigation Routes", "Calculating and rendering the shortest spherical travel paths across the globe", n, CYAN_PRIMARY)
    
    code = """# New York to London
ny_lat, ny_lon = 40.7128, -74.0060
lon_lat, lon_lon = 51.5074, -0.1278

# Tokyo to Sydney
tok_lat, tok_lon = 35.6762, 139.6503
syd_lat, syd_lon = -33.8688, 151.2093

m.drawgreatcircle(ny_lon, ny_lat, lon_lon, lon_lat,
                  color='#f43f5e', linewidth=2.5,
                  label='NYC -> London')

m.drawgreatcircle(tok_lon, tok_lat, syd_lon, syd_lat,
                  color='#38bdf8', linewidth=2.5,
                  label='Tokyo -> Sydney')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Spherical Geodesics vs. Flat Map Lines",
                        ["On a flat map, straight lines are Rhumb lines — they do NOT represent shortest distance.",
                         "The true shortest distance between two spherical points is an arc along a Great Circle.",
                         "ax.drawgreatcircle() internally computes spherical trigonometry geodesic interpolation.",
                         "Curves significantly toward high latitudes (e.g., flight arcs passing over Greenland)."],
                        CYAN_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, CYAN_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "basemap_great_circle.png", "Geodesic Trans-Oceanic Flight Arcs", CYAN_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Commercial Aviation Route Planning & Fuel Optimization",
                     "Computing optimal flight paths for trans-Atlantic and trans-Pacific commercial jet routes.",
                     "Saves commercial airlines millions of gallons of aviation jet fuel annually by reducing flight miles.")

def build_basemap_projections(slide, n):
    """Slide 20: Map Projections Comparison."""
    add_slide_header(slide, "🗺️ TOPIC 02 • SECTION 2.5", "Cartographic Projection Systems Comparison", "Evaluating distortion trade-offs across Cylindrical, Mollweide, and Orthographic views", n, CYAN_PRIMARY)
    
    code = """# Cylindrical Equidistant
m1 = Basemap(projection='cyl', resolution='c')

# Mollweide (Equal-Area Pseudocylindrical)
m2 = Basemap(projection='moll', lon_0=0, resolution='c')

# Orthographic (3D Globe as seen from outer space)
m3 = Basemap(projection='ortho', lat_0=20, lon_0=80,
             resolution='c')

# Lambert Conformal Conic (Middle Latitudes)
m4 = Basemap(projection='lcc', lat_1=20, lat_2=40,
             lon_0=80, width=5E6, height=4E6)"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Classification of Map Projections",
                        ["Conformal Projections (Mercator, LCC): Preserves local angles & shapes; distorts polar area.",
                         "Equal-Area Projections (Mollweide, Albers): Preserves true area ratios; distorts shapes at edges.",
                         "Orthographic Projection: Simulates a 3D hemisphere view as viewed from deep outer space.",
                         "Choice of projection must match the analytical goal (navigational vs. thematic statistics)."],
                        CYAN_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, CYAN_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "basemap_perspective_ortho.png", "Orthographic Planetary Globe View", CYAN_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Global Climate Research & Carbon Budget Accounting",
                     "Equal-area Mollweide projections ensure carbon emission calculations are not visually biased by polar landmasses.",
                     "Prevents Greenland and Antarctica from appearing deceptively larger than the entire continent of Africa.")

def build_cartopy(slide, n):
    """Slide 21: Cartopy Modern Stack."""
    add_slide_header(slide, "🗺️ TOPIC 02 • SECTION 2.6", "Modern Geospatial Stack — Cartopy & GeoPandas", "The next-generation standard for Python geospatial data visualization", n, CYAN_PRIMARY)
    
    code = """import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1,
                     projection=ccrs.Robinson())

# Native vector feature layers
ax.add_feature(cfeature.COASTLINE, lw=0.8)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.OCEAN, color='#0f172a')
ax.gridlines(draw_labels=True)
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Why the Community Transitioned to Cartopy",
                        ["Basemap has reached official end-of-life; Cartopy is the official active successor.",
                         "Native integration with Matplotlib Axes (subclasses GeoAxes directly).",
                         "Automatic coordinate re-projection: pass transform=ccrs.PlateCarree() to any plot call.",
                         "Seamless interoperability with GeoPandas, Shapely, and xarray raster grids."],
                        CYAN_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, CYAN_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "basemap_mollweide.png", "Mollweide Global Equal-Area Map", CYAN_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Modern Web GIS & Cloud Native Geospatial Pipelines",
                     "Integrating Cloud-Optimized GeoTIFFs (COG) and OpenStreetMap vector tiles in production data pipelines.",
                     "Enables effortless multi-projection analytics without deprecation risks or manual coordinate conversion bugs.")

def build_basemap_summary(slide, n):
    """Slide 22: Basemap Decision Matrix."""
    add_slide_header(slide, "🗺️ TOPIC 02 • SECTION 2.7", "Geospatial Decision Matrix & Best Practices", "Architectural guidelines for selecting the optimal projection for spatial analytics", n, CYAN_PRIMARY)
    
    cards = [
        ("Global Thematic Studies", "Mollweide / Robinson", "Preserves relative area proportions accurately across continents.", "Global greenhouse gas budgets, population distributions, biodiversity loss indices.", CYAN_PRIMARY),
        ("Regional Navigation & GIS", "Lambert Conformal Conic", "Preserves local shapes, angles, and distances across mid-latitude zones.", "National meteorological rainfall radar, road networks, aeronautical sectional charts.", EMERALD_ACCENT),
        ("Planetary Hemisphere Views", "Orthographic", "Provides realistic 3D globe perspective as viewed from geostationary orbit.", "Satellite mission telemetry, intercontinental missile defense, global communications.", BLUE_ACCENT),
        ("Equatorial & Marine Lanes", "Mercator / Cylindrical", "Lines of constant compass heading (rhumb lines) plot as straight segments.", "Nautical maritime navigation, marine automated identification systems (AIS).", AMBER_ACCENT),
    ]
    
    for i, (cat, proj, desc, usage, accent) in enumerate(cards):
        row = i // 2
        col = i % 2
        x = Inches(0.55 + col * 6.2)
        y = Inches(1.6 + row * 2.7)
        w = Inches(5.95)
        h = Inches(2.45)
        
        card = add_rounded_card(slide, x, y, w, h, fill=CARD_BG, line_color=CARD_BORDER)
        add_rect(slide, x, y, Inches(0.05), h, fill=accent)
        
        add_text_box(slide, cat, x + Inches(0.2), y + Inches(0.12), w - Inches(0.4), Inches(0.28), size=11, bold=True, color=accent)
        add_text_box(slide, f"Standard Projection: {proj}", x + Inches(0.2), y + Inches(0.42), w - Inches(0.4), Inches(0.22), size=9.5, bold=True, color=TEXT_WHITE)
        add_text_box(slide, desc, x + Inches(0.2), y + Inches(0.70), w - Inches(0.4), Inches(0.70), size=9, color=TEXT_MUTED)
        
        add_rounded_card(slide, x + Inches(0.2), y + Inches(1.5), w - Inches(0.4), Inches(0.75), fill=RGBColor(0x0C, 0x12, 0x20), line_color=CARD_BORDER)
        add_text_box(slide, f"🎯 Practical Use Case:\n{usage}", x + Inches(0.3), y + Inches(1.58), w - Inches(0.6), Inches(0.6), size=8.5, color=TEXT_WHITE)

def build_seaborn_divider(slide, n):
    """Slide 23: Module 3 Divider."""
    add_rounded_card(slide, Inches(1.0), Inches(1.0), Inches(11.33), Inches(5.5), fill=CARD_BG, line_color=ROSE_PRIMARY, line_width=Pt(1.5))
    add_rect(slide, Inches(1.0), Inches(1.0), Inches(11.33), Inches(0.08), fill=ROSE_PRIMARY)
    
    add_rounded_card(slide, Inches(1.8), Inches(1.8), Inches(2.2), Inches(0.35), fill=ROSE_BG, line_color=ROSE_PRIMARY)
    add_text_box(slide, "MODULE 03 • SECTION 5.1", Inches(1.8), Inches(1.86), Inches(2.2), Inches(0.24), size=10, bold=True, color=ROSE_PRIMARY, align=PP_ALIGN.CENTER)
    
    add_text_box(slide, "Statistical Data Visualization\nwith Seaborn", Inches(1.8), Inches(2.4), Inches(9.5), Inches(1.4),
                 size=38, bold=True, color=TEXT_WHITE, font="Segoe UI")
                 
    add_text_box(slide, "Elevating exploratory data analysis: high-level declarative syntax, automated statistical aggregation, kernel density estimation, multi-dimensional pairplots, categorical distributions, and linear regression models.", Inches(1.8), Inches(4.0), Inches(9.5), Inches(0.9),
                 size=13, color=TEXT_MUTED, font="Segoe UI")
                 
    add_rect(slide, Inches(1.8), Inches(5.1), Inches(9.5), Inches(0.02), fill=CARD_BORDER)
    add_text_box(slide, "Key Functions: sns.histplot • sns.kdeplot • sns.jointplot • sns.pairplot • sns.catplot • sns.heatmap • sns.lmplot", Inches(1.8), Inches(5.3), Inches(9.5), Inches(0.4),
                 size=10, bold=True, color=AMBER_ACCENT, font="Consolas")

def build_seaborn_intro(slide, n):
    """Slide 24: Seaborn Philosophy."""
    add_slide_header(slide, "📊 TOPIC 03 • SECTION 3.1", "Seaborn Design Philosophy & Architecture", "The declarative grammar of statistical data exploration in Python", n, ROSE_PRIMARY)
    
    code = """import seaborn as sns
import matplotlib.pyplot as plt

# Declarative API: specify WHAT to plot, not HOW to draw it
tips = sns.load_dataset('tips')

sns.relplot(
    data=tips,
    x='total_bill', y='tip',
    hue='time', size='size', style='sex',
    col='day', col_wrap=2,
    palette='magma'
)
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Why Seaborn Built Upon Matplotlib",
                        ["Matplotlib is imperative (requires explicit loops, color assignments, legend hooks).",
                         "Seaborn is declarative: directly consumes tidy DataFrames via columns (x, y, hue, col).",
                         "Built-in statistical aggregation: computes confidence intervals and error bars automatically.",
                         "Modern aesthetic defaults: sophisticated color palettes, integrated grid layout systems."],
                        ROSE_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, ROSE_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "seaborn_catplot.png", "Declarative Faceted Subplots", ROSE_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Customer Churn & Behavioral Economics",
                     "Rapid exploratory data analysis (EDA) investigating how multiple customer variables interact across segments.",
                     "Reduces 50 lines of tedious Matplotlib code into a single 4-line expressive declarative statement.")

def build_seaborn_hist_kde(slide, n):
    """Slide 25: Histograms & KDE."""
    add_slide_header(slide, "📊 TOPIC 03 • SECTION 3.2", "Univariate Distributions — Histograms & KDE", "Estimating continuous probability density functions from empirical observations", n, ROSE_PRIMARY)
    
    code = """import seaborn as sns
import matplotlib.pyplot as plt

data = np.random.randn(1000)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
# Histogram with KDE overlay
sns.histplot(data, kde=True, color='#f43f5e',
             bins=30, ax=axes[0])
axes[0].set_title('Histogram + Gaussian KDE')

# Cumulative & Rug Distribution
sns.kdeplot(data, fill=True, color='#06b6d4',
            cumulative=True, ax=axes[1])
sns.rugplot(data, color='#38bdf8', ax=axes[1])
axes[1].set_title('Cumulative Probability Density')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Kernel Density Estimation (KDE) Mechanics",
                        ["Histograms depend heavily on bin edge placement and bin width selection.",
                         "KDE centers a smooth Gaussian kernel curve at every empirical sample point.",
                         "Summing all individual kernels yields a continuous probability density curve.",
                         "rugplot() adds tick marks at the bottom, directly indicating raw data density."],
                        ROSE_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, ROSE_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "seaborn_histplot_kde.png", "Histograms & KDE Density Curves", ROSE_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Algorithmic Trading & Asset Return Volatility",
                     "Evaluating stock market return distributions to test for heavy tails, skewness, and black-swan outliers.",
                     "Prevents quantitative risk models from underestimating catastrophic market liquidation events.")

def build_seaborn_jointplot(slide, n):
    """Slide 26: Jointplot."""
    add_slide_header(slide, "📊 TOPIC 03 • SECTION 3.3", "Bivariate Relationships — sns.jointplot()", "Combining central scatter/hexbin plots with marginal univariate density curves", n, ROSE_PRIMARY)
    
    code = """import seaborn as sns
iris = sns.load_dataset('iris')

# Hexagonal Binning with Marginal Histograms
g = sns.jointplot(
    data=iris,
    x='sepal_length', y='sepal_width',
    kind='hex', cmap='plasma',
    marginal_kws=dict(bins=20, fill=True)
)
g.fig.suptitle('Hexbin Density with Marginal Distributions')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Joint & Marginal Distribution Geometry",
                        ["Simultaneously visualizes the 2D joint relationship and 1D marginals on the axes.",
                         "kind='hex': Replaces overlapping point scatter with hexagonal density accumulation.",
                         "kind='kde': Produces smooth 2D elevation contour isolines of probability density.",
                         "Eliminates scatter overplotting when analyzing large datasets (100,000+ points)."],
                        ROSE_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, ROSE_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "seaborn_jointplot.png", "Jointplot Hexbin Bivariate Output", ROSE_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "E-Commerce Pricing Optimization & Cart Value",
                     "Analyzing the correlation between marketing ad spend (X) and average order revenue (Y).",
                     "Hexagonal bins immediately highlight the highest-density conversion sweet spots.")

def build_seaborn_pairplot(slide, n):
    """Slide 27: Pairplot."""
    add_slide_header(slide, "📊 TOPIC 03 • SECTION 3.4", "Multi-Feature Matrices — sns.pairplot()", "Generating N×N pairwise feature scatter matrices across class categories", n, ROSE_PRIMARY)
    
    code = """import seaborn as sns
iris = sns.load_dataset('iris')

# Full N x N Feature Scatter & Density Matrix
sns.pairplot(
    data=iris,
    hue='species',
    palette='Set1',
    diag_kind='kde',
    markers=['o', 's', 'D'],
    plot_kws={'alpha': 0.8}
)
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Pairwise Feature Correlation Matrices",
                        ["Automatically renders all N×N pairwise bivariate combinations across continuous features.",
                         "Diagonal plots: Display univariate KDE distribution for each individual feature.",
                         "Off-diagonal plots: Show pairwise scatter relationships to reveal feature correlations.",
                         "hue='species': Color-codes points by categorical label to show cluster separation."],
                        ROSE_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, ROSE_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "seaborn_pairplot.png", "Pairplot Feature Matrix Grid", ROSE_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Clinical Pharmacology & Drug Discovery Screening",
                     "Screening hundreds of molecular chemical compound properties against therapeutic target efficacy.",
                     "Identifies collinear features immediately, enabling machine learning engineers to prune redundant variables.")

def build_seaborn_catplot(slide, n):
    """Slide 28: Categorical Plots."""
    add_slide_header(slide, "📊 TOPIC 03 • SECTION 3.5", "Categorical Distributions — Box, Violin & Strip", "Comparing continuous variable distributions across categorical grouping levels", n, ROSE_PRIMARY)
    
    code = """tips = sns.load_dataset('tips')

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Boxplot with Quartiles & Outliers
sns.boxplot(data=tips, x='day', y='total_bill',
            hue='smoker', palette='Blues', ax=axes[0])
axes[0].set_title('Boxplot: Quartiles & Whiskers')

# Violinplot with Embedded KDE
sns.violinplot(data=tips, x='day', y='total_bill',
               hue='sex', split=True, palette='Pastel1',
               ax=axes[1])
axes[1].set_title('Violinplot: Split Probability Density')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Categorical Distribution Modalities",
                        ["Boxplot: Encodes 5-number summary (Min, Q1, Median, Q3, Max) and identifies IQR outliers.",
                         "Violinplot: Combines boxplot with mirrored KDE curves to reveal bimodal distributions.",
                         "split=True: Folds two category halves together for direct visual comparison.",
                         "catplot(): Universal entry point for box, violin, strip, swarm, and bar charts."],
                        ROSE_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, ROSE_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "seaborn_catplot.png", "Categorical Box & Violin Comparisons", ROSE_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Healthcare Hospital Operations & Patient Wait Times",
                     "Comparing patient emergency room wait times across hospital triage categories and shifts.",
                     "Violin plots reveal bimodal distributions that single-number averages (means) completely conceal.")

def build_seaborn_heatmap(slide, n):
    """Slide 29: Heatmaps."""
    add_slide_header(slide, "📊 TOPIC 03 • SECTION 3.6", "Correlation Matrices & Heatmaps — sns.heatmap()", "Visualizing multidimensional correlation coefficients and tabular intensity grids", n, ROSE_PRIMARY)
    
    code = """flights = sns.load_dataset('flights')
pivot = flights.pivot(index='month', columns='year',
                      values='passengers')

plt.figure(figsize=(9, 6))
sns.heatmap(
    pivot,
    annot=True, fmt='d',
    cmap='YlGnBu',
    linewidths=0.5, linecolor='#1e293b',
    cbar_kws={'label': 'Passenger Count (1000s)'}
)
plt.title('Monthly Flight Passenger Volume Heatmap')
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Matrix Intensity & Correlation Mapping",
                        ["Takes 2D matrix arrays and encodes numerical magnitudes as color gradients.",
                         "annot=True overlays numerical cell values directly inside each rectangle.",
                         "fmt='d' formats integers; fmt='.2f' formats continuous correlation Pearson coefficients.",
                         "linewidths=0.5 draws subtle boundary lines to distinguish adjacent cell values."],
                        ROSE_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, ROSE_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "seaborn_heatmap.png", "Faceted Flight Matrix Heatmap", ROSE_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Genomic Microarray Expression & FinTech Correlations",
                     "Computing Pearson correlation matrices across thousands of financial equities to construct diversified investment portfolios.",
                     "Instantly reveals highly correlated asset pairs to eliminate systemic risk exposure.")

def build_seaborn_lmplot(slide, n):
    """Slide 30: Linear Regression LMPlot."""
    add_slide_header(slide, "📊 TOPIC 03 • SECTION 3.7", "Linear Regression & Residuals — sns.lmplot()", "Fitting ordinary least squares regression models with statistical confidence bands", n, ROSE_PRIMARY)
    
    code = """tips = sns.load_dataset('tips')

# Faceted Linear Regression with 95% Confidence Band
sns.lmplot(
    data=tips,
    x='total_bill', y='tip',
    hue='smoker', col='time',
    markers=['o', 'x'],
    palette='Set1',
    scatter_kws={'alpha': 0.6},
    ci=95  # 95% Bootstrap Confidence Interval
)
plt.show()"""

    add_definition_card(slide, Inches(0.55), Inches(1.5), Inches(5.85), Inches(2.0),
                        "Statistical Regression Modeling with Confidence Intervals",
                        ["Combines regplot() with FacetGrid to plot linear models across categorical subsets.",
                         "Automatically estimates regression slope, intercept, and translucent 95% bootstrap confidence bands.",
                         "col & row arguments break the dataset into separate regression subplots automatically.",
                         "order=2 fits polynomial curves; robust=True down-weights outlier influence."],
                        ROSE_PRIMARY)
                        
    add_code_card(slide, Inches(0.55), Inches(3.6), Inches(5.85), Inches(3.4), code, ROSE_PRIMARY)
    add_output_card(slide, Inches(6.65), Inches(1.5), Inches(6.15), Inches(3.4), "seaborn_lmplot.png", "Faceted Linear Regression with CI", ROSE_PRIMARY)
    add_usecase_card(slide, Inches(6.65), Inches(5.05), Inches(6.15), Inches(1.95),
                     "Predictive Marketing Attribution & Customer LTV",
                     "Estimating customer lifetime value (LTV) growth as a function of initial acquisition discount tier.",
                     "Confidence bands signal exactly where sample sizes are too small to support business decisions.")

def build_seaborn_palettes(slide, n):
    """Slide 31: Color Palettes."""
    add_slide_header(slide, "📊 TOPIC 03 • SECTION 3.8", "Scientific Color Palettes & Accessible Design", "Color theory guidelines for continuous, diverging, and categorical visualizations", n, ROSE_PRIMARY)
    
    palettes = [
        ("Qualitative / Categorical", "Set1, deep, pastel, dark", "Unordered discrete classes with distinct hues but equal visual luminance.", "Species classification, geographical regions, departmental divisions.", ROSE_PRIMARY),
        ("Sequential / Continuous", "mako, rocket, viridis, Blues", "Ordered numeric metrics progressing smoothly from light to dark.", "Density heatmaps, population volume, elevation topography.", CYAN_PRIMARY),
        ("Diverging / Polarizing", "coolwarm, vlag, seismic", "Highlighting positive vs negative deviation from a neutral critical center.", "Stock market profit/loss, temperature anomaly above/below historical baseline.", AMBER_ACCENT),
        ("Colorblind Accessible", "colorblind, cmocean, plasma", "Perceptually uniform color sequences optimized for deuteranopia & protanopia.", "Official scientific publishing, medical interfaces, executive dashboards.", EMERALD_ACCENT),
    ]
    
    for i, (cat, examples, desc, usage, accent) in enumerate(palettes):
        row = i // 2
        col = i % 2
        x = Inches(0.55 + col * 6.2)
        y = Inches(1.6 + row * 2.7)
        w = Inches(5.95)
        h = Inches(2.45)
        
        card = add_rounded_card(slide, x, y, w, h, fill=CARD_BG, line_color=CARD_BORDER)
        add_rect(slide, x, y, Inches(0.05), h, fill=accent)
        
        add_text_box(slide, cat, x + Inches(0.2), y + Inches(0.12), w - Inches(0.4), Inches(0.28), size=11, bold=True, color=accent)
        add_text_box(slide, f"Standard Palettes: {examples}", x + Inches(0.2), y + Inches(0.42), w - Inches(0.4), Inches(0.22), size=9.5, bold=True, color=TEXT_WHITE)
        add_text_box(slide, desc, x + Inches(0.2), y + Inches(0.70), w - Inches(0.4), Inches(0.70), size=9, color=TEXT_MUTED)
        
        add_rounded_card(slide, x + Inches(0.2), y + Inches(1.5), w - Inches(0.4), Inches(0.75), fill=RGBColor(0x0C, 0x12, 0x20), line_color=CARD_BORDER)
        add_text_box(slide, f"🎯 Typical Application:\n{usage}", x + Inches(0.3), y + Inches(1.58), w - Inches(0.6), Inches(0.6), size=8.5, color=TEXT_WHITE)

def build_seaborn_gallery(slide, n):
    """Slide 32: Seaborn Multi-Plot Visual Gallery."""
    add_slide_header(slide, "📊 TOPIC 03 • SECTION 3.9", "Seaborn Multi-Plot Visual Gallery", "Comprehensive catalog of Seaborn figure-level and axes-level statistical functions", n, ROSE_PRIMARY)
    
    # 4 miniature gallery cards with images
    gallery_items = [
        ("seaborn_histplot_kde.png", "Histograms & Density Estimation", "sns.histplot & sns.kdeplot"),
        ("seaborn_jointplot.png", "Bivariate Relationships & Hexbins", "sns.jointplot(kind='hex')"),
        ("seaborn_catplot.png", "Categorical Facets & Violin Splits", "sns.catplot(kind='violin')"),
        ("seaborn_heatmap.png", "Faceted Matrices & Heatmaps", "sns.heatmap(annot=True)"),
    ]
    
    for i, (img_name, title, func) in enumerate(gallery_items):
        row = i // 2
        col = i % 2
        x = Inches(0.55 + col * 6.2)
        y = Inches(1.55 + row * 2.75)
        w = Inches(5.95)
        h = Inches(2.55)
        
        card = add_rounded_card(slide, x, y, w, h, fill=CARD_BG, line_color=CARD_BORDER)
        add_text_box(slide, title, x + Inches(0.2), y + Inches(0.1), w - Inches(0.4), Inches(0.24), size=10, bold=True, color=TEXT_WHITE)
        add_text_box(slide, func, x + Inches(0.2), y + Inches(0.32), w - Inches(0.4), Inches(0.20), size=8.5, color=ROSE_PRIMARY)
        
        path = img(img_name)
        if path:
            add_image_fit(slide, path, x + Inches(0.2), y + Inches(0.55), w - Inches(0.4), h - Inches(0.68))

def build_seaborn_summary(slide, n):
    """Slide 33: Seaborn Best Practices."""
    add_slide_header(slide, "📊 TOPIC 03 • SECTION 3.10", "Seaborn Best Practices & Architecture", "Engineering guidelines for clean statistical reporting and publication-grade figures", n, ROSE_PRIMARY)
    
    best_practices = [
        ("Figure-Level vs Axes-Level", "Understand the difference: relplot, catplot, lmplot create their own FacetGrid figures; scatterplot, boxplot, histplot draw directly onto existing Matplotlib axes.", ROSE_PRIMARY),
        ("Tidy Data Formatting", "Always reshape wide tables into tidy long-form DataFrames using pandas.melt() before plotting in Seaborn.", CYAN_PRIMARY),
        ("Perceptual Color Consistency", "Never use qualitative palettes for continuous data; verify that your color schemes pass accessibility checks.", AMBER_ACCENT),
        ("Statistical Integrity", "State confidence intervals explicitly (e.g. ci=95); never hide high variance by showing only bar means without error bars.", EMERALD_ACCENT),
    ]
    
    for i, (title, desc, accent) in enumerate(best_practices):
        y = Inches(1.6 + i * 1.3)
        add_rounded_card(slide, Inches(0.55), y, Inches(12.23), Inches(1.12), fill=CARD_BG, line_color=CARD_BORDER)
        add_rect(slide, Inches(0.55), y, Inches(0.06), Inches(1.12), fill=accent)
        add_text_box(slide, f"✓  {title}", Inches(0.8), y + Inches(0.15), Inches(11.8), Inches(0.3), size=12, bold=True, color=accent)
        add_text_box(slide, desc, Inches(0.8), y + Inches(0.48), Inches(11.8), Inches(0.5), size=10, color=TEXT_WHITE)

def build_comparison_table(slide, n):
    """Slide 34: 3-Way Library Comparison Matrix."""
    add_slide_header(slide, "⚖️ BENCHMARK MATRIX", "Matplotlib 3D vs. Basemap/Cartopy vs. Seaborn", "Comparative architectural trade-offs across all three seminar visual libraries", n, BLUE_ACCENT)
    
    headers = ["Evaluation Metric", "Matplotlib 3D (mplot3d)", "Basemap & Cartopy", "Seaborn"]
    col_widths = [Inches(2.8), Inches(3.1), Inches(3.1), Inches(3.1)]
    
    rows = [
        ("Primary Domain", "Spatial 3D & Volumetric Surfaces", "Geographic & Geodesic GIS Mapping", "Statistical Multi-Variable Distributions"),
        ("Data Structure", "(x, y, z) Triples & 2D Meshgrids", "GPS (Lat, Lon) & GeoJSON Geometries", "Tidy Long-Form Pandas DataFrames"),
        ("API Abstraction", "Low-Level Imperative Canvas", "Mid-Level Projection Coordinates", "High-Level Declarative Semantic Grammar"),
        ("Strengths", "Full 3D rotation, wireframes, Delaunay", "Accurate cartographic transforms, coastlines", "Automated confidence intervals, aesthetics"),
        ("Limitations", "Complex layout code, static in print", "Basemap deprecated; requires Cartopy", "2D only; lacks native 3D spatial surfaces"),
        ("Ideal Use Case", "CFD simulation, biophysics trajectories", "Logistics routing, global climate models", "Exploratory data analysis, ML feature diagnostics")
    ]
    
    y_start = Inches(1.6)
    row_h = Inches(0.42)
    header_h = Inches(0.45)
    
    # Table Header
    cur_x = Inches(0.6)
    for j, h in enumerate(headers):
        add_rounded_card(slide, cur_x, y_start, col_widths[j], header_h, fill=RGBColor(0x1B, 0x25, 0x3D), line_color=CARD_BORDER)
        add_text_box(slide, h, cur_x + Inches(0.1), y_start + Inches(0.1), col_widths[j] - Inches(0.2), Inches(0.3),
                     size=10, bold=True, color=TEXT_WHITE if j > 0 else CYAN_PRIMARY, align=PP_ALIGN.CENTER if j > 0 else PP_ALIGN.LEFT)
        cur_x += col_widths[j] + Inches(0.05)
        
    # Table Rows
    for i, r in enumerate(rows):
        cur_x = Inches(0.6)
        row_y = y_start + header_h + Inches(0.06) + i * (row_h + Inches(0.04))
        for j, val in enumerate(r):
            fill = CARD_BG if i % 2 == 0 else RGBColor(0x0E, 0x14, 0x24)
            add_rounded_card(slide, cur_x, row_y, col_widths[j], row_h, fill=fill, line_color=CARD_BORDER)
            color = TEXT_WHITE if j == 0 else TEXT_MUTED
            bold = True if j == 0 else False
            add_text_box(slide, val, cur_x + Inches(0.1), row_y + Inches(0.08), col_widths[j] - Inches(0.2), Inches(0.28),
                         size=8.8, bold=bold, color=color, align=PP_ALIGN.CENTER if j > 0 else PP_ALIGN.LEFT)
            cur_x += col_widths[j] + Inches(0.05)

def build_qr_code_slide(slide, n):
    """Slide 35: QR Resources."""
    add_slide_header(slide, "📱 INTERACTIVE RESOURCES", "Interactive Web Demos & Presentation Videos", "Scan QR codes with any smartphone camera for instant mobile access", n, EMERALD_ACCENT)
    
    qrs = [
        ("qr_ppt_download.png", "Download Seminar PPTX", "Official 36-Slide PPTX Presentation", "download-ppt.html", AMBER_ACCENT),
        ("qr_english_video.png", "English Presentation", "Full 7-min HD 3D Video Narration", "video-english.html", BLUE_ACCENT),
        ("qr_tanglish_video.png", "Tanglish Presentation", "Full 3D Presentation in Tamil + English", "video-tanglish.html", VIOLET_PRIMARY),
        ("qr_interactive_deck.png", "Interactive 3D Web Deck", "Live WebGL 3D Rotation on Mobile", "index.html", CYAN_PRIMARY),
    ]
    
    for i, (filename, title, desc, path_slug, accent_col) in enumerate(qrs):
        x = Inches(0.55 + i * 3.1)
        y = Inches(1.6)
        w = Inches(2.95)
        h = Inches(5.3)
        
        card = add_rounded_card(slide, x, y, w, h, fill=CARD_BG, line_color=CARD_BORDER)
        add_rect(slide, x, y, w, Inches(0.06), fill=accent_col)
        
        # Pure white container tile for the QR code for maximum contrast and instant camera lock
        qr_tile_size = Inches(2.45)
        qr_x = x + Inches(0.25)
        qr_y = y + Inches(0.25)
        add_rounded_card(slide, qr_x, qr_y, qr_tile_size, qr_tile_size, fill=RGBColor(0xFF, 0xFF, 0xFF), line_color=RGBColor(0xE2, 0xE8, 0xF0))
        
        # QR Image inside the white tile with comfortable quiet zone
        img_p = img(filename)
        if img_p:
            add_image_fit(slide, img_p, qr_x + Inches(0.12), qr_y + Inches(0.12), qr_tile_size - Inches(0.24), qr_tile_size - Inches(0.24))
            
        add_text_box(slide, title, x + Inches(0.1), y + Inches(2.85), Inches(2.75), Inches(0.38),
                     size=11.5, bold=True, color=TEXT_WHITE, align=PP_ALIGN.CENTER)
        add_text_box(slide, desc, x + Inches(0.1), y + Inches(3.25), Inches(2.75), Inches(0.55),
                     size=8.8, color=TEXT_MUTED, align=PP_ALIGN.CENTER)
                     
        # Scan prompt pill
        add_rounded_card(slide, x + Inches(0.2), y + Inches(3.95), Inches(2.55), Inches(1.05), fill=RGBColor(0x0C, 0x14, 0x24), line_color=CARD_BORDER)
        add_text_box(slide, "📷 SCAN WITH PHONE", x + Inches(0.2), y + Inches(4.05), Inches(2.55), Inches(0.28),
                     size=9, bold=True, color=accent_col, align=PP_ALIGN.CENTER)
        add_text_box(slide, f"gurup7029-coder.github.io\n/.../{path_slug}", x + Inches(0.2), y + Inches(4.35), Inches(2.55), Inches(0.55),
                     size=7.5, color=TEXT_MUTED, align=PP_ALIGN.CENTER)

def build_final(slide, n):
    """Slide 36: Thank You / Conclusion."""
    add_rounded_card(slide, Inches(1.0), Inches(1.0), Inches(11.33), Inches(5.5), fill=CARD_BG, line_color=VIOLET_PRIMARY, line_width=Pt(1.5))
    add_rect(slide, Inches(1.0), Inches(1.0), Inches(11.33), Inches(0.08), fill=VIOLET_PRIMARY)
    
    add_text_box(slide, "Thank You!", Inches(1.5), Inches(1.6), Inches(10.33), Inches(0.9),
                 size=46, bold=True, color=TEXT_WHITE, align=PP_ALIGN.CENTER, font="Segoe UI")
                 
    add_text_box(slide, "Data Visualization in Python Seminar • Master Practical Presentation", Inches(1.5), Inches(2.6), Inches(10.33), Inches(0.4),
                 size=14, bold=True, color=CYAN_PRIMARY, align=PP_ALIGN.CENTER, font="Segoe UI")
                 
    # Summary highlights card
    add_rounded_card(slide, Inches(2.0), Inches(3.2), Inches(9.33), Inches(2.2), fill=RGBColor(0x0E, 0x15, 0x26), line_color=CARD_BORDER)
    
    summary_bullets = [
        "✓ 3D Plotting: Spatial coordinates, parametric spirals, and Delaunay meshes illuminate complex geometries.",
        "✓ Basemap & Cartopy: Precise cartographic projections reveal planetary phenomena without geographical distortion.",
        "✓ Seaborn: Declarative statistical graphics turn raw exploratory data into actionable predictive insights.",
        "✓ Mastered the unified workflow connecting data engineering, statistical modeling, and executive storytelling."
    ]
    for idx, sb in enumerate(summary_bullets):
        add_text_box(slide, sb, Inches(2.3), Inches(3.4 + idx * 0.45), Inches(8.8), Inches(0.38),
                     size=10.5, color=TEXT_WHITE)
                     
    add_text_box(slide, "Presenter: Guruprasath B (7376242AD131) • Bannari Amman Institute of Technology (BIT)", Inches(1.5), Inches(5.8), Inches(10.33), Inches(0.35),
                 size=10.5, color=TEXT_MUTED, align=PP_ALIGN.CENTER)

# ═══════════════════════════════════════════════════════════════════════════════
# BUILD ALL SLIDES
# ═══════════════════════════════════════════════════════════════════════════════

builders = [
    build_cover,               # 1
    build_toc,                 # 2
    build_datasets_overview,   # 3
    build_dataset_samples,     # 4
    build_3d_divider,          # 5
    build_3d_axes,             # 6
    build_3d_helix,            # 7
    build_3d_contour,          # 8
    build_3d_wireframe,        # 9
    build_3d_viewinit,         # 10
    build_3d_bar,              # 11
    build_3d_triangulation,    # 12
    build_3d_iris,             # 13
    build_3d_flights,          # 14
    build_basemap_divider,     # 15
    build_basemap_intro,       # 16
    build_basemap_setup,       # 17
    build_basemap_cities,      # 18
    build_basemap_greatcircles,# 19
    build_basemap_projections, # 20
    build_cartopy,             # 21
    build_basemap_summary,     # 22
    build_seaborn_divider,     # 23
    build_seaborn_intro,       # 24
    build_seaborn_hist_kde,    # 25
    build_seaborn_jointplot,   # 26
    build_seaborn_pairplot,    # 27
    build_seaborn_catplot,     # 28
    build_seaborn_heatmap,     # 29
    build_seaborn_lmplot,      # 30
    build_seaborn_palettes,    # 31
    build_seaborn_gallery,     # 32
    build_seaborn_summary,     # 33
    build_comparison_table,    # 34
    build_qr_code_slide,       # 35
    build_final,               # 36
]

print(f"Building {len(builders)} enhanced AI-themed slides...")
for i, builder in enumerate(builders, 1):
    sl = blank_slide(transition_type="fade")
    builder(sl, i)
    print(f"  [OK] Slide {i:02d}/{len(builders):02d}: {builder.__name__}")

try:
    prs.save(OUT_FILE)
    print(f"\nDone! Primary presentation saved to:\n   {OUT_FILE}")
except Exception as e:
    print(f"Could not save to {OUT_FILE}: {e}")

prs.save(ENHANCED_FILE)
print(f"Done! Enhanced presentation saved to:\n   {ENHANCED_FILE}")
print(f"Total slides generated: {len(prs.slides)}")
