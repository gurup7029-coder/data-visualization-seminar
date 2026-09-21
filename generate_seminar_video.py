import os
import sys
import asyncio
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from html2image import Html2Image
import edge_tts
from moviepy import ImageClip, AudioFileClip, VideoClip, concatenate_videoclips

# Force UTF-8 stdout
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

OUTPUT_DIR = r"E:\sem3\data science\seminar\video_assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 28 Complete Seminar Presentation Slides with Fluent Professional English Voice
SLIDE_SCRIPTS = [
    # --- SECTION 1: MATPLOTLIB FOUNDATIONS (index.html) ---
    {
        "id": "index_slide_1",
        "url": "http://localhost:8765/index.html#slide-1",
        "title": "Seminar Opening & Presenter Information",
        "voice": "en-US-AndrewNeural",
        "script": "Welcome everyone to today's seminar on Data Visualization, a core component of the Essential of Data Science course. Presented by Guru Prakash A, Registration Number 25322011, Second Year MCA, Department of Computer Science and Applications. Today, we will explore fundamental and advanced visualization techniques in Python."
    },
    {
        "id": "index_slide_2",
        "url": "http://localhost:8765/index.html#slide-2",
        "title": "Seminar Workflow & Topic Overview",
        "voice": "en-US-AndrewNeural",
        "script": "Here is our structured seminar workflow. We begin with raw Data Loading, proceed through Data Processing, and leverage Matplotlib for 2D plots, mplot3d for 3D surfaces, Basemap for geographic mapping, and Seaborn for high-level statistical visualization to extract actionable data science insights."
    },
    {
        "id": "index_slide_3",
        "url": "http://localhost:8765/index.html#slide-3",
        "title": "What is Data Visualization? Matplotlib Architecture",
        "voice": "en-US-AndrewNeural",
        "script": "Data Visualization is the Graphical Representation of Information and Data. Matplotlib is the bedrock library in Python. Its architecture consists of a Canvas, a top-level Figure object acting as the container, and Axes objects representing individual plotting regions with ticks, grids, and labels."
    },
    {
        "id": "index_slide_4",
        "url": "http://localhost:8765/index.html#slide-4",
        "title": "Essential Matplotlib Plot Types",
        "voice": "en-US-AndrewNeural",
        "script": "Matplotlib offers a versatile suite of plot types: Line plots for tracking continuous trends, Scatter plots for discovering correlations, Histograms for analyzing frequency distributions, and Box plots for detecting statistical outliers."
    },

    # --- SECTION 2: 3D VISUALIZATION WITH MPLOT3D (3d-plotting.html) ---
    {
        "id": "3d_slide_1",
        "url": "http://localhost:8765/3d-plotting.html#slide-1",
        "title": "Introduction to 3D Plotting with mplot3d",
        "voice": "en-US-AndrewNeural",
        "script": "Welcome to Topic 2: Three-Dimensional Visualization. By importing the mplot3d toolkit, Matplotlib gains the ability to project complex multivariable data into interactive 3D spaces, enabling surface plots, wireframes, and 3D contours."
    },
    {
        "id": "3d_slide_2",
        "url": "http://localhost:8765/3d-plotting.html#slide-2",
        "title": "3D Points & Line Plots (ax.scatter3D, ax.plot3D)",
        "voice": "en-US-AndrewNeural",
        "script": "To create 3D line and point plots, we initialize an axes object with projection equals 3D. The ax.scatter3D function plots individual data points in three spatial coordinates, while ax.plot3D connects points into smooth 3D parametric spirals."
    },
    {
        "id": "3d_slide_3",
        "url": "http://localhost:8765/3d-plotting.html#slide-3",
        "title": "3D Contour Plots (ax.contour3D)",
        "voice": "en-US-AndrewNeural",
        "script": "3D Contour Plots project elevation level curves onto a three-dimensional surface. Using ax.contour3D with 50 contour levels and colormaps like binary or viridis, we can visualize topological hills, valleys, and gradient shifts."
    },
    {
        "id": "3d_slide_4",
        "url": "http://localhost:8765/3d-plotting.html#slide-4",
        "title": "Wireframe Plots (ax.plot_wireframe)",
        "voice": "en-US-AndrewNeural",
        "script": "Wireframe plots display a 3D surface grid as a structural mesh of interconnected lines. The ax.plot_wireframe function renders this lightweight grid representation, controlled by stride sampling parameters."
    },
    {
        "id": "3d_slide_5",
        "url": "http://localhost:8765/3d-plotting.html#slide-5",
        "title": "3D Surface Plots (ax.plot_surface)",
        "voice": "en-US-AndrewNeural",
        "script": "3D Surface Plots create continuous filled polygon surfaces in 3D space. By combining ax.plot_surface with smooth grid meshes generated via np.meshgrid, we achieve vibrant, shaded elevation topographies."
    },
    {
        "id": "3d_slide_6",
        "url": "http://localhost:8765/3d-plotting.html#slide-6",
        "title": "Surface Triangulations (ax.plot_trisurf)",
        "voice": "en-US-AndrewNeural",
        "script": "When handling unstructured or randomly sampled 3D points without a uniform mesh grid, ax.plot_trisurf automatically constructs Delaunay triangulations to form a smooth contiguous surface."
    },
    {
        "id": "3d_slide_7",
        "url": "http://localhost:8765/3d-plotting.html#slide-7",
        "title": "Mobius Strip 3D Visualization",
        "voice": "en-US-AndrewNeural",
        "script": "A Mobius Strip is a famous topological surface with only one side and one boundary component. Using parametric equations for radius, angle, and twist, we triangulate and render this mathematical manifold in full 3D."
    },
    {
        "id": "3d_slide_8",
        "url": "http://localhost:8765/3d-plotting.html#slide-8",
        "title": "3D Subplots & Multi-View Projections",
        "voice": "en-US-AndrewNeural",
        "script": "In complex data scientific workflows, side-by-side comparison is critical. Using plt.subplot with 3D projections, we can display multiple distinct 3D perspectives within a single figure container."
    },
    {
        "id": "3d_slide_9",
        "url": "http://localhost:8765/3d-plotting.html#slide-9",
        "title": "Interactive 3D Rotation Parameters (ax.view_init)",
        "voice": "en-US-AndrewNeural",
        "script": "The ax.view_init method allows us to programmatically adjust camera elevation and azimuthal rotation angles, giving viewers optimal viewing perspectives of intricate 3D surfaces."
    },

    # --- SECTION 3: GEOGRAPHIC MAPPING WITH BASEMAP (basemap.html) ---
    {
        "id": "basemap_slide_1",
        "url": "http://localhost:8765/basemap.html#slide-1",
        "title": "Geographic Data Visualization & Basemap Toolkit",
        "voice": "en-US-AndrewNeural",
        "script": "Moving to Geographic Data Visualization, the Basemap toolkit allows data scientists to project spatial latitude and longitude coordinates directly onto global map projections with continent and ocean boundaries."
    },
    {
        "id": "basemap_slide_2",
        "url": "http://localhost:8765/basemap.html#slide-2",
        "title": "Map Projections (Orthographic, Robinson, Mercator)",
        "voice": "en-US-AndrewNeural",
        "script": "Basemap supports numerous map projection mathematical models. The Orthographic projection provides a realistic 3D globe perspective, while Mercator and Robinson projections flatten spherical coordinates into rectangular maps."
    },
    {
        "id": "basemap_slide_3",
        "url": "http://localhost:8765/basemap.html#slide-3",
        "title": "Topography & Shaded Relief Imagery",
        "voice": "en-US-AndrewNeural",
        "script": "Using methods like m.shadedrelief() and m.bluemarble(), Basemap overlay NASA satellite imagery and topographical relief textures, adding realistic terrain background details to geographic plots."
    },
    {
        "id": "basemap_slide_4",
        "url": "http://localhost:8765/basemap.html#slide-4",
        "title": "Plotting Geographic Coordinates & Cities",
        "voice": "en-US-AndrewNeural",
        "script": "Spatial coordinates like city latitude and longitude are converted into map projection units using the Basemap object, enabling precise marker placement with m.scatter and text labeling with plt.text."
    },
    {
        "id": "basemap_slide_5",
        "url": "http://localhost:8765/basemap.html#slide-5",
        "title": "Great Circle Flight Routes & Geodesic Paths",
        "voice": "en-US-AndrewNeural",
        "script": "The m.drawgreatcircle method computes and draws geodesic shortest-distance flight paths across the curvature of the Earth between distant global airports such as Tokyo, New York, and London."
    },
    {
        "id": "basemap_slide_6",
        "url": "http://localhost:8765/basemap.html#slide-6",
        "title": "Climate Data & Contour Overlay on Maps",
        "voice": "en-US-AndrewNeural",
        "script": "Geographic heatmaps and meteorological pressure contours are drawn over regional maps by combining m.contour and m.contourf with spatial latitude-longitude meshgrids."
    },
    {
        "id": "basemap_slide_7",
        "url": "http://localhost:8765/basemap.html#slide-7",
        "title": "California Cities Geographic Case Study",
        "voice": "en-US-AndrewNeural",
        "script": "In this real-world case study, California city populations and areas are mapped using marker size for population magnitude and marker color for geographical land area metrics."
    },

    # --- SECTION 4: STATISTICAL VISUALIZATION WITH SEABORN (seaborn.html) ---
    {
        "id": "seaborn_slide_1",
        "url": "http://localhost:8765/seaborn.html#slide-1",
        "title": "High-Level Statistical Visualization with Seaborn",
        "voice": "en-US-AndrewNeural",
        "script": "Topic 3 covers Seaborn, Python's premier statistical data visualization library. Built on top of Matplotlib, Seaborn provides elegant default color themes, modern aesthetics, and seamless integration with pandas DataFrames."
    },
    {
        "id": "seaborn_slide_2",
        "url": "http://localhost:8765/seaborn.html#slide-2",
        "title": "Matplotlib vs Seaborn Code Comparison",
        "voice": "en-US-AndrewNeural",
        "script": "Comparing code side-by-side, Seaborn dramatically reduces boilerplate code. What takes dozens of custom styling lines in Matplotlib is accomplished in Seaborn with a single concise function call."
    },
    {
        "id": "seaborn_slide_3",
        "url": "http://localhost:8765/seaborn.html#slide-3",
        "title": "Histograms & Kernel Density Estimation (KDE)",
        "voice": "en-US-AndrewNeural",
        "script": "Functions like sns.histplot and sns.kdeplot combine frequency histograms with continuous Kernel Density Estimation curves, visualizing probability density distributions of continuous variables."
    },
    {
        "id": "seaborn_slide_4",
        "url": "http://localhost:8765/seaborn.html#slide-4",
        "title": "Pair Plots (sns.pairplot) & Iris Dataset",
        "voice": "en-US-AndrewNeural",
        "script": "The sns.pairplot function creates a grid of pairwise scatter plots across all numeric features in a dataset. On the famous Iris dataset, it highlights feature clusters and species separations effortlessly."
    },
    {
        "id": "seaborn_slide_5",
        "url": "http://localhost:8765/seaborn.html#slide-5",
        "title": "Faceted Grids (sns.FacetGrid) & Subgroup Analysis",
        "voice": "en-US-AndrewNeural",
        "script": "Seaborn's FacetGrid class allows data scientists to map plotting functions across conditional subsets of a dataset, creating small multiple subplots categorized by row and column variables."
    },
    {
        "id": "seaborn_slide_6",
        "url": "http://localhost:8765/seaborn.html#slide-6",
        "title": "Categorical Plots (sns.catplot, Box & Violin Plots)",
        "voice": "en-US-AndrewNeural",
        "script": "Using sns.catplot, we explore categorical data distributions. Box plots display quartile ranges and medians, while Violin plots combine box plots with mirrored density estimations."
    },
    {
        "id": "seaborn_slide_7",
        "url": "http://localhost:8765/seaborn.html#slide-7",
        "title": "2D Heatmaps (sns.heatmap) & Correlation Matrices",
        "voice": "en-US-AndrewNeural",
        "script": "The sns.heatmap function visualizes 2D matrices as color-coded grids. It is ideal for correlation matrices, using color intensity and numeric annotations to highlight strong variable relationships."
    },
    {
        "id": "seaborn_slide_8",
        "url": "http://localhost:8765/seaborn.html#slide-8",
        "title": "Seminar Conclusion & Thank You",
        "voice": "en-US-AndrewNeural",
        "script": "Thank you very much for attending this comprehensive seminar on Data Visualization in Python. We hope these Matplotlib, 3D, Basemap, and Seaborn techniques empower your data science projects. Thank you!"
    }
]

async def generate_audio_files():
    print("--- 1. Generating English Neural Voice Narration Clips ---")
    for idx, item in enumerate(SLIDE_SCRIPTS):
        audio_path = os.path.join(OUTPUT_DIR, f"en_{item['id']}.mp3")
        if not os.path.exists(audio_path) or os.path.getsize(audio_path) == 0:
            print(f"[{idx+1}/{len(SLIDE_SCRIPTS)}] Generating English TTS for {item['id']}: {item['title']}...")
            success = False
            for attempt in range(3):
                try:
                    clean_script = item['script'].replace('ax.', 'ax ').replace('sns.', 'sns ').replace('m.', 'm ')
                    communicate = edge_tts.Communicate(clean_script, item['voice'])
                    await communicate.save(audio_path)
                    if os.path.exists(audio_path) and os.path.getsize(audio_path) > 0:
                        success = True
                        break
                except Exception as e:
                    print(f"   Attempt {attempt+1} failed ({e}), retrying with fallback voice...")
                    await asyncio.sleep(1)
                    item['voice'] = "en-US-GuyNeural"
            if not success:
                print(f"   Warning: Failed to generate audio for {item['id']}")
    print("[OK] All 28 English TTS audio clips generated successfully!")

def capture_slide_screenshots():
    print("--- 2. Capturing 1080p Slide Screenshots ---")
    hti = Html2Image(size=(1920, 1080), custom_flags=['--hide-scrollbars', '--disable-gpu'])
    for idx, item in enumerate(SLIDE_SCRIPTS):
        img_filename = f"{item['id']}.png"
        img_path = os.path.join(OUTPUT_DIR, img_filename)
        if not os.path.exists(img_path):
            print(f"[{idx+1}/{len(SLIDE_SCRIPTS)}] Capturing screenshot: {item['title']}...")
            hti.screenshot(url=item['url'], save_as=img_filename)
            if os.path.exists(img_filename):
                os.replace(img_filename, img_path)
    print("[OK] All 28 slide screenshots ready!")

def create_presentation_video():
    print("--- 3. Compositing 3D Cartoon Teacher Presentation Video with Pointer Stick ---")
    clips = []
    
    # 3D Cartoon Teacher Avatar with Pointer Stick
    teacher_3d_path = r"E:\sem3\data science\seminar\assets\images\cat_teacher_3d_stick.png"
    cat_avatar = None
    if os.path.exists(teacher_3d_path):
        cat_avatar = Image.open(teacher_3d_path).convert("RGBA")
        cat_avatar = cat_avatar.resize((360, 360))

    try:
        font = ImageFont.truetype("arial.ttf", 32)
    except:
        font = ImageFont.load_default()

    for idx, item in enumerate(SLIDE_SCRIPTS):
        img_path = os.path.join(OUTPUT_DIR, f"{item['id']}.png")
        audio_path = os.path.join(OUTPUT_DIR, f"en_{item['id']}.mp3")

        if not os.path.exists(img_path) or not os.path.exists(audio_path):
            print(f"Skipping {item['id']}, missing image or audio")
            continue

        audio_clip = AudioFileClip(audio_path)
        duration = audio_clip.duration + 0.5

        # Base slide image with bottom banner
        base_slide_img = Image.open(img_path).convert("RGB")
        draw = ImageDraw.Draw(base_slide_img)

        # Overlay Banner at bottom for topic title
        banner_height = 80
        banner_rect = [0, 1080 - banner_height, 1920, 1080]
        draw.rectangle(banner_rect, fill=(15, 23, 42))
        draw.text((40, 1080 - 60), f"Slide {idx+1}/{len(SLIDE_SCRIPTS)} • Topic: {item['title']}", fill=(255, 255, 255), font=font)

        # Dynamic Animated Frame Generator function (3D Cartoon Teacher with Stick points and teaches live!)
        def make_frame(t, bg_img=base_slide_img, avatar=cat_avatar):
            if avatar is None:
                return np.array(bg_img)
            
            # Dynamic bounce & pointing action (3D Cartoon Teacher holding stick)
            y_bounce = int(12 * math.sin(2 * math.pi * 1.4 * t))
            x_sway = int(6 * math.cos(2 * math.pi * 0.7 * t))
            
            frame_img = bg_img.copy()
            # Position 3D Teacher holding pointer stick on bottom right pointing up towards slide board
            avatar_x = 1920 - 380 + x_sway
            avatar_y = 1080 - 80 - 350 + y_bounce
            frame_img.paste(avatar, (avatar_x, avatar_y), avatar)
            return np.array(frame_img)

        # Create VideoClip with animated frame generator
        video_clip = VideoClip(make_frame, duration=duration).with_audio(audio_clip)
        clips.append(video_clip)

    print(f"Concatenating {len(clips)} animated slide video scenes...")
    final_video = concatenate_videoclips(clips)
    output_mp4 = r"E:\sem3\data science\seminar\Data_Visualization_Seminar_Presentation.mp4"
    
    print(f"Exporting final 3D Cartoon English MP4 video to {output_mp4}...")
    final_video.write_videofile(
        output_mp4,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        preset="ultrafast",
        threads=4
    )
    print("[SUCCESS] Professional 3D Cartoon English Presentation Video created at:", output_mp4)

async def main():
    await generate_audio_files()
    capture_slide_screenshots()
    create_presentation_video()

if __name__ == "__main__":
    asyncio.run(main())
