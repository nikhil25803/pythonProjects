import matplotlib.pyplot
import numpy as np

arr = np.array(range(10))

arr = np.array([10,20,30])

print(list(arr)) #Array access in Python is based on C language

print(arr[-1])

arr2 = np.array([[10,20,30],[40,50,60]])

print(list(arr2))
print(arr2.shape)


#RGB

img = np.ones(shape=(20, 20, 3), dtype=np.uint8) 

print(img.dtype)

out=img*255

# print(out)
print(out.shape)

import matplotlib.pyplot as plt #Import to present it on a plotting graph

print(plt.imshow(out))

import requests

data=requests.get("https://bgr.com/wp-content/uploads/2019/11/avengers-endgame-iron-man-gauntlet.jpg?quality=82&strip=all")
with open("ironman.png","wb") as f:
    f.write(data.content)


from PIL import Image

img=Image.open("ironman.png")

arrimg=np.array(img)

print(arrimg.shape)

selection = arrimg[0:350,480:810]

plt.imshow(selection)

# plt.imshow(selection.mean(axis=2), cmap="gray") #Make pic Gray
selection[:, :, 0]=0 # Remove redness of a pic
plt.imshow(selection)


matplotlib.pyplot.show() #Will pop a graphical representation














