from moviepy.editor import VideoFileClip
from PIL import Image
from analyzer.image_analyzer import classify_image
from utils.label_mapper import map_labels_to_category
from collections import Counter

def analyze_video(video_path):
    try:
        clip = VideoFileClip(video_path)
        duration = clip.duration
        step = max(1, duration // 10)
        predicted_categories = []

        for t in range(0, int(duration), int(step)):
            try:
                frame = clip.get_frame(t)
                img = Image.fromarray(frame)
                labels = classify_image(img)
                category = map_labels_to_category(labels)
                predicted_categories.append(category)
            except Exception as frame_err:
                print(f"⚠️ Skipping frame at {t}s: {frame_err}")

        if not predicted_categories:
            return {"Uncategorized"}

        most_common = Counter(predicted_categories).most_common(1)[0][0]
        return {most_common}

    except Exception as e:
        print(f"❌ Error in analyze_video({video_path}): {e}")
        return {"Uncategorized"}
