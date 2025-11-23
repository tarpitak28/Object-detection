"""Generate a synthetic sample image with several filled circles (coins).
This writes `assets/sample_images/coins.jpg`.
"""
import cv2
import numpy as np
from pathlib import Path

out_path = Path(__file__).resolve().parents[1] / 'assets' / 'sample_images' / 'coins.jpg'
out_path.parent.mkdir(parents=True, exist_ok=True)

w, h = 600, 400
img = np.full((h, w, 3), 255, dtype=np.uint8)
centers = [(120, 200), (220, 120), (340, 180), (460, 260), (300, 80)]
radii = [40, 30, 35, 28, 25]
for c, r in zip(centers, radii):
    cv2.circle(img, c, r, (160, 160, 160), -1)

# add some small noise / shadows
cv2.circle(img, (220, 120), 10, (120, 120, 120), -1)

cv2.imwrite(str(out_path), img)
print(f"Wrote sample image to: {out_path}")
