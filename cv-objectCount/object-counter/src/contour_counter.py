import cv2


def count_contours(binary_image, min_area=100):
    """Find contours and return (count, contours_list).

    binary_image: single-channel (0/255) image
    min_area: minimum contour area to consider an object
    Returns: (count:int, contours:List[ndarray])
    """
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtered = [c for c in contours if cv2.contourArea(c) >= min_area]
    return len(filtered), filtered


# backward-compatible wrapper
def count_objects(edge_image):
    contours, _ = cv2.findContours(edge_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours, len(contours)
