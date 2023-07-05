import cv2
import os
import sys

# Input folder name as argument if exists
if len(sys.argv) > 1:
    folder = sys.argv[1]
else:
    folder = "frames"

# Open frames/0.png and get the frame size
# folder = "frames_2"
# img = cv2.imread("frames/0.png")
img = cv2.imread(f"{folder}/0.png")
frame_height, frame_width, _ = img.shape

# Open a new video file
# frame_rate = 2  # 2 fps
frame_rate = 30  # 30 fps
codec = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')

video = cv2.VideoWriter('animation.avi', codec, frame_rate, (frame_width, frame_height))

i = 0
while True:
    # check if "frames/{}.png".format(i) exists
    if not os.path.exists(f"{folder}/{i}.png"):
        break

    # Open "frames/{}.png".format(i) and show it
    img = cv2.imread(f"{folder}/{i}.png")

    if img is None:
        print("error: image not found")
        break

    # Print the frame number
    print(f"{folder}/{i}.png")

    # Write the frame to the video file
    video.write(img)

    i += 1

# Close the video file
video.release()
