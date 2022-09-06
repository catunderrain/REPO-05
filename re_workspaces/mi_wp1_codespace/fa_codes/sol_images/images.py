import cv2
import os
import numpy
import matplotlib.image as img
import matplotlib.pyplot as plt
numpy.set_printoptions(threshold=numpy.inf)

path = 'D:\\do\\re_workspaces\\mi_wp1_codespace\\fa_codes\\sol_images\\'
image = cv2.imread(path + 'test.png')
print(image)
print(image.shape)
matrix = numpy.array([0, 1, 1, 0, 1, 1, 0, 1, 1])
# mxn m-2 n-2
m = image.shape[1]
n = image.shape[0]

def multi(img, mat):
    for ni in range(n-2):
        for mi in range(m-2):
            img[ni][mi][0] = numpy.uint8(img[ni][mi][0] * mat[0])
            img[ni][mi+1][0] = numpy.uint8(img[ni][mi+1][0] * mat[1])
            img[ni][mi+2][0] = numpy.uint8(img[ni][mi+2][0] * mat[2])
            img[ni+1][mi][0] = numpy.uint8(img[ni+1][mi][0] * mat[3]) 
            img[ni+1][mi+1][0] = numpy.uint8(img[ni+1][mi+1][0] * mat[4]) 
            img[ni+1][mi+2][0] = numpy.uint8(img[ni+1][mi+2][0] * mat[5]) 
            img[ni+2][mi][0] = numpy.uint8(img[ni+2][mi][0] * mat[6]) 
            img[ni+2][mi+1][0] = numpy.uint8(img[ni+2][mi+1][0] * mat[7])
            img[ni+2][mi+2][0] = numpy.uint8(img[ni+2][mi+2][0] * mat[8]) 
            
            img[ni][mi][1] = numpy.uint8(img[ni][mi][0] * mat[0]) 
            img[ni][mi+1][1] = numpy.uint8(img[ni][mi+1][0] * mat[1]) 
            img[ni][mi+2][1] = numpy.uint8(img[ni][mi+2][0] * mat[2]) 
            img[ni+1][mi][1] = numpy.uint8(img[ni+1][mi][0] * mat[3]) 
            img[ni+1][mi+1][1] = numpy.uint8(img[ni+1][mi+1][0] * mat[4])
            img[ni+1][mi+2][1] = numpy.uint8(img[ni+1][mi+2][0] * mat[5]) 
            img[ni+2][mi][1] = numpy.uint8(img[ni+2][mi][0] * mat[6]) 
            img[ni+2][mi+1][1] = numpy.uint8(img[ni+2][mi+1][0] * mat[7])
            img[ni+2][mi+2][1] = numpy.uint8(img[ni+2][mi+2][0] * mat[8]) 
            
            img[ni][mi][2] = numpy.uint8(img[ni][mi][0] * mat[0]) 
            img[ni][mi+1][2] = numpy.uint8(img[ni][mi+1][0] * mat[1]) 
            img[ni][mi+2][2] = numpy.uint8(img[ni][mi+2][0] * mat[2]) 
            img[ni+1][mi][2] = numpy.uint8(img[ni+1][mi][0] * mat[3])
            img[ni+1][mi+1][2] = numpy.uint8(img[ni+1][mi+1][0] * mat[4])
            img[ni+1][mi+2][2] = numpy.uint8(img[ni+1][mi+2][0] * mat[5])
            img[ni+2][mi][2] = numpy.uint8(img[ni+2][mi][0] * mat[6]) 
            img[ni+2][mi+1][2] = numpy.uint8(img[ni+2][mi+1][0] * mat[7])
            img[ni+2][mi+2][2] = numpy.uint8(img[ni+2][mi+2][0] * mat[8]) 


image = multi(image, matrix)

try:
    os.remove('D:\\do\\re_workspaces\\mi_wp1_codespace\\fa_codes\\sol_images\\re.png')
except:
    print('Deleted.')
cv2.imwrite('D:\\do\\re_workspaces\\mi_wp1_codespace\\fa_codes\\sol_images\\re.png', numpy.array(image))