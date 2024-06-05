import cv2
import numpy as np

image = cv2.imread('right.png')
image = cv2.resize(image, (1280, 720))

src = np.array([
  [ [ 3424.169677734375, 2178 ] ],
  [ [ 3424.169677734375, 1734.711669921875 ] ],
  [ [ 2876.065185546875, 1734.711669921875 ] ],
  [ [ 2876.204833984375, 1319.8680419921875 ] ],
  [ [ 3241.3984375, 1382.3765869140625 ] ],
  [ [ 3424.169677734375, 1382.3765869140625 ] ],
  [ [ 3241.3984375, 795.6234130859375 ] ],
  [ [ 3424.169677734375, 795.6234130859375 ] ]

], dtype=np.float32).reshape(-1,1,2)

dst = np.array([
  [ [ 1187.764404296875, 471.2115478515625 ] ],
  [ [ 774.3653564453125, 374.49517822265625 ] ],
  [ [ 327.45672607421875, 471.4711608886719 ] ],
  [ [ 47.69711685180664, 382.5096130371094 ] ],
  [ [ 407.3125, 340.2788391113281 ] ],
  [ [ 530.4759521484375, 317.89422607421875 ] ],
  [ [ 94.97115325927734, 260.8461608886719 ] ],
  [ [ 216.74038696289062, 245.5048065185547 ] ]
], dtype=np.float32).reshape(-1,1,2)

for i, point in enumerate(dst):
    print(point[0])
    image = cv2.circle(image, (int(point[0][0]), int(point[0][1])), radius=6, color=(0, 0, 255), thickness=-1)


corners = np.array([ 
 [ [ 0, 0 ] ], 
 [ [ 3488, 0 ] ], 
 [ [ 3488, 2178 ] ], 
 [ [ 0, 2178 ] ] 
], dtype=np.float32).reshape(-1,1,2)

H, mask = cv2.findHomography(src, dst, cv2.RANSAC)

# arr = np.asarray(H, dtype=np.float32)
# H = np.linalg.inv(arr)

transformed_corners = cv2.perspectiveTransform(corners, H)
print(transformed_corners)


for i, point in enumerate(transformed_corners):
    image = cv2.circle(image, (int(point[0][0]), int(point[0][1])), radius=6, color=(0, 255, 0), thickness=-1)

# Draw lines between the corners
for i in range(len(transformed_corners)):
    start_point = (int(transformed_corners[i][0][0]), int(transformed_corners[i][0][1]))
    end_point = (int(transformed_corners[(i + 1) % len(transformed_corners)][0][0]), int(transformed_corners[(i + 1) % len(transformed_corners)][0][1]))
    image = cv2.line(image, start_point, end_point, color=(255, 0, 0), thickness=2)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()