import imageio
from PIL import Image
from analyzer.image_analyzer import classify_image
from utils.label_mapper import map_labels_to_category
from collections import Counter

def analyze_gif(gif_path):
    try:
        gif = imageio.mimread(gif_path)
        step = max(1, len(gif) // 10)
        predicted_categories = []

        for i in range(0, len(gif), step):
            try:
                frame = Image.fromarray(gif[i])
                labels = classify_image(frame)
                category = map_labels_to_category(labels)
                predicted_categories.append(category)
            except Exception as frame_err:
                print(f"⚠️ Skipping frame {i}: {frame_err}")

        if not predicted_categories:
            return {"Uncategorized"}

        most_common = Counter(predicted_categories).most_common(1)[0][0]
        return {most_common}

    except Exception as e:
        print(f"❌ Error in analyze_gif({gif_path}): {e}")
        return {"Uncategorized"}
