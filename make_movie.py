import cv2
import os


image_folder = 'Frames'
video_name = 'video.mp4'


os.system("ffmpeg -r 20 -i Frames/%01d.png -vcodec mpeg4 -y -vb 40M movie.mp4")

