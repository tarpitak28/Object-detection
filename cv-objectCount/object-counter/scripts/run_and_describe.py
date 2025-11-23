"""Run preprocessing + counting on the sample image and print a summary.
This uses the project's `src` package.
"""
from pathlib import Path
import cv2

from src.preprocessing import preprocess
from src.contour_counter import count_contours


def main():
    img_path = Path('assets/sample_images/coins.jpg')
    out_path = Path('outputs/result.jpg')

    if not img_path.exists():
        print('Sample image not found:', img_path)
        return

    img = cv2.imread(str(img_path))
    proc = preprocess(img)
    count, contours = count_contours(proc)

    print('Sample image:', img_path)
    print('Image shape (H, W, C):', img.shape)
    print('Processed (single-channel) shape:', proc.shape)
    print('Detected objects (count):', count)
    print('Visualization path:', out_path)

    # optionally load saved visualization to show size
    if out_path.exists():
        import os
        print('Saved visualization exists, size(bytes):', os.path.getsize(out_path))
    else:
        print('Saved visualization not found. Run src.main with --output to save it.')


if __name__ == '__main__':
    main()
