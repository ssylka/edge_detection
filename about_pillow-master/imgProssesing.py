from PIL import Image
from PIL import ImageFilter 
from PIL import ImageChops 
import PIL.ImageOps




class RBC():
    def __init__(self, passDir = 'maxresdefault.jpg'):
        with Image.open(passDir) as self.img:
            self.img.load()

    def Add(self,passDir = 'russia.jpg', scale = 2, offset = 0):
        with Image.open(passDir) as img2:
            img2.load()
        self.img = ImageChops.add(self.img, img2,scale,offset)
        return ImageChops.add(self.img, img2,scale,offset)

    def Reverse(self):
        self.img = PIL.ImageOps.invert(self.img)
        return PIL.ImageOps.invert(self.img)
    
    def GaussianBlur(self, intensivity = 10):
        self.img = self.img.filter(ImageFilter.GaussianBlur(intensivity))
        return self.img.filter(ImageFilter.GaussianBlur(intensivity))
    
    def Contrast(self):
        self.img = self.img.filter(ImageFilter.EDGE_ENHANCE)
        return self.img.filter(ImageFilter.EDGE_ENHANCE)

    def FindEdges(self):
        self.img = self.img.filter(ImageFilter.FIND_EDGES)
        return self.img.filter(ImageFilter.FIND_EDGES)

    def Brightness(self, intensivity):
        self.img = ImageChops.add(self.img, self.img, 2, intensivity)
        return ImageChops.add(self.img, self.img, 2, intensivity)
        # brightness range selection is from -255 to 255
        
    def Crop(self, x1,y1,x2,y2):
        self.img  = self.img.crop((x1,y1,x2,y2))
        return self.img.crop((x1,y1,x2,y2))

    def Set(dirPass = 'russia.jpg'):
        with Image.open(passDir) as img2:
            img2.load()
        self.img = img2

    def Get():
        return self.img

    def Show(self):
        self.img.show()



a = RBC('maxresdefault.jpg')
a.Add()
a.Show()
