"""Generate multiple synthetic images and run the object counter on each.

Saves images to `assets/sample_images/` and visualizations to `outputs/`.
Prints a concise summary table of detections.
"""
from pathlib import Path
import cv2
import numpy as np
import os

from src.preprocessing import preprocess
from src.contour_counter import count_contours

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets' / 'sample_images'
OUT = ROOT / 'outputs'
ASSETS.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)


def save(img, path: Path):
    cv2.imwrite(str(path), img)


def draw_and_save(orig, contours, count, out_path: Path):
    out = orig.copy()
    cv2.drawContours(out, contours, -1, (0, 255, 0), 2)
    cv2.putText(out, f"Count: {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    save(out, out_path)


def gen_coins(name='coins_5.jpg', centers=None, radii=None, size=(600, 400)):
    if centers is None:
        centers = [(120, 200), (220, 120), (340, 180), (460, 260), (300, 80)]
    if radii is None:
        radii = [40, 30, 35, 28, 25][: len(centers)]
    img = np.full((size[1], size[0], 3), 255, dtype=np.uint8)
    for c, r in zip(centers, radii):
        cv2.circle(img, c, r, (160, 160, 160), -1)
    return img


def gen_overlap(name='coins_overlap.jpg', size=(600, 400)):
    centers = [(150, 200), (180, 220), (210, 200), (260, 190), (300, 210), (340, 190), (380, 210), (420, 200)]
    radii = [40] * len(centers)
    img = np.full((size[1], size[0], 3), 255, dtype=np.uint8)
    for c, r in zip(centers, radii):
        cv2.circle(img, c, r, (150, 150, 150), -1)
    return img


def gen_many_small(name='many_small.jpg', size=(600, 400)):
    img = np.full((size[1], size[0], 3), 255, dtype=np.uint8)
    rng = np.random.RandomState(1)
    for _ in range(30):
        c = (int(rng.uniform(20, size[0]-20)), int(rng.uniform(20, size[1]-20)))
        r = int(rng.uniform(5, 12))
        cv2.circle(img, c, r, (120, 120, 120), -1)
    return img


def gen_mixed(name='mixed.jpg', size=(600, 400)):
    img = np.full((size[1], size[0], 3), 255, dtype=np.uint8)
    # rectangles
    cv2.rectangle(img, (50, 50), (150, 140), (150, 150, 150), -1)
    cv2.rectangle(img, (200, 250), (270, 330), (160, 160, 160), -1)
    # circles
    cv2.circle(img, (400, 120), 35, (140, 140, 140), -1)
    cv2.circle(img, (480, 280), 28, (130, 130, 130), -1)
    return img


def run_on_image(img, img_name):
    # save original
    in_path = ASSETS / img_name
    out_path = OUT / f"result_{img_name}"
    save(img, in_path)

    proc = preprocess(img)
    # run two sensitivities
    results = {}
    for min_area in (300, 50):
        count, contours = count_contours(proc, min_area=min_area)
        outp = OUT / f"result_{img_name.stem}_ma{min_area}.jpg" if hasattr(img_name, 'stem') else OUT / f"result_{Path(img_name).stem}_ma{min_area}.jpg"
        draw_and_save(img, contours, count, outp)
        results[min_area] = (count, outp)
    return in_path, results


def main():
    specs = [
        ('coins_5.jpg', gen_coins),
        ('coins_overlap.jpg', gen_overlap),
        ('many_small.jpg', gen_many_small),
        ('mixed.jpg', gen_mixed),
    ]

    summary = []
    for name, gen in specs:
        img = gen(name)
        in_path, results = run_on_image(img, name)
        summary.append((in_path, results))

    print('\nSummary of detections:')
    for in_path, results in summary:
        print(f"\nImage: {in_path}")
        for ma, (count, outp) in results.items():
            print(f"  min_area={ma}: detected={count}, visualization={outp}")


if __name__ == '__main__':
    main()
