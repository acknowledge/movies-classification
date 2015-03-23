def hull_ratio(img):
    cnt = extract_contour(img)
    hull = cv2.convexHull(cnt)
    areaValid = cv2.contourArea(cnt)
    hullArea = cv2.contourArea(hull)
    return areaValid/hullArea