import cv2
import os

# Open frames/0.png and get the frame size
img = cv2.imread("frames/0.png")
frame_height, frame_width, _ = img.shape

# Open a new video file
frame_rate = 2  # 2 fps
codec = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')

video = cv2.VideoWriter('animation.avi', codec, frame_rate, (frame_width, frame_height))

i = 0
while True:
    # check if "frames/{}.png".format(i) exists
    if not os.path.exists("frames/{}.png".format(i)):
        break

    # Open "frames/{}.png".format(i) and show it
    img = cv2.imread("frames/{}.png".format(i))

    if img is None:
        print("error: image not found")
        break

    # Print the frame number
    print("frames/{}.png".format(i))

    # Write the frame to the video file
    video.write(img)

    i += 1

# Close the video file
video.release()
