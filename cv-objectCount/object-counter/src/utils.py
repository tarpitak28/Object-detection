import cv2

def draw_contours(image, contours):
    """Draw detected objects on the image."""
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    return image
