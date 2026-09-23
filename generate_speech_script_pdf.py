import os
import sys
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

BASE_DIR = r"E:\sem3\data science\seminar"
PDF_OUTPUT = os.path.join(BASE_DIR, "Data_Visualization_Seminar_Speech_Script.pdf")

# Custom Canvas for Running Headers and "Page X of Y" Footers
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        # Don't draw on cover page (Page 1)
        if self._pageNumber == 1:
            return
            
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Running Top Header
        self.drawString(54, A4[1] - 36, "DATA VISUALIZATION IN PYTHON — SEMINAR SPEECH SCRIPT")
        self.drawRightString(A4[0] - 54, A4[1] - 36, "MASTER MCA PRESENTATION")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.75)
        self.line(54, A4[1] - 42, A4[0] - 54, A4[1] - 42)
        
        # Running Bottom Footer
        self.line(54, 46, A4[0] - 54, 46)
        self.setFont("Helvetica", 8)
        self.drawString(54, 34, "Presenter: Guru Prakash A (Reg No: 25322011) • Dept. of Computer Science & Applications")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(A4[0] - 54, 34, page_str)
        self.restoreState()

def build_pdf():
    print(f"Generating Master Presentation Speech Script PDF: {PDF_OUTPUT}...")
    
    doc = SimpleDocTemplate(
        PDF_OUTPUT,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Color Palette Tokens
    NAVY_MAIN = colors.HexColor("#0F172A")
    BLUE_PRIMARY = colors.HexColor("#2563EB")
    PURPLE_ACCENT = colors.HexColor("#7C3AED")
    AMBER_ACCENT = colors.HexColor("#D97706")
    EMERALD_ACCENT = colors.HexColor("#059669")
    SLATE_MUTED = colors.HexColor("#475569")
    BG_LIGHT_BLUE = colors.HexColor("#F0F6FE")
    BG_LIGHT_AMBER = colors.HexColor("#FEF7ED")
    BG_LIGHT_PURPLE = colors.HexColor("#F8F5FF")
    BG_CODE = colors.HexColor("#F8FAFC")
    BORDER_SUBTLE = colors.HexColor("#E2E8F0")

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=NAVY_MAIN,
        alignment=0,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=16,
        textColor=BLUE_PRIMARY,
        alignment=0,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=NAVY_MAIN,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=BLUE_PRIMARY,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14.5,
        textColor=NAVY_MAIN,
        spaceAfter=6
    )

    speech_style = ParagraphStyle(
        'SpeechQuote',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=15,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=6
    )

    cue_style = ParagraphStyle(
        'StageCue',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#9333EA")
    )

    def_title_style = ParagraphStyle(
        'DefTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#1D4ED8")
    )

    def_body_style = ParagraphStyle(
        'DefBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        textColor=colors.HexColor("#1E293B")
    )

    example_title_style = ParagraphStyle(
        'ExampleTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#B45309")
    )

    code_style = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#0F172A")
    )

    qa_q_style = ParagraphStyle(
        'QAQuestion',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=NAVY_MAIN,
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )

    qa_a_style = ParagraphStyle(
        'QAAnswer',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=14,
        textColor=colors.HexColor("#334155"),
        spaceAfter=6
    )

    story = []

    # Helper: Speech Block Card
    def add_speech_card(cue_text, speech_text):
        content = [
            Paragraph(f"<b>ACTION / CUE:</b> {cue_text}", cue_style),
            Spacer(1, 4),
            Paragraph(f'"{speech_text}"', speech_style)
        ]
        t = Table([[content]], colWidths=[A4[0] - 108])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
            ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor("#CBD5E1")),
            ('LINELEFT', (0, 0), (0, -1), 3.5, colors.HexColor("#3B82F6")),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ]))
        story.append(t)
        story.append(Spacer(1, 8))

    # Helper: Definition Card
    def add_definition_box(title, text):
        content = [
            Paragraph(f"📖 <b>FORMAL DEFINITION:</b> {title}", def_title_style),
            Spacer(1, 3),
            Paragraph(text, def_body_style)
        ]
        t = Table([[content]], colWidths=[A4[0] - 108])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), BG_LIGHT_BLUE),
            ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor("#93C5FD")),
            ('LINELEFT', (0, 0), (0, -1), 3.5, colors.HexColor("#2563EB")),
            ('TOPPADDING', (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ]))
        story.append(t)
        story.append(Spacer(1, 8))

    # Helper: Real-World Use Case Card
    def add_example_box(title, text):
        content = [
            Paragraph(f"💡 <b>INDUSTRY EXAMPLE & USE CASE:</b> {title}", example_title_style),
            Spacer(1, 3),
            Paragraph(text, def_body_style)
        ]
        t = Table([[content]], colWidths=[A4[0] - 108])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), BG_LIGHT_AMBER),
            ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor("#FCD34D")),
            ('LINELEFT', (0, 0), (0, -1), 3.5, colors.HexColor("#D97706")),
            ('TOPPADDING', (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ]))
        story.append(t)
        story.append(Spacer(1, 8))

    # Helper: Code Snippet Card
    def add_code_card(code_text):
        content = [Paragraph(code_text.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style)]
        t = Table([[content]], colWidths=[A4[0] - 108])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), BG_CODE),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ]))
        story.append(t)
        story.append(Spacer(1, 8))

    # ═══════════════════════════════════════════════════════════════════════════
    # COVER / HEADER BANNER
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(Paragraph("Data Visualization in Python", title_style))
    story.append(Paragraph("Complete Professional Seminar Speech Script • Master Technical Walkthrough", subtitle_style))
    
    # Metadata Table
    meta_data = [
        [
            Paragraph("<b>Subject:</b> Essential of Data Science", body_style),
            Paragraph("<b>Presenter:</b> Guru Prakash A", body_style),
        ],
        [
            Paragraph("<b>Registration No:</b> 25322011", body_style),
            Paragraph("<b>Class:</b> II MCA", body_style),
        ],
        [
            Paragraph("<b>Department:</b> Dept. of Computer Science & Applications", body_style),
            Paragraph("<b>Presentation Duration:</b> 15 – 20 Minutes", body_style),
        ]
    ]
    meta_table = Table(meta_data, colWidths=[(A4[0]-108)*0.5, (A4[0]-108)*0.5])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#E2E8F0")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 14))

    # ═══════════════════════════════════════════════════════════════════════════
    # PRESENTER'S STAGE DELIVERY RULES
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(Paragraph("🎯 Stage Delivery Guidelines & Best Practices", h1_style))
    story.append(Paragraph(
        "• <b>Pacing & Posture:</b> Maintain an articulate cadence of ~135 words/minute. Stand upright with weight evenly balanced. Make continuous eye contact across the evaluator panel.<br/>"
        "• <b>Interactive Touchpoints:</b> Whenever addressing 3D spatial plots on the live web deck, click, drag, and rotate the WebGL model on screen to prove real-time dynamic interactivity.<br/>"
        "• <b>Transitions:</b> Treat each topic as a natural evolution: from 2D foundations ➔ 3D spatial surfaces ➔ global cartographic projections ➔ multi-variable statistical diagnostics.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # ═══════════════════════════════════════════════════════════════════════════
    # PART 1: WELCOME & FOUNDATIONS
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(HRFlowable(width="100%", thickness=1.5, color=BLUE_PRIMARY, spaceBefore=8, spaceAfter=10))
    story.append(Paragraph("PART 1: Welcome & Foundations (index.html • Slides 1–4)", h1_style))

    story.append(Paragraph("Slide 1: Formal Opening Address & Presenter Introduction", h2_style))
    add_speech_card(
        "Stand confidently at the center of the podium. Smile and address the panel directly.",
        "Respected Head of the Department, honorable faculty evaluators, and my dear colleagues — a very pleasant morning to one and all. I am Guru Prakash A, registering under roll number 25322011, currently pursuing my second year in Master of Computer Applications. Today, under the subject 'Essential of Data Science', I have the privilege of presenting a comprehensive seminar on one of the most critical disciplines in modern computing: Advanced Data Visualization in Python. Over the course of this seminar, we will discover how Python empowers data scientists to model multidimensional spatial geometries, map planetary geodetic coordinates, and distill high-dimensional datasets into publication-grade statistical graphics."
    )

    story.append(Paragraph("Slide 2: The Data Science Pipeline Architecture", h2_style))
    add_speech_card(
        "Advance to Slide 2. Gesture toward the 4-stage flowchart diagram on screen.",
        "Before diving into code, let us look at the bigger picture. In data science, raw data is essentially inert. Our architecture flowchart demonstrates the exact transformation journey: First, Data Ingestion from databases, IoT streams, and satellite telemetry. Second, Preprocessing using Pandas and NumPy to clean nulls and encode features. Third, The Visualization Layer, where data routes into three specialized libraries: Matplotlib mplot3d for spatial surfaces, Basemap and Cartopy for geographic mapping, and Seaborn for statistical modeling. Finally, Executive Insights: empowering leadership and researchers to uncover patterns that pure numbers conceal."
    )

    story.append(Paragraph("Slide 3: What is Data Visualization? Matplotlib's OO Architecture", h2_style))
    add_definition_box(
        "Data Visualization",
        "The graphical representation of quantitative data and information using visual encoding elements (coordinate axes, color gradients, glyph sizes, and contour isolines) to exploit human perceptual bandwidth for rapid pattern recognition and anomaly detection."
    )
    add_speech_card(
        "Emphasize the three-tier hierarchy of Figure -> Axes -> Artists.",
        "In Python, the foundation of all plotting is Matplotlib, engineered by John D. Hunter. To write scalable code, we must master its Object-Oriented Architecture: The Figure represents the top-level canvas. The Axes represents the actual plotting region with coordinate axes. And Artists represent visual primitives — lines, text labels, markers, and colorbars. Understanding this hierarchy eliminates unpredictable global states and gives us absolute programmatic precision."
    )

    story.append(Paragraph("Slide 4: Foundational 2D Plot Archetypes", h2_style))
    add_example_box(
        "Diagnostic Selection of Basic 2D Charts",
        "• <b>Line Plots (plt.plot):</b> Continuous temporal series (e.g. stock equity pricing over time).<br/>"
        "• <b>Scatter Plots (plt.scatter):</b> Bivariate clustering and correlation identification.<br/>"
        "• <b>Histograms (plt.hist):</b> Univariate frequency distributions (Gaussian vs skewed).<br/>"
        "• <b>Box Plots (plt.boxplot):</b> Five-number summaries (Min, Q1, Median, Q3, Max) and IQR outlier detection."
    )

    # ═══════════════════════════════════════════════════════════════════════════
    # PART 2: 3D VISUALIZATION WITH MPLOT3D
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(HRFlowable(width="100%", thickness=1.5, color=PURPLE_ACCENT, spaceBefore=4, spaceAfter=10))
    story.append(Paragraph("PART 2: 3D Visualization with mplot3d (3d-plotting.html • Slides 5–14)", h1_style))

    story.append(Paragraph("Slides 5 & 6: 3D Axes Initialization & Coordinate System", h2_style))
    add_code_card("fig = plt.figure(figsize=(8, 6))\nax = plt.axes(projection='3d')")
    add_speech_card(
        "Navigate to 3d-plotting.html. Point to the orthogonal 3D spatial coordinate axes.",
        "When real-world phenomena involve three continuous variables simultaneously, 2D charts fail. We import Matplotlib's mplot3d toolkit. By specifying projection='3d', Matplotlib instantiates an Axes3D object equipped with three orthogonal spatial axes — X for width, Y for depth, and Z for elevation — complete with real-time perspective distortion and viewing angles."
    )

    story.append(Paragraph("Slide 7: 3D Point Clouds & Parametric Space Curves (Helix)", h2_style))
    add_definition_box(
        "Parametric Space Curve (Helix)",
        "A 3D curve where coordinates (X, Y, Z) are evaluated as continuous mathematical functions of an independent parameter t: X = sin(t), Y = cos(t), Z = t. The particle undergoes circular motion in the X-Y plane while advancing linearly along the Z-axis."
    )
    add_example_box(
        "Aerospace Telemetry & Autonomous Drone Navigation",
        "SpaceX and drone flight controllers track trajectory coordinates (X, Y, Z) through time to verify orbital ascent paths and obstacle avoidance maneuvers."
    )
    add_code_card("z = np.linspace(0, 15, 1000)\nx = np.sin(z); y = np.cos(z)\nax.plot3D(x, y, z, 'gray')\nax.scatter3D(x, y, z, c=z, cmap='plasma')")

    story.append(Paragraph("Slide 8: 3D Contour Plots (ax.contour3D)", h2_style))
    add_definition_box(
        "3D Contour Plot",
        "A graphical technique that connects points of equal elevation (Z) across a 2D grid (X, Y) using smooth isolines, visualizing topographical elevation gradients without surface polygon occlusion."
    )
    add_speech_card(
        "Rotate the 3D contour plot on screen. Point out the binary colormap isolines.",
        "To evaluate continuous 2D mathematical fields like Z = f(X, Y), we use np.meshgrid() to generate 2D coordinate matrices. ax.contour3D then calculates isolines of constant elevation. Civil engineers use this to model dam reservoir basins, assessing water pressure gradients across canyon walls."
    )

    story.append(Paragraph("Slide 9 & 10: Wireframes vs Continuous Surface Plots", h2_style))
    add_example_box(
        "Computer Vision & Formula 1 Aerodynamics",
        "• <b>Wireframes (ax.plot_wireframe):</b> Display structural polygonal skeletons using rstride and cstride grid strides. Used in LiDAR scanning and 3D facial geometry meshes.<br/>"
        "• <b>Continuous Surfaces (ax.plot_surface):</b> Fills polygons with smooth colormap gradients. Formula 1 aerodynamicists use surface plots to analyze air pressure distributions over race car chassis."
    )
    add_speech_card(
        "Click the colormap toggle pills on the web page: switch between Viridis, Plasma, and Coolwarm.",
        "Notice on our live web deck how we can dynamically switch between colormaps: Viridis provides perceptual uniformity for scientific integrity and colorblind accessibility, while Coolwarm highlights positive versus negative thermal deviations."
    )

    story.append(Paragraph("Slides 11 & 12: Unstructured Data & Surface Triangulations (ax.plot_trisurf)", h2_style))
    add_definition_box(
        "Delaunay Triangulation (plot_trisurf)",
        "A geometric algorithm that connects scattered, irregular coplanar points into triangles such that no point lies within the circumcircle of any triangle. It enables smooth surface interpolation over unstructured data without requiring an artificial regular grid."
    )
    add_speech_card(
        "Highlight the Möbius Strip 3D model.",
        "In the field, sensor data arrives as unstructured (X, Y, Z) triples. To demonstrate how Delaunay Triangulation overcomes grid limitations, look at our 3D Möbius Strip on Slide 12. Because a Möbius Strip is a non-orientable topological surface with only one continuous boundary, regular Cartesian grids self-intersect, but plot_trisurf meshes it flawlessly."
    )

    story.append(Paragraph("Slides 13 & 14: Interactive Camera Viewing Parameters (view_init)", h2_style))
    add_speech_card(
        "Drag the 3D plot to change angles, explaining elevation and azimuth.",
        "To prevent visual occlusion where foreground peaks block background valleys, Matplotlib provides programmatic camera control via ax.view_init(elev=30, azim=45). Elevation sets vertical camera angle above the horizon; Azimuth sets rotation around the Z-axis. Scripting loops over view_init creates 360-degree rotational videos."
    )

    # ═══════════════════════════════════════════════════════════════════════════
    # PART 3: GEOGRAPHIC DATA VISUALIZATION
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(HRFlowable(width="100%", thickness=1.5, color=EMERALD_ACCENT, spaceBefore=4, spaceAfter=10))
    story.append(Paragraph("PART 3: Geographic Mapping (basemap.html • Slides 15–22)", h1_style))

    story.append(Paragraph("Slides 15 & 16: The Spherical Projection Paradox & Basemap", h2_style))
    add_definition_box(
        "The Spherical Projection Paradox (Gauss's Theorema Egregium)",
        "The mathematical proof that an oblate spheroid (the Earth) cannot be mapped onto a flat two-dimensional plane without introducing geometric distortion in either surface area, local shape, geodesic distance, or compass direction."
    )
    add_speech_card(
        "Advance to basemap.html. Highlight the curvature of the Earth.",
        "When moving to planetary scales, we encounter Carl Friedrich Gauss's Theorema Egregium: flattening a sphere onto a 2D screen mathematically forces distortion. In Python, the Basemap Toolkit and modern Cartopy resolve this by transforming spherical Latitude and Longitude coordinates into projected map coordinates."
    )

    story.append(Paragraph("Slides 17 & 18: Map Projections (Orthographic vs Mercator vs Robinson)", h2_style))
    add_example_box(
        "Comparative Map Projection Mechanics",
        "• <b>Orthographic ('ortho'):</b> Space perspective view with zero distortion at the center, ideal for hemispheric climate simulation.<br/>"
        "• <b>Mercator ('merc'):</b> Conformal projection preserving navigational compass angles, but severely exaggerates polar landmasses (Greenland appears equal to Africa, though Africa is 14x larger).<br/>"
        "• <b>Robinson ('robin'):</b> Compromise projection balancing shape and area distortions for global socio-economic maps."
    )

    story.append(Paragraph("Slide 19: California Cities Case Study & Multi-Variable Encoding", h2_style))
    add_speech_card(
        "Point to the California bubble map on the slide.",
        "In our California Cities Case Study, we apply multi-dimensional visual encoding: Point position (x, y) establishes precise GPS location; Circle radius encodes population size; and Color gradient maps municipal land area. In one glance, viewers grasp urban density clusters without parsing spreadsheets."
    )

    story.append(Paragraph("Slide 20: Great Circle Flight Routes & Geodesic Navigation", h2_style))
    add_definition_box(
        "Great Circle Route (m.drawgreatcircle)",
        "The shortest geodesic distance between two points on the surface of a sphere, formed by the intersection of the sphere with a plane passing through the Earth's center. On flat Mercator projections, it appears as an upward curved arch toward polar latitudes."
    )
    add_example_box(
        "Aviation Fuel Optimization & Jet Stream Routing",
        "Airlines flying from New York to Tokyo route flights over Alaska because great circle geodesic curves minimize flight mileage, saving thousands of gallons of jet fuel."
    )

    story.append(Paragraph("Slides 21 & 22: Meteorological Overlays & Cartopy Migration", h2_style))
    add_speech_card(
        "Emphasize professional software lifecycle awareness.",
        "Basemap also powers meteorological overlays: using m.contourf(), scientists visualize isobar atmospheric pressure and hurricane wind velocity fields. As professional data scientists, we must note that Basemap has reached end-of-life maintenance and has been succeeded by Cartopy, developed by the UK Met Office using modern C++ PROJ and GEOS libraries."
    )

    # ═══════════════════════════════════════════════════════════════════════════
    # PART 4: STATISTICAL VISUALIZATION WITH SEABORN
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#E11D48"), spaceBefore=4, spaceAfter=10))
    story.append(Paragraph("PART 4: Statistical Visualization with Seaborn (seaborn.html • Slides 23–33)", h1_style))

    story.append(Paragraph("Slides 23 & 24: What is Seaborn? Matplotlib vs Seaborn", h2_style))
    add_speech_card(
        "Advance to seaborn.html. Emphasize developer productivity and declarative syntax.",
        "Now, let us examine Seaborn, created by Michael Waskom. While Matplotlib provides low-level canvas primitives, Seaborn provides a high-level statistical grammar. A grouped scatter plot with categorical legends requires 15 lines of manual Matplotlib code, but only a single declarative line in Seaborn: sns.scatterplot(data=df, x='bill', y='tip', hue='smoker'). It natively implements Tidy Data principles."
    )

    story.append(Paragraph("Slide 25: Univariate Distributions — Histograms & KDE", h2_style))
    add_definition_box(
        "Kernel Density Estimation (KDE)",
        "A non-parametric method to estimate the underlying continuous probability density function of a random variable, smoothing discrete histogram frequency counts using a localized Gaussian kernel function."
    )
    add_speech_card(
        "Point to the smooth density curve over the histogram bars.",
        "Histogram bars are sensitive to arbitrary bin boundaries. By overlaying a Kernel Density Estimation curve via sns.histplot(kde=True), we obtain a smooth, mathematically continuous probability distribution, exposing skewness and multimodal peaks."
    )

    story.append(Paragraph("Slide 26: Bivariate Hexagonal Binning (sns.jointplot)", h2_style))
    add_example_box(
        "Mitigating Big Data Overplotting",
        "In datasets with 500,000 observations, point markers overlap into solid ink blobs. kind='hex' accumulates overlapping points into regular hexagonal bins and colors them by frequency density, revealing the true statistical distribution sweet spots."
    )
    add_speech_card(
        "Highlight the central plot and marginal top/right axes.",
        "sns.jointplot provides a revolutionary layout: it simultaneously renders the central 2D bivariate relationship and the 1D marginal distributions along the top and right margins."
    )

    story.append(Paragraph("Slide 27: Multi-Feature Correlation Matrices (sns.pairplot)", h2_style))
    add_speech_card(
        "Point to the N x N grid layout and class separation.",
        "When evaluating an N-feature machine learning dataset, sns.pairplot constructs an N x N matrix: diagonal subplots display 1D univariate KDE curves, while off-diagonals display pairwise scatter relationships. By setting hue='species', ML engineers instantly spot linearly separable features and eliminate collinear variables."
    )

    story.append(Paragraph("Slide 28: Categorical Distributions — Boxplots vs Violinplots", h2_style))
    add_definition_box(
        "Violin Plot (sns.violinplot)",
        "A hybrid categorical visualization combining the five-number summary of a boxplot (median, quartiles, IQR whiskers) with a mirrored continuous KDE density curve, revealing bimodal distributions that single-number means and standard boxplots conceal."
    )
    add_example_box(
        "Healthcare Emergency Room Triage Times",
        "Two hospital shifts may share identical median wait times on a boxplot, but a violin plot reveals that Shift B is bimodal — separating fast-track patients from critically delayed emergency cases."
    )

    story.append(Paragraph("Slide 29: Correlation Heatmaps (sns.heatmap)", h2_style))
    add_example_box(
        "FinTech Quantitative Risk & Genomic Expression",
        "Quantitative hedge funds compute Pearson correlation matrices across hundreds of equities. A heatmap with annot=True instantly flags pairs of assets with +1.0 correlation, preventing redundant portfolio risk exposure."
    )
    add_code_card("corr = df.corr()\nsns.heatmap(corr, annot=True, fmt='.2f', cmap='YlGnBu', linewidths=0.5)")

    story.append(Paragraph("Slide 30: Linear Regression & 95% Confidence Intervals (sns.lmplot)", h2_style))
    add_definition_box(
        "Bootstrap Confidence Band (sns.lmplot)",
        "A shaded statistical envelope around the Ordinary Least Squares regression line, computed via empirical bootstrap resampling (1,000 iterations), displaying the 95% statistical confidence margin of the predicted slope."
    )
    add_speech_card(
        "Point to the regression slope and translucent confidence ribbon.",
        "Seaborn is not just a plotting library; it is a statistical modeling engine. sns.lmplot fits an OLS regression line and automatically estimates translucent 95% bootstrap confidence bands. A widening band at high dollar values warns business leaders that sample sizes are too small to justify aggressive budget forecasts."
    )

    story.append(Paragraph("Slide 31: Scientific Color Palettes & Accessibility Guidelines", h2_style))
    add_speech_card(
        "Emphasize ethical visualization design.",
        "Data scientists carry an ethical duty to design accessible visuals: Use Qualitative palettes (Set1) for unordered categories; Sequential palettes (viridis) for increasing numbers; and Diverging palettes (coolwarm) for profit vs loss around zero. Never rely on red-vs-green: 8% of men experience deuteranopia color blindness. Viridis ensures legibility even in black-and-white print."
    )

    # ═══════════════════════════════════════════════════════════════════════════
    # PART 5: SYNTHESIS & BENCHMARK MATRIX
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(HRFlowable(width="100%", thickness=1.5, color=NAVY_MAIN, spaceBefore=4, spaceAfter=10))
    story.append(Paragraph("PART 5: Synthesis, Benchmark Matrix & Conclusion (Slides 34–36)", h1_style))

    story.append(Paragraph("Slide 34: 3-Way Comparative Benchmark Matrix", h2_style))
    
    matrix_data = [
        [
            Paragraph("<b>Evaluation Metric</b>", body_style),
            Paragraph("<b>Matplotlib 3D (mplot3d)</b>", body_style),
            Paragraph("<b>Basemap & Cartopy</b>", body_style),
            Paragraph("<b>Seaborn</b>", body_style),
        ],
        [
            Paragraph("<b>Primary Domain</b>", body_style),
            Paragraph("Spatial 3D & Volumetric Surfaces", body_style),
            Paragraph("Geographic GIS & Cartography", body_style),
            Paragraph("Statistical Distributions & Models", body_style),
        ],
        [
            Paragraph("<b>Data Structure</b>", body_style),
            Paragraph("(X, Y, Z) Triples & 2D Meshes", body_style),
            Paragraph("GPS Coordinates & Shapefiles", body_style),
            Paragraph("Tidy Long-Form Pandas DataFrames", body_style),
        ],
        [
            Paragraph("<b>Abstraction Level</b>", body_style),
            Paragraph("Low-Level Imperative Canvas", body_style),
            Paragraph("Mid-Level Cartographic Transforms", body_style),
            Paragraph("High-Level Declarative Grammar", body_style),
        ],
        [
            Paragraph("<b>Greatest Strength</b>", body_style),
            Paragraph("Real-time 3D rotation & Delaunay meshes", body_style),
            Paragraph("Geodesic curves & projections", body_style),
            Paragraph("Automated confidence intervals", body_style),
        ],
        [
            Paragraph("<b>Key Limitation</b>", body_style),
            Paragraph("Verbose layout boilerplate", body_style),
            Paragraph("Basemap deprecated; use Cartopy", body_style),
            Paragraph("2D only; lacks native 3D meshes", body_style),
        ],
        [
            Paragraph("<b>Target Industry</b>", body_style),
            Paragraph("Aerospace, CAD, Biophysics", body_style),
            Paragraph("Aviation, Logistics, Meteorology", body_style),
            Paragraph("Machine Learning, FinTech, Medicine", body_style),
        ]
    ]
    t_matrix = Table(matrix_data, colWidths=[100, 125, 125, 137])
    t_matrix.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1E293B")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#FFFFFF"), colors.HexColor("#F8FAFC")]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t_matrix)
    story.append(Spacer(1, 10))

    story.append(Paragraph("Slide 35 & 36: Cloud QR Ecosystem, Conclusion & Academic Gratitude", h2_style))
    add_speech_card(
        "Point to the four scannable QR code tiles on Slide 35. Step forward for conclusion.",
        "To make this seminar fully reproducible, I have deployed a cloud ecosystem accessible via the four QR codes on screen: QR 1 downloads our official 36-slide PPTX deck; QR 2 opens the full 7-minute English 3D video presentation; QR 3 opens the Tanglish video walkthrough; and QR 4 launches the live interactive WebGL deck on GitHub Pages.<br/><br/>To conclude: 'Data is the new crude oil, but raw data is unrefined and unintelligible. Data visualization is the refinery that transforms raw tabular numbers into human insight, actionable strategy, and scientific breakthrough.' I express my deepest gratitude to our esteemed professors, to my department, and to all of you for your gracious attention. I warmly welcome any questions from the panel. Thank you!"
    )

    # ═══════════════════════════════════════════════════════════════════════════
    # EVALUATION PANEL Q&A DEFENSE
    # ═══════════════════════════════════════════════════════════════════════════
    story.append(PageBreak())
    story.append(HRFlowable(width="100%", thickness=1.5, color=AMBER_ACCENT, spaceBefore=4, spaceAfter=10))
    story.append(Paragraph("🧠 Evaluation Panel Q&A Defense Cheat Sheet", h1_style))
    story.append(Paragraph("Master academic answers to top anticipated questions from evaluating professors:", body_style))
    story.append(Spacer(1, 6))

    qa_items = [
        (
            "Q1: Why should data scientists migrate from Basemap to Cartopy?",
            "Basemap was built over 15 years ago and reached official end-of-life in 2020. It relies on legacy C bindings that frequently fail to compile on modern Python 3.11+ environments. Cartopy, developed by the UK Met Office, is its modern object-oriented successor. It integrates natively with modern PROJ geodetic transformation engines, uses Shapely for topological polygon clipping, and implements Matplotlib's modern GeoAxes interface."
        ),
        (
            "Q2: What is the architectural difference between Figure-level and Axes-level functions in Seaborn?",
            "An Axes-level function (such as sns.scatterplot or sns.histplot) draws directly onto an existing Matplotlib Axes object passed via ax=, making it modular inside complex multi-plot dashboards. A Figure-level function (such as sns.relplot or sns.catplot) manages its own FacetGrid figure canvas, automatically instantiating multiple faceted subplots across categorical rows and columns."
        ),
        (
            "Q3: What causes plot_surface to fail on unstructured (X, Y, Z) points, and how is it resolved?",
            "plot_surface strictly requires 2D matrix arrays generated by np.meshgrid(), where index adjacency maps to topological surface neighbors. Passing scattered 1D vectors causes dimension mismatch errors. To visualize unstructured coordinates, we use ax.plot_trisurf(), which executes Delaunay Triangulation to dynamically construct optimal triangle meshes across irregular point clouds."
        ),
        (
            "Q4: How does Seaborn mathematically compute the 95% Confidence Interval in lmplot?",
            "Seaborn applies non-parametric empirical bootstrap resampling. It draws 1,000 random samples with replacement from the dataset, recalculates the Ordinary Least Squares (OLS) regression slope for each resample, and takes the 2.5th and 97.5th percentiles of the predicted regression distribution to construct the shaded confidence band."
        )
    ]

    for q, a in qa_items:
        story.append(Paragraph(f"<b>{q}</b>", qa_q_style))
        story.append(Paragraph(a, qa_a_style))
        story.append(Spacer(1, 4))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[SUCCESS] PDF successfully created: {PDF_OUTPUT} ({os.path.getsize(PDF_OUTPUT)} bytes)")

if __name__ == "__main__":
    build_pdf()
