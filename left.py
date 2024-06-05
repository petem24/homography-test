import cv2
import numpy as np

image = cv2.imread('left.png')
image = cv2.resize(image, (1280, 720))

src = np.array([
 [ [ 63.83039855957031, 1734.711669921875 ] ],
 [ [ 611.9346923828125, 1734.711669921875 ] ],
 [ [ 611.9346923828125, 443.288330078125 ] ],
 [ [ 63.83039855957031, 443.288330078125 ] ]
], dtype=np.float32).reshape(-1,1,2)

dst = np.array([
 [ [ 24.28842544555664, 292.6755065917969 ] ],
 [ [ 517.95068359375, 383.7571105957031 ] ],
 [ [ 1154.307373046875, 149.98101806640625 ] ],
 [ [ 768.7286376953125, 111.72675323486328 ] ]
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