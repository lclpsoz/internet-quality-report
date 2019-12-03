from PIL import Image
from random import randint
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Recebe nome da imagem que deve ler
# como uma string
def imRead (strImg):
	img = mpimg.imread(strImg)

	return img
# Recebe imagem (ndarray) e mostra essa imagem
def imShow (img):
	plt.imshow (img, interpolation='nearest')
	plt.show()

# Executa funcoes
def run ():
	imColor = imRead ("graph.png")
	imShow (imColor)

	imShow(imBw[:,:,2], cmap='Greys')

def generateRow (vals, imgName):

    rows = len(vals)//15
    columns = len (vals)

    pts = []
    mat = []
    for i in range (columns):
        mat.append ([0]*rows)

    im= Image.new('RGB', (columns, rows))

    data = []
    for lin in range (rows):
        for i in range (columns):
            data.append ((vals[i]*255, 0, 0))

    im.putdata(data)
    im.save(imgName + '.png')
    imColor = imRead (imgName + '.png')
    imShow (imColor)
'''
vals = []
for i in range (1000):
    vals.append (randint (0, 1))
generateRow (vals)
'''