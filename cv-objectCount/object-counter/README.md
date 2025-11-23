# Object Counter

Lightweight computer-vision project that detects and counts objects in images using classic
image-processing techniques (preprocessing + contour detection). It's intended as a small
research/demo tool and a starting point for experimenting with object counting methods.

## Features

- Contour-based object detection and counting.
- Simple preprocessing pipeline (grayscale, blur, edge/threshold).
- CLI runner with headless mode and optional output saving (`src/main.py`).
- Scripts to generate synthetic sample images and batch-run detections (`scripts/`).

## Quick start (PowerShell)

```powershell
Set-Location -Path 'c:\Users\pc\Music\cv-objectCount\object-counter'
C:/Users/pc/Music/cv-objectCount/.venv/Scripts/python.exe -m pip install -r requirements.txt
# run tests
C:/Users/pc/Music/cv-objectCount/.venv/Scripts/python.exe -m pytest -q
# generate a sample image
C:/Users/pc/Music/cv-objectCount/.venv/Scripts/python.exe scripts/generate_sample.py
# run demo (no GUI) and save visualization
C:/Users/pc/Music/cv-objectCount/.venv/Scripts/python.exe -m src.main --image assets/sample_images/coins.jpg --no-gui --output outputs/result.jpg
```

Project layout

- `src/` - source modules (`main.py`, `preprocessing.py`, `contour_counter.py`, `utils.py`)
- `assets/sample_images/` - sample images created/used by scripts
- `scripts/` - helper scripts: `generate_sample.py`, `generate_and_detect.py`, `run_and_describe.py`
- `outputs/` - visualized outputs produced by the demo scripts
- `test/` - unit tests (pytest)

Usage notes

`src/main.py` supports `--no-gui` (headless) and `--output <path>` to save a visualization
instead of opening windows. Run it as a module (`python -m src.main ...`) so package imports
resolve correctly.

`scripts/generate_and_detect.py` creates multiple synthetic images and runs detection with
two `min_area` sensitivity settings, saving visualizations to `outputs/`.

Tuning and improvements

Adjust `min_area` in `src/contour_counter.py` or pass different thresholds when invoking
the counting routine to control sensitivity to small objects.

For overlapping objects consider adding watershed, distance transform, or marker-based
segmentation before contour extraction.

Testing

- Run `pytest` from the project root (uses the configured venv):

```powershell
C:/Users/pc/Music/cv-objectCount/.venv/Scripts/python.exe -m pytest -q
```

If you want, I can: embed example output images into this README, tune preprocessing for
better separation of overlapping objects, or add a CSV exporter summarizing detections.
