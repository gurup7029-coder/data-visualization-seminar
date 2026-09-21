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

# 28 Complete Seminar Presentation Slides with Fluent Studio-Grade Tanglish Voice
SLIDE_SCRIPTS = [
    # --- SECTION 1: MATPLOTLIB FOUNDATIONS (index.html) ---
    {
        "id": "index_slide_1",
        "url": "http://localhost:8765/index.html#slide-1",
        "title": "Seminar Opening & Presenter Information",
        "voice": "ta-IN-ValluvarNeural",
        "script": "வணக்கம் மற்றும் வரவேற்பு! Essential of Data Science பாடப்பிரிவின் டேட்டா விஷுவலைசேஷன் செமினாரை வழங்குகிறார் Guru Prakash A, Registration Number 25322011, Second Year MCA. இந்த செமினாரில், டேட்டா விஷுவலைசேஷனின் முக்கியத்துவத்தையும், Python லைப்ரரிகளையும் விரிவாகப் பார்க்கப் போகிறோம்."
    },
    {
        "id": "index_slide_2",
        "url": "http://localhost:8765/index.html#slide-2",
        "title": "Topic Overview & Data Science Flowchart",
        "voice": "ta-IN-ValluvarNeural",
        "script": "இந்த ஃப்ளோசார்ட்டில் காட்டியபடி, நமது செமினாரின் வழிமுறை: Data Loading-ல் தொடங்கி, Data Processing செய்து, பிறகு Matplotlib, 3D Plotting, Basemap மற்றும் Seaborn மூலமாக டேட்டாவை காட்சிப்படுத்தி, இறுதியில் Insights பெறுகிறோம்."
    },
    {
        "id": "index_slide_3",
        "url": "http://localhost:8765/index.html#slide-3",
        "title": "What is Data Visualization? Matplotlib Architecture",
        "voice": "ta-IN-ValluvarNeural",
        "script": "Data Visualization என்பது காம்ப்ளக்ஸ் டேட்டாவை எளிதாகப் புரிந்து கொள்ள உதவும் ஒரு கலை. Matplotlib என்பது Python-ன் முதன்மையான Drawing Engine. இதில் Figure என்பது Canvas, Axes என்பது 2D அல்லது 3D Graph plotting region ஆகும்."
    },
    {
        "id": "index_slide_4",
        "url": "http://localhost:8765/index.html#slide-4",
        "title": "Core Matplotlib Plot Types",
        "voice": "ta-IN-ValluvarNeural",
        "script": "Matplotlib-ல் பல்வேறு பிளாட்டிங் வகைகள் உள்ளன: Line plots டிரெண்டுகளைக் காட்டவும், Scatter plots மாறிகளுக்கு இடையேயான தொடர்பைக் காட்டவும், Histograms விநியோகத்தைக் காட்டவும், Box plots Outliers-ஐக் கண்டுபிடிக்க பயன்படுகின்றன."
    },

    # --- SECTION 2: 3D VISUALIZATION WITH MPLOT3D (3d-plotting.html) ---
    {
        "id": "3d_slide_1",
        "url": "http://localhost:8765/3d-plotting.html#slide-1",
        "title": "3D Data Visualization with mplot3d",
        "voice": "ta-IN-ValluvarNeural",
        "script": "இப்போது 3D Data Visualization-க்கு வருவோம். Matplotlib-ன் mplot3d டூல்கிட் மூலமாக Three-dimensional surface plots, 3D contour, wireframe மற்றும் scatter plots உருவாக்க முடியும்."
    },
    {
        "id": "3d_slide_2",
        "url": "http://localhost:8765/3d-plotting.html#slide-2",
        "title": "3D Points & Line Plots",
        "voice": "ta-IN-ValluvarNeural",
        "script": "3D Points மற்றும் Lines பிளாட் செய்ய projection='3d' அமைக்க வேண்டும். ax scatter3D முப்பரிமாணத்தில் புள்ளிகளையும், ax plot3D முப்பரிமாண சுருள் பாதைகளையும் வரைபடமாக்குகிறது."
    },
    {
        "id": "3d_slide_3",
        "url": "http://localhost:8765/3d-plotting.html#slide-3",
        "title": "3D Contour Plots (ax contour3D)",
        "voice": "ta-IN-ValluvarNeural",
        "script": "3D Contour Plots என்பது ஒரு 3D மேல்பரப்பின் உயரத்தை சமவ உயரக் கோடுகளாக (contour lines) காட்டுகிறது. ax contour3D(X, Y, Z, 50, cmap='binary') கட்டளையைப் பயன்படுத்தி உருவாக்கலாம்."
    },
    {
        "id": "3d_slide_4",
        "url": "http://localhost:8765/3d-plotting.html#slide-4",
        "title": "Wireframe Plots (ax plot_wireframe)",
        "voice": "ta-IN-ValluvarNeural",
        "script": "Wireframe plots என்பது 3D மேல்பரப்பை சட்டகக் கோடுகளாக (grid lines) வெளிப்படுத்துகிறது. ax plot_wireframe(X, Y, Z, color='black') மூலம் இதனை உருவாக்கலாம்."
    },
    {
        "id": "3d_slide_5",
        "url": "http://localhost:8765/3d-plotting.html#slide-5",
        "title": "3D Surface Plots (ax plot_surface)",
        "voice": "ta-IN-ValluvarNeural",
        "script": "3D Surface Plotting என்பது முப்பரிமாணத்தில் வண்ணமயமான பரப்பை உருவாக்குகிறது. Viridis கலர்மேப் மற்றும் rstride, cstride அளவுருக்கள் மூலம் பரப்பின் தரம் கட்டுப்படுத்தப்படுகிறது."
    },
    {
        "id": "3d_slide_6",
        "url": "http://localhost:8765/3d-plotting.html#slide-6",
        "title": "Surface Triangulations (ax plot_trisurf)",
        "voice": "ta-IN-ValluvarNeural",
        "script": "சீரற்ற புள்ளிகள் (Unstructured points) இருந்தால், ax plot_trisurf முக்கோண அமைப்புகளைக் கொண்டு (triangulation) அழகான 3D மேற்பரப்பை அமைக்கிறது."
    },
    {
        "id": "3d_slide_7",
        "url": "http://localhost:8765/3d-plotting.html#slide-7",
        "title": "Mobius Strip 3D Visualization",
        "voice": "ta-IN-ValluvarNeural",
        "script": "Mobius Strip என்பது ஒரு விசித்திரமான ஒருபக்க வடிவம். Python-ல் parametric equations மற்றும் triangulation பயன்படுத்தி இந்த 3D மேபியஸ் நாடாவை நாம் உருவாக்கலாம்."
    },
    {
        "id": "3d_slide_8",
        "url": "http://localhost:8765/3d-plotting.html#slide-8",
        "title": "3D Subplots & Projections",
        "voice": "ta-IN-ValluvarNeural",
        "script": "ஒரு ஒரே figure-ல் பல 3D plots-ஐ பக்கவாட்டில் காட்ட Subplots உதவுகின்றன. வெவ்வேறு கோணங்களில் டேட்டாவை ஒப்பிட இது மிகவும் பயனுள்ளது."
    },
    {
        "id": "3d_slide_9",
        "url": "http://localhost:8765/3d-plotting.html#slide-9",
        "title": "Interactive 3D Viewing Parameters",
        "voice": "ta-IN-ValluvarNeural",
        "script": "ax view_init(elev, azim) கட்டளை மூலம் 3D வரைபடத்தின் உயரக் கோணம் (elevation) மற்றும் சுழல் கோணத்தை (azimuth) மாற்றி அமைக்க முடியும்."
    },

    # --- SECTION 3: GEOGRAPHIC MAPPING WITH BASEMAP (basemap.html) ---
    {
        "id": "basemap_slide_1",
        "url": "http://localhost:8765/basemap.html#slide-1",
        "title": "Geographic Data Visualization & Basemap",
        "voice": "ta-IN-ValluvarNeural",
        "script": "உலக வரைபடத்தில் டேட்டாவை வரைபடமாக்க Basemap டூல்கிட் பயன்படுகிறது. புவியியல் தரவுகளை வரைபடத்தில் துல்லியமாக காட்ட இது உதவுகிறது."
    },
    {
        "id": "basemap_slide_2",
        "url": "http://localhost:8765/basemap.html#slide-2",
        "title": "Map Projections (Orthographic, Robinson, Mercator)",
        "voice": "ta-IN-ValluvarNeural",
        "script": "Basemap-ல் பல வரைபட கணிப்பு முறைகள் (projections) உள்ளன. Orthographic 3D கோள வடிவில் பூமியைக் காட்டுகிறது, Mercator தட்டையான வரைபடத்தைக் காட்டுகிறது."
    },
    {
        "id": "basemap_slide_3",
        "url": "http://localhost:8765/basemap.html#slide-3",
        "title": "Topography & Shaded Relief Maps",
        "voice": "ta-IN-ValluvarNeural",
        "script": "m shadedrelief மற்றும் m bluemarble முறைகள் மூலம் பூமியின் இயற் வடிவம், கடல்கள் மற்றும் நிலப்பரப்பை வண்ண நிழல் படமாக வரையலாம்."
    },
    {
        "id": "basemap_slide_4",
        "url": "http://localhost:8765/basemap.html#slide-4",
        "title": "Plotting Geographic Coordinates & Cities",
        "voice": "ta-IN-ValluvarNeural",
        "script": "நகரங்களின் அட்சரேகை (Latitude) மற்றும் தீர்க்கரேகைகளை (Longitude) Basemap-ல் m scatter மூலம் புள்ளிகளாகவும், பெயர்களாகவும் குறிக்கலாம்."
    },
    {
        "id": "basemap_slide_5",
        "url": "http://localhost:8765/basemap.html#slide-5",
        "title": "Great Circle Flight Routes & Distances",
        "voice": "ta-IN-ValluvarNeural",
        "script": "m drawgreatcircle கட்டளை இரண்டு நகரங்களுக்கு இடையே உள்ள மிகக் குறுகிய விமானப் பாதையை வளைந்த கோடாக வரைபடத்தில் காட்டுகிறது."
    },
    {
        "id": "basemap_slide_6",
        "url": "http://localhost:8765/basemap.html#slide-6",
        "title": "Climate Data & Contour Overlay on Maps",
        "voice": "ta-IN-ValluvarNeural",
        "script": "வரைபடத்தின் மேல் தப்பவெப்ப நிலை மற்றும் மழைப்பொழிவு டேட்டாவை 2D Contour கோடுகளாக வரைபடமாக்க m contour பயன்படுகிறது."
    },
    {
        "id": "basemap_slide_7",
        "url": "http://localhost:8765/basemap.html#slide-7",
        "title": "California Cities Geographic Case Study",
        "voice": "ta-IN-ValluvarNeural",
        "script": "கலிஃபோர்னியா நகரங்களின் மக்கள் தொகை மற்றும் பரப்பளவை வண்ணங்கள் மற்றும் அளவுகள் மூலம் Basemap-ல் காட்டும் Case Study இதுவாகும்."
    },

    # --- SECTION 4: STATISTICAL VISUALIZATION WITH SEABORN (seaborn.html) ---
    {
        "id": "seaborn_slide_1",
        "url": "http://localhost:8765/seaborn.html#slide-1",
        "title": "High-Level Statistical Visualization with Seaborn",
        "voice": "ta-IN-ValluvarNeural",
        "script": "Seaborn என்பது Matplotlib-ன் மேல் அமைந்த ஒரு உயர்நிலை லைப்ரரி. இது நவீன வண்ணங்கள், தானியங்கி ஸ்டைலிங் மற்றும் புள்ளியியல் வரைபடங்களை எளிதில் உருவாக்க உதவுகிறது."
    },
    {
        "id": "seaborn_slide_2",
        "url": "http://localhost:8765/seaborn.html#slide-2",
        "title": "Matplotlib vs Seaborn Code Comparison",
        "voice": "ta-IN-ValluvarNeural",
        "script": "Matplotlib-ல் பல வரிகள் எழுத வேண்டிய குறியீட்டை, Seaborn ஒற்றை வரியில் அழகிய பாணியில் உருவாக்கி விடும். இந்த ஒப்பீட்டைப் பாருங்கள்."
    },
    {
        "id": "seaborn_slide_3",
        "url": "http://localhost:8765/seaborn.html#slide-3",
        "title": "Histograms & Kernel Density Estimation (KDE)",
        "voice": "ta-IN-ValluvarNeural",
        "script": "sns histplot மற்றும் sns kdeplot மூலம் டேட்டாவின் விநியோகத்தை (distribution) மென்மையான வளைகோடாகக் கணக்கிட்டு வரையலாம்."
    },
    {
        "id": "seaborn_slide_4",
        "url": "http://localhost:8765/seaborn.html#slide-4",
        "title": "Pair Plots (sns pairplot) & Iris Dataset",
        "voice": "ta-IN-ValluvarNeural",
        "script": "Iris தரவுத்தொகுப்பின் அனைத்து பண்புகளுக்கும் இடையேயான தொடர்பை sns pairplot ஒரே மேட்ரிக்ஸில் அழகாகக் காட்டுகிறது."
    },
    {
        "id": "seaborn_slide_5",
        "url": "http://localhost:8765/seaborn.html#slide-5",
        "title": "Faceted Grids (sns FacetGrid) & Flight Data",
        "voice": "ta-IN-ValluvarNeural",
        "script": "sns FacetGrid துணைப்பிரிவுகள் வாரியாக டேட்டாவைப் பிரித்து பல சிறிய வரைபடங்களாக (small multiples) காட்டுகிறது."
    },
    {
        "id": "seaborn_slide_6",
        "url": "http://localhost:8765/seaborn.html#slide-6",
        "title": "Categorical Plots (sns catplot, boxplot, violinplot)",
        "voice": "ta-IN-ValluvarNeural",
        "script": "sns catplot வகைப்படுத்தப்பட்ட தரவுகளுக்கு Box plots, Violin plots மற்றும் Bar plots வரைந்து ஒப்பிட உதவுகிறது."
    },
    {
        "id": "seaborn_slide_7",
        "url": "http://localhost:8765/seaborn.html#slide-7",
        "title": "2D Heatmaps (sns heatmap) & Correlation Matrices",
        "voice": "ta-IN-ValluvarNeural",
        "script": "sns heatmap மாறிகளுக்கு இடையேயான தொடர்பை (correlation matrix) வண்ண தீவிரத்தின் மூலம் காட்டும் சக்திவாய்ந்த வரைபடம்."
    },
    {
        "id": "seaborn_slide_8",
        "url": "http://localhost:8765/seaborn.html#slide-8",
        "title": "Seminar Conclusion & Thank You",
        "voice": "ta-IN-ValluvarNeural",
        "script": "நன்றி! நமது டேட்டா விஷுவலைசேஷன் செமினாரை இவ்வளவு நேரமாக ஆர்வத்துடன் கவனித்த உங்கள் அனைவருக்கும் எனது மனமார்ந்த நன்றிகள்! வாழ்க வளமுடன்!"
    }
]

async def generate_audio_files():
    print("--- 1. Generating Tanglish Neural Voice Narration Clips ---")
    for idx, item in enumerate(SLIDE_SCRIPTS):
        audio_path = os.path.join(OUTPUT_DIR, f"ta_{item['id']}.mp3")
        if not os.path.exists(audio_path) or os.path.getsize(audio_path) == 0:
            print(f"[{idx+1}/{len(SLIDE_SCRIPTS)}] Generating Tanglish TTS for {item['id']}: {item['title']}...")
            communicate = edge_tts.Communicate(item['script'], item['voice'])
            await communicate.save(audio_path)
    print("[OK] All 28 Tanglish TTS audio clips generated successfully!")

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
    print("--- 3. Compositing 3D Cartoon Teacher Presentation Video (Tanglish) ---")
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
        audio_path = os.path.join(OUTPUT_DIR, f"ta_{item['id']}.mp3")

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
        draw.text((40, 1080 - 60), f"Slide {idx+1}/{len(SLIDE_SCRIPTS)} • Topic: {item['title']} (Tanglish)", fill=(255, 255, 255), font=font)

        # Dynamic Animated Frame Generator function
        def make_frame(t, bg_img=base_slide_img, avatar=cat_avatar):
            if avatar is None:
                return np.array(bg_img)
            
            y_bounce = int(12 * math.sin(2 * math.pi * 1.4 * t))
            x_sway = int(6 * math.cos(2 * math.pi * 0.7 * t))
            
            frame_img = bg_img.copy()
            avatar_x = 1920 - 380 + x_sway
            avatar_y = 1080 - 80 - 350 + y_bounce
            frame_img.paste(avatar, (avatar_x, avatar_y), avatar)
            return np.array(frame_img)

        video_clip = VideoClip(make_frame, duration=duration).with_audio(audio_clip)
        clips.append(video_clip)

    print(f"Concatenating {len(clips)} slide video scenes...")
    final_video = concatenate_videoclips(clips)
    output_mp4 = r"E:\sem3\data science\seminar\Data_Visualization_Seminar_Tanglish.mp4"
    
    print(f"Exporting final Tanglish MP4 video to {output_mp4}...")
    final_video.write_videofile(
        output_mp4,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        preset="ultrafast",
        threads=4
    )
    print("[SUCCESS] Professional Cartoon Tanglish Presentation Video created at:", output_mp4)

async def main():
    await generate_audio_files()
    capture_slide_screenshots()
    create_presentation_video()

if __name__ == "__main__":
    asyncio.run(main())
