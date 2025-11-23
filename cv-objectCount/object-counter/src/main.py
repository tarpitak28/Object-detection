import argparse
import os
from pathlib import Path

import cv2

from src.preprocessing import preprocess
from src.contour_counter import count_contours


def draw_contours_on_image(image, contours, count):
    out = image.copy()
    cv2.drawContours(out, contours, -1, (0, 255, 0), 2)
    cv2.putText(out, f"Objects Detected: {count}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--no-gui", action="store_true", help="Do not open GUI windows")
    parser.add_argument("--output", help="Path to save visualized output (optional)")
    args = parser.parse_args()

    img_path = Path(args.image)
    if not img_path.exists():
        raise SystemExit(f"Image not found: {img_path}")

    img = cv2.imread(str(img_path))
    proc = preprocess(img)
    count, contours = count_contours(proc)

    out = draw_contours_on_image(img, contours, count)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        cv2.imwrite(str(out_path), out)
        print(f"Saved output to: {out_path}")

    if not args.no_gui:
        cv2.imshow('Original', img)
        cv2.imshow('Processed', proc)
        cv2.imshow('Detected', out)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
