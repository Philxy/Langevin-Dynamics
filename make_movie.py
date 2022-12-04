import cv2
import os
import natsort 

image_folder = 'Frames2/'
video_name = 'meiden.avi'

images = [img for img in natsort.natsorted(os.listdir(image_folder),reverse=True) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 10, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()