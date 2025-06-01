import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
from utils.file_utils import get_media_files, move_file_to_category
from analyzer.image_analyzer import analyze_image_file
from analyzer.video_analyzer import analyze_video
from analyzer.gif_analyzer import analyze_gif
from utils.cache import load_cache, save_cache

SOURCE = 'data'     # <-- UPDATE THIS
DEST = 'output'    # <-- UPDATE THIS

cache = load_cache()

def process_file(file_path):
    if file_path in cache:
        return (file_path, cache[file_path])

    ext = file_path.lower()
    try:
        if os.path.getsize(file_path) > 100 * 1024 * 1024:
            return (file_path, ["Skipped (large file)"])

        if ext.endswith(('.jpg', '.jpeg', '.png')):
            categories = analyze_image_file(file_path)
        elif ext.endswith(('.mp4', '.mov')):
            categories = analyze_video(file_path)
        elif ext.endswith('.gif'):
            categories = analyze_gif(file_path)
        else:
            categories = ["Uncategorized"]

        move_file_to_category(file_path, categories, DEST)
        cache[file_path] = categories
        return (file_path, categories)
    except Exception as e:
        return (file_path, [f"Error: {str(e)}"])

if __name__ == '__main__':
    files = get_media_files(SOURCE)
    with Pool(processes=cpu_count()) as pool:
        for file_path, categories in tqdm(pool.imap_unordered(process_file, files), total=len(files)):
            pass

    save_cache(cache)
    print("✅ Done. Media sorted and cached.")
