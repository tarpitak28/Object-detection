# Project Statement

## Objective

Build a lightweight, easy-to-run object counting tool using classic computer-vision
techniques. The project demonstrates how preprocessing and contour detection can be
combined to locate and count distinct objects in an image and produce a visualization
highlighting detected objects.

## Approach

- Preprocessing: convert to grayscale, blur, and either edge-detect or threshold to
	produce a binary image suitable for contour extraction.
- Contour detection: use OpenCV's `findContours` and filter by area (`min_area`) to
	remove small noise.
- Visualization: draw detected contours and annotate the image with a count. Provide
	a headless mode to save images without opening GUI windows.

## Deliverables

- `src/`: modular code (`preprocessing.py`, `contour_counter.py`, `main.py`, `utils.py`).
- `scripts/`: helper scripts to generate synthetic images and batch-run detection.
- `test/`: unit test(s) validating counting behavior on synthetic inputs.

## Limitations & Next Steps

- Overlapping objects can merge into single contours; improve separation with
	distance-transform + watershed or marker-based segmentation for more accurate
	instance separation.
- The approach is tuned for high-contrast, relatively uniform objects (coins, blobs).
	For complex scenes consider adopting deep-learning instance segmentation (Mask R-CNN
	or U-Net) or advanced classical methods.

## Evaluation

Use synthetic images and ground-truth counts (as in `scripts/`) to validate behavior
across `min_area` values and preprocessing variants. The repository includes a basic
pytest unit that demonstrates expected counts on a small synthetic image.

If you want, I can add a short evaluation notebook that calculates precision/recall
on a small labeled dataset and visualizes failure cases.
