from PIL import Image 
from numpy import random 


    
def gusian_calculation(img):

    img_bw = img.convert('L')
    return img_bw


filename="1200px-Lenna.png"

with Image.open (filename) as img :
    img.load()



img=gusian_calculation(img)

img.show()