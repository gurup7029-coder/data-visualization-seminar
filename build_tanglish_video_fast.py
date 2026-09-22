import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"E:\sem3\data science\seminar"
VIDEO_ASSETS = os.path.join(BASE_DIR, "video_assets")
TEMP_SLIDES_DIR = os.path.join(VIDEO_ASSETS, "tanglish_clips")
os.makedirs(TEMP_SLIDES_DIR, exist_ok=True)

AVATAR_PATH = os.path.join(BASE_DIR, "assets", "images", "cat_teacher_3d_stick.png")
FINAL_OUTPUT = os.path.join(BASE_DIR, "Data_Visualization_Seminar_Tanglish.mp4")

# Import the 28 SLIDE_SCRIPTS definitions from generate_tanglish_video
from generate_tanglish_video import SLIDE_SCRIPTS

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

try:
    font = ImageFont.truetype("arial.ttf", 32)
except Exception:
    font = ImageFont.load_default()

def render_slide(args):
    idx, item = args
    slide_id = item["id"]
    title = item["title"]
    img_path = os.path.join(VIDEO_ASSETS, f"{slide_id}.png")
    audio_path = os.path.join(VIDEO_ASSETS, f"ta_{slide_id}.mp3")
    clip_output = os.path.join(TEMP_SLIDES_DIR, f"clip_{idx:02d}_{slide_id}.mp4")

    # If valid clip already exists, skip
    if os.path.exists(clip_output) and os.path.getsize(clip_output) > 50000:
        print(f"  [{idx+1:02d}/{len(SLIDE_SCRIPTS):02d}] CACHED: {slide_id}")
        return clip_output

    if not os.path.exists(img_path) or not os.path.exists(audio_path):
        print(f"  [WARN] Skipping slide {idx+1}: {slide_id} (missing image or audio)")
        return None

    # Prepare composite slide background with bottom topic banner
    base_img = Image.open(img_path).convert("RGB")
    draw = ImageDraw.Draw(base_img)
    banner_rect = [0, 1080 - 80, 1920, 1080]
    draw.rectangle(banner_rect, fill=(15, 23, 42))
    draw.text((40, 1080 - 60), f"Slide {idx+1}/{len(SLIDE_SCRIPTS)} • Topic: {title} (Tanglish)", fill=(255, 255, 255), font=font)
    
    prepared_bg = os.path.join(TEMP_SLIDES_DIR, f"bg_{idx:02d}.png")
    base_img.save(prepared_bg)

    cmd = [
        ffmpeg, "-y",
        "-loop", "1", "-i", prepared_bg,
        "-loop", "1", "-i", AVATAR_PATH,
        "-i", audio_path,
        "-filter_complex",
        "[1:v]scale=360:360[av];[0:v][av]overlay=x=1920-380+6*cos(2*PI*0.7*t):y=1080-80-350+12*sin(2*PI*1.4*t):shortest=1[v]",
        "-map", "[v]", "-map", "2:a",
        "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
        "-shortest",
        clip_output
    ]

    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    if res.returncode == 0 and os.path.exists(clip_output) and os.path.getsize(clip_output) > 50000:
        size_kb = os.path.getsize(clip_output) / 1024
        print(f"  [{idx+1:02d}/{len(SLIDE_SCRIPTS):02d}] DONE: {slide_id} ({size_kb:.1f} KB)")
        return clip_output
    else:
        print(f"  [ERROR] Failed slide {idx+1}: {slide_id}")
        return None

def main():
    print(f"--- Fast Multi-Threaded Build for Tanglish Video ({len(SLIDE_SCRIPTS)} slides) ---")
    tasks = [(idx, item) for idx, item in enumerate(SLIDE_SCRIPTS)]
    
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(render_slide, tasks))

    valid_clips = [r for r in results if r is not None and os.path.exists(r) and os.path.getsize(r) > 50000]
    print(f"\nAll {len(valid_clips)}/{len(SLIDE_SCRIPTS)} slide clips ready! Concatenating...")

    concat_list_file = os.path.join(TEMP_SLIDES_DIR, "concat_list.txt")
    with open(concat_list_file, "w", encoding="utf-8") as f:
        for clip in valid_clips:
            escaped_clip = clip.replace("\\", "/")
            f.write(f"file '{escaped_clip}'\n")

    concat_cmd = [
        ffmpeg, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_file,
        "-c", "copy",
        "-movflags", "+faststart",
        FINAL_OUTPUT
    ]

    c_res = subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    if c_res.returncode == 0 and os.path.exists(FINAL_OUTPUT):
        final_size_mb = os.path.getsize(FINAL_OUTPUT) / (1024 * 1024)
        print(f"\n[SUCCESS] Tanglish Presentation Video successfully exported ({final_size_mb:.2f} MB) with Faststart!")
        print(f"   -> {FINAL_OUTPUT}")
    else:
        print("\n[ERROR] Concatenation failed:")
        print(c_res.stderr[-500:])

if __name__ == "__main__":
    main()
