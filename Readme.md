# Media Sorter

A simple Python tool to classify and organize media files (images, videos, GIFs) into category folders using a pretrained model and keyword mapping.

---

## Features

* Supports images (`.jpg`, `.jpeg`, `.png`), videos (`.mp4`, `.mov`), and GIFs (`.gif`).
* Uses EfficientNetB3 (ImageNet) to predict labels for frames.
* Maps labels to human-friendly categories (e.g., “dog” → `Pets`, “pizza” → `Food`).
* Samples multiple frames from videos/GIFs and picks the most common category.
* Copies each file into `output/<Category>/`.
* Caches results (`media_cache.json`) so files aren’t re-analyzed on subsequent runs.
* Leverages all CPU cores with a progress bar.

---

## Requirements

* Python 3.8+
* Packages listed in `requirements.txt`

---

## Installation

1. Clone or download this repository:

   ```bash
   git clone https://github.com/yourusername/media-sorter.git
   cd media-sorter/media-sorter
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
   ```

3. Install dependencies:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## Usage

1. **Place your files** in the `data/` folder.

   * Acceptable extensions: `.jpg`, `.jpeg`, `.png`, `.mp4`, `.mov`, `.gif`.

2. (Optional) Review or modify categories in `utils/label_mapper.py`.

3. Run the sorter:

   ```bash
   python main.py
   ```

   * A progress bar will display.
   * Sorted files will be copied into `output/<Category>/`.

4. To reprocess all files, delete `media_cache.json` before rerunning.

---

## Project Structure

```
media-sorter/
└── media-sorter/
    ├── main.py            # Entry point
    ├── requirements.txt   # Dependencies
    ├── run.bat            # Windows shortcut to run main.py
    │
    ├── analyzer/          # Classification logic
    │   ├── image_analyzer.py
    │   ├── video_analyzer.py
    │   └── gif_analyzer.py
    │
    ├── utils/             # Helper functions
    │   ├── cache.py       # Load/save media_cache.json
    │   ├── file_utils.py  # List and copy files
    │   └── label_mapper.py # Map model labels to categories
    │
    ├── data/              # ← Put your media files here
    ├── output/            # ← Sorted output appears here
    └── media_cache.json   # (Generated) Caches results
```

---

## Custom Categories

* Open `utils/label_mapper.py`.
* Edit the `CATEGORY_KEYWORDS` dictionary:

  ```python
  CATEGORY_KEYWORDS = {
      'people': ['person', 'man', 'woman'],
      'pets': ['cat', 'dog'],
      'food': ['pizza', 'cake', 'burger'],
      # …add or update as needed
  }
  ```
* Save and rerun `main.py`.

---

## License

This project is released under the MIT License.
