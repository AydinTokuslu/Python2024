import cv2
import imageio

# 1. Get Images
cap = cv2.VideoCapture(1) # harici camera kullanıyorsak 1, bilgisayar kamerası ise 0

while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)

frames = []
image_count = 0
while True:
    ret, frame = cap.read()

    cv2.imshow("frame", frame)

    key = cv2.waitKey(0)
    if key == ord("a"):
        image_count += 1
        frames.append(frame)
        print("Adding new image:", image_count)
    elif key == ord("q"):
        break

print("Images added: ", len(frames))

print("Saving GIF file")
with imageio.get_writer("smiling.gif", mode="I") as writer:
    for idx, frame in enumerate(frames):
        print("Adding frame to GIF file: ", idx + 1)
        writer.append_data(frame)

rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


