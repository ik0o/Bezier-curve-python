import cv2
import numpy as np

t = 0
mpos = []
image = np.zeros((750,750), np.uint8)
cv2.namedWindow("i")

# linear interpolation between 2 point using t value
def lerp(a,b,c):
    out = np.array((1-c)*a + c*b)
    return out

# function for find point at any t on n-point Bézier curve 
def find(pos,c):
    n = np.array([],np.uint)
    for i in range(len(pos)-1):
        for j in range(len(pos)-1):
            n = np.append(n, lerp(pos[0],pos[1],c))
            n = n.reshape((len(n)//2, 2))
            pos = np.delete(pos, 0, axis=0)
        pos = np.copy(n)
        n = []
    return pos

# function for get mouse position in cv2
def mouse(event, x, y, flags, param):
    global mpos
    if event == cv2.EVENT_LBUTTONDOWN:
       pos = [y,x]
       mpos.append(pos)
       image[tuple(pos)] = 200

# count control point and write down their coordinates      
cv2.imshow("i", image)
while 1:
    cv2.setMouseCallback('i', mouse)
    if cv2.waitKey(0) & 0xFF == ord("a"):
        break
    cv2.imshow("i", image)

# drawing Bézier curve
while 1:
    p = np.uint(np.around(find(np.array(mpos),t)[0]))
    image[tuple(p)] = 200
    cv2.imshow("i", image)
    if cv2.waitKey(1) & 0xFF == ord('q') or t > 1:
        break
    t += 0.001
cv2.waitKey(0)
