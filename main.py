import cv2 as cv
import cv2
video_1 = cv.VideoCapture('videonuz.mp4')

ayirt_edici = cv.createBackgroundSubtractorMOG2(90,50)

while 1:
	ret,frame = video_1.read()
	if ret:
		filtrele = ayirt_edici.apply(frame)
		cv2.imshow('Filtre',filtrele)
		if cv2.waitKey(5) == ord('z'):
			break
	else:
		video_2 = cv2.VideoCapture('videonuz.mp4')
cv2.destroyAllWindows()
vide.relase()


