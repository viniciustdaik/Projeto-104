import cv2  # python solar_planets.py

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sol", (90, 100), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=3.6, color=(0, 125, 255))

cv2.putText(img, "Mercurio", (110, 170), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1.0, color=(175, 175, 175))

cv2.putText(img, "Venus", (180, 265), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1.0, color=(0, 125, 255))

cv2.putText(img, "Terra", (255, 175), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1.0, color=(0, 255, 0))


cv2.putText(img, "Lua", (325, 160), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.7, color=(175, 175, 175))

cv2.putText(img, "Marte", (365, 180), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1.0, color=(0, 0, 255))

cv2.putText(img, "Jupiter", (445, 80), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1.0, color=(0, 105, 155))


cv2.putText(img, "Saturno", (785, 130), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1.0, color=(0, 105, 155))

cv2.putText(img, "Urano", (957, 145), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1.0, color=(255, 255, 255))

cv2.putText(img, "Netuno", (1100, 145), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1.0, color=(255, 0, 105))


cv2.imshow("resultado", img)
cv2.waitKey(0)
