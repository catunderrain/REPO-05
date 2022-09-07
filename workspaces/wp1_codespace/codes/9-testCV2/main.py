# import cv2
# i = 0
# while True:
#     cap = cv2.VideoCapture(0)
#     a, frame = cap.read()
#     print(a)
    
#     cv2.imwrite(f'D:\\do\\workspaces\\wp1_codespace\\codes\\9-testCV2\\{i}.png', frame)
#     cv2.imshow('frame', frame)
#     key = cv2.waitKey(1)
#     i += 1
#     if key == 27:
#         break

import numpy as np
print(np.zeros((3,4), np.uint8).fill(0))