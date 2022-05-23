#Nome: Bryan Jonathan Melo De Oliveira
#Matricula: 708688

#imports
import matplotlib.pyplot as plt



im = plt.imread("station2.png")
implot = plt.imshow(im)

# put a blue dot at (10, 20)
#plt.scatter([10], [20])

plt.xlim([0,720])
plt.ylim([0,720])

# put a red dot, size 40, at 2 locations:
#plt.scatter(x=[30, 40], y=[50, 60], c='r', s=40)

plt.show()